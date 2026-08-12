(() => {
  'use strict';

  const normalize = value => (value || '')
    .toString()
    .normalize('NFKC')
    .toLocaleLowerCase('ja')
    .replace(/\s+/g, ' ')
    .trim();

  const roundFor = number => {
    if (number <= 36) return '1';
    if (number <= 104) return '2';
    if (number <= 140) return '3';
    return '4';
  };

  const setup = panel => {
    const scope = panel.dataset.filterScope;
    const isConversation = scope === 'conversations';
    const cardSelector = isConversation ? '.card.conversation[id^="conv-"]' : '.card.note[id^="note-"]';
    const cards = Array.from(document.querySelectorAll(cardSelector));
    if (!cards.length) return;

    const query = panel.querySelector('[data-filter="query"]');
    const character = panel.querySelector('[data-filter="character"]');
    const event = panel.querySelector('[data-filter="event"]');
    const round = panel.querySelector('[data-filter="round"]');
    const topic = panel.querySelector('[data-filter="topic"]');
    const reset = panel.querySelector('.filter-reset');
    const count = panel.querySelector('[data-filter-count]');
    const empty = document.querySelector('[data-filter-empty]');
    const total = cards.length;

    const searchable = new Map(cards.map(card => [card, normalize(card.textContent)]));

    const apply = () => {
      const q = normalize(query?.value);
      const person = normalize(character?.value);
      const eventValue = event?.value || '';
      const roundValue = round?.value || '';
      const topicValue = topic?.value || '';
      let visible = 0;

      for (const card of cards) {
        const number = Number((card.id.match(/(\d+)$/) || [])[1]);
        const title = normalize(card.querySelector('h2')?.textContent);
        const text = searchable.get(card);
        const matchesQuery = !q || text.includes(q);
        const matchesCharacter = !person || title.includes(person);
        const matchesEvent = !eventValue || (eventValue === 'yes' ? !!card.querySelector('.result-event-yes') : !card.querySelector('.result-event-yes'));
        const matchesRound = !roundValue || roundFor(number) === roundValue;
        const matchesTopic = !topicValue || !!card.querySelector(`.topic-${topicValue}`);
        const show = matchesQuery && matchesCharacter && matchesEvent && matchesRound && matchesTopic;
        card.hidden = !show;
        if (show) visible += 1;
      }

      const active = !!(q || person || eventValue || roundValue || topicValue);
      document.body.classList.toggle('records-filtering', isConversation && active);
      if (count) count.textContent = `${visible} / ${total}件`;
      if (empty) empty.hidden = visible !== 0;
    };

    for (const control of panel.querySelectorAll('input, select')) {
      control.addEventListener(control.tagName === 'INPUT' ? 'input' : 'change', apply);
    }

    reset?.addEventListener('click', () => {
      for (const control of panel.querySelectorAll('input, select')) control.value = '';
      apply();
      query?.focus();
    });

    apply();
  };

  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.record-filter[data-filter-scope]').forEach(setup);
  });
})();
