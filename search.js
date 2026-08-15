(() => {
  'use strict';

  const normalize = value => (value || '')
    .toString()
    .normalize('NFKC')
    .toLocaleLowerCase('ja')
    .replace(/\s+/g, ' ')
    .trim();

  const roundFor = number => {
    if (!Number.isFinite(number)) return 'supplement';
    if (number <= 36) return '1';
    if (number <= 104) return '2';
    if (number <= 140) return '3';
    if (number <= 176) return '4';
    if (number <= 212) return '5';
    return '6';
  };

  const setup = panel => {
    const scope = panel.dataset.filterScope;
    const isConversation = scope === 'conversations';
    const isPairRecords = scope === 'pairs';
    const isPairIndex = scope === 'pair-index';
    const isPair = isPairRecords || isPairIndex;
    const isWorld = scope === 'world';
    const selectors = {
      conversations: '.card.conversation[id^="conv-"]',
      notes: '.card[id^="note-"]',
      pairs: '.pairgroup[id^="pair-"]',
      'pair-index': '.pair-index-entry',
      world: 'section.card[id]'
    };
    const cardSelector = selectors[scope];
    if (!cardSelector) return;
    const cards = Array.from(document.querySelectorAll(cardSelector));
    if (!cards.length) return;

    const query = panel.querySelector('[data-filter="query"]');
    const character = panel.querySelector('[data-filter="character"]');
    const event = panel.querySelector('[data-filter="event"]');
    const round = panel.querySelector('[data-filter="round"]');
    const topic = panel.querySelector('[data-filter="topic"]');
    const area = panel.querySelector('[data-filter="area"]');
    const status = panel.querySelector('[data-filter="status"]');
    const reset = panel.querySelector('.filter-reset');
    const count = panel.querySelector('[data-filter-count]');
    const empty = document.querySelector('[data-filter-empty]');
    const total = cards.length;
    const worldArchive = isWorld ? document.getElementById('past-observations') : null;
    const worldArchiveWasOpen = !!worldArchive?.open;

    const searchable = new Map(cards.map(card => [
      card,
      normalize(`${card.textContent} ${card.dataset.search || ''}`)
    ]));

    const apply = () => {
      const q = normalize(query?.value);
      const person = normalize(character?.value);
      const eventValue = event?.value || '';
      const roundValue = round?.value || '';
      const topicValue = topic?.value || '';
      const areaValue = area?.value || '';
      const statusValue = status?.value || '';
      let visible = 0;
      let visibleArchive = 0;

      for (const card of cards) {
        const number = Number((card.id.match(/(\d+)$/) || [])[1]);
        const title = normalize(card.dataset.pair || card.querySelector('h2')?.textContent);
        const text = searchable.get(card);
        const inArchive = !!worldArchive?.contains(card);
        const hasAnyStatus = !!card.querySelector('.status-confirmed, .status-hypothesis, .status-refuted, .status-withdrawn');
        const matchesQuery = !q || text.includes(q);
        const matchesCharacter = !person || title.includes(person);
        const matchesEvent = !eventValue || (eventValue === 'yes' ? !!card.querySelector('.result-event-yes') : !card.querySelector('.result-event-yes'));
        const matchesRound = !roundValue || roundFor(number) === roundValue;
        const matchesTopic = !topicValue || !!card.querySelector(`.topic-${topicValue}`);
        const matchesArea = !areaValue || (areaValue === 'archive' ? inArchive : !inArchive);
        const matchesStatus = !statusValue || (statusValue === 'unlabeled' ? !hasAnyStatus : !!card.querySelector(`.status-${statusValue}`));
        const show = matchesQuery && matchesCharacter && matchesEvent && matchesRound && matchesTopic && matchesArea && matchesStatus;
        card.hidden = !show;
        if (show) {
          visible += 1;
          if (inArchive) visibleArchive += 1;
        }
      }

      const active = !!(q || person || eventValue || roundValue || topicValue || areaValue || statusValue);
      document.body.classList.toggle('records-filtering', (isConversation || isPairRecords || isWorld) && active);
      if (worldArchive) {
        worldArchive.hidden = active && visibleArchive === 0;
        if (active && visibleArchive > 0) worldArchive.open = true;
        if (!active) {
          worldArchive.hidden = false;
          worldArchive.open = worldArchiveWasOpen;
        }
      }
      if (count) count.textContent = `${visible} / ${total}${isPair ? 'ペア' : '件'}`;
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
