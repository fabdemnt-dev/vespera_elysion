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
    if (number <= 248) return '6';
    if (number <= 258) return '7';
    if (number <= 265) return '8';
    if (number <= 272) return '9';
    if (number <= 278) return '10';
    if (number <= 285) return '11';
    if (number <= 291) return '12';
    if (number <= 297) return '13';
    if (number <= 303) return '14';
    if (number <= 307) return '15';
    if (number <= 311) return '16';
    if (number <= 315) return '17';
    if (number <= 319) return '18';
    if (number <= 323) return '19';
    if (number <= 326) return '20';
    if (number <= 328) return '21';
    if (number <= 330) return '22';
    if (number <= 332) return '23';
    if (number <= 334) return '24';
    if (number <= 336) return '25';
    if (number <= 338) return '26';
    if (number <= 340) return '27';
    if (number <= 342) return '28';
    if (number <= 344) return '29';
    if (number <= 346) return '30';
    if (number <= 348) return '31';
    if (number <= 350) return '32';
    if (number <= 352) return '33';
    if (number <= 354) return '34';
    if (number <= 356) return '35';
    if (number <= 358) return '36';
    if (number <= 360) return '37';
    if (number <= 362) return '38';
    if (number <= 364) return '39';
    if (number <= 366) return '40';
    if (number <= 368) return '41';
    if (number <= 377) return '42';
    if (number <= 379) return '43';
    if (number <= 381) return '44';
    return 'supplement';
  };

  const setup = panel => {
    const scope = panel.dataset.filterScope;
    const isConversation = scope === 'conversations';
    const isPairRecords = scope === 'pairs';
    const isPairIndex = scope === 'pair-index';
    const isPair = isPairRecords || isPairIndex;
    const isWorld = scope === 'world';
    const selectors = { conversations: '.card.conversation[id^="conv-"]', notes: '.card[id^="note-"]', pairs: '.pairgroup[id^="pair-"]', 'pair-index': '.pair-index-entry', world: 'section.card[id]', events: '.event-timeline .event-entry' };
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
    const searchable = new Map(cards.map(card => [card, normalize(`${card.textContent} ${card.dataset.search || ''}`)]));
    const apply = () => {
      const q = normalize(query?.value), person = normalize(character?.value), eventValue = event?.value || '', roundValue = round?.value || '', topicValue = topic?.value || '', areaValue = area?.value || '', statusValue = status?.value || '';
      let visible = 0, visibleArchive = 0;
      for (const card of cards) {
        const number = Number((card.id.match(/(\d+)$/) || [])[1]);
        const title = normalize(card.dataset.pair || card.querySelector('h2')?.textContent);
        const text = searchable.get(card), inArchive = !!worldArchive?.contains(card);
        const hasAnyStatus = !!card.querySelector('.status-confirmed, .status-hypothesis, .status-refuted, .status-withdrawn');
        const show = (!q || text.includes(q)) && (!person || title.includes(person)) && (!eventValue || (eventValue === 'yes' ? !!card.querySelector('.result-event-yes') : !card.querySelector('.result-event-yes'))) && (!roundValue || roundFor(number) === roundValue) && (!topicValue || !!card.querySelector(`.topic-${topicValue}`)) && (!areaValue || (areaValue === 'archive' ? inArchive : !inArchive)) && (!statusValue || (statusValue === 'unlabeled' ? !hasAnyStatus : !!card.querySelector(`.status-${statusValue}`)));
        card.hidden = !show;
        if (show) { visible += 1; if (inArchive) visibleArchive += 1; }
      }
      const active = !!(q || person || eventValue || roundValue || topicValue || areaValue || statusValue);
      document.body.classList.toggle('records-filtering', (isConversation || isPairRecords || isWorld) && active);
      if (worldArchive) {
        worldArchive.hidden = active && visibleArchive === 0;
        if (active && visibleArchive > 0) worldArchive.open = true;
        if (!active) { worldArchive.hidden = false; worldArchive.open = worldArchiveWasOpen; }
      }
      if (count) count.textContent = `${visible} / ${total}${isPair ? 'ペア' : '件'}`;
      if (empty) empty.hidden = visible !== 0;
    };
    for (const control of panel.querySelectorAll('input, select')) control.addEventListener(control.tagName === 'INPUT' ? 'input' : 'change', apply);
    reset?.addEventListener('click', () => { for (const control of panel.querySelectorAll('input, select')) control.value = ''; apply(); query?.focus(); });
    apply();
  };

  document.addEventListener('DOMContentLoaded', async () => {
    document.querySelectorAll('.record-filter[data-filter-scope]').forEach(setup);
  });
})();