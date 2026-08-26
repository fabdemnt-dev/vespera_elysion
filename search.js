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
    return 'supplement';
  };

  const round42Pairs = {
    6: { count: 7, numbers: '#6 / #56 / #137 / #173 / #209 / #245 / #375', added: [375], state: '終了' },
    11: { count: 46, numbers: '#11 / #51 / #77 / #128 / #164 / #200 / #236 / #255 / #262 / #269 / #276 / #282 / #289 / #295 / #301 / #306 / #310 / #314 / #318 / #322 / #325 / #328 / #330 / #332 / #334 / #336 / #338 / #340 / #342 / #344 / #346 / #348 / #350 / #352 / #354 / #356 / #358 / #360 / #362 / #364 / #366 / #368 / #370 / #372 / #374 / #379', added: [370, 372, 374], state: '継続中' },
    23: { count: 11, numbers: '#23 / #47 / #88 / #135 / #171 / #207 / #243 / #258 / #265 / #272 / #377', added: [377], state: '終了' },
    26: { count: 7, numbers: '#26 / #62 / #107 / #143 / #179 / #215 / #376', added: [376], state: '終了' },
    32: { count: 46, numbers: '#32 / #54 / #76 / #93 / #119 / #155 / #191 / #227 / #253 / #260 / #267 / #274 / #280 / #287 / #293 / #299 / #304 / #308 / #312 / #316 / #320 / #324 / #327 / #329 / #331 / #333 / #335 / #337 / #339 / #341 / #343 / #345 / #347 / #349 / #351 / #353 / #355 / #357 / #359 / #361 / #363 / #365 / #367 / #369 / #371 / #373 / #378', added: [369, 371, 373], state: '継続中' }
  };

  const syncPairIndex = () => {
    if (!/\/pairs\.html$/.test(location.pathname)) return;
    for (const [id, spec] of Object.entries(round42Pairs)) {
      const link = document.querySelector(`.pair-index-entry[href$="#pair-${id}"]`);
      if (!link) continue;
      const pairName = link.dataset.pair || link.textContent.replace(/（.*$/, '').trim();
      link.textContent = `${pairName}（${spec.count}件）— ${spec.state}`;
      link.dataset.search = `${spec.numbers} ${spec.state}`;
    }
    const callout = document.querySelector('.intro .callout');
    if (callout) callout.innerHTML = '<strong>#379終了時点の会話状態：</strong>継続中2組 / 終了34組。42周目は継続2組に加え、終了挙動比較として3組を再観察しました。 <a href="elysion_observation/conversation_status.md">判定一覧と根拠を見る</a>';
  };

  const syncPairGroups = async () => {
    const m = location.pathname.match(/\/pairs\/group(\d{2}-\d{2})\.html$/);
    if (!m) return;
    const idsByGroup = { '01-06': [6], '07-12': [11], '19-24': [23], '25-30': [26], '31-36': [32] };
    const ids = idsByGroup[m[1]];
    if (!ids) return;
    let source;
    try {
      const response = await fetch('../conversations/round42.html');
      if (!response.ok) return;
      source = new DOMParser().parseFromString(await response.text(), 'text/html');
    } catch (_) { return; }

    for (const id of ids) {
      const spec = round42Pairs[id];
      const group = document.getElementById(`pair-${id}`);
      if (!group) continue;
      group.querySelector('.paircount')?.replaceChildren(document.createTextNode(`${spec.count}件`));
      const numbers = group.querySelector('.pairnumbers');
      if (numbers) numbers.textContent = `記録番号：${spec.numbers}`;
      const tocLink = document.querySelector(`.pairtoc a[href="#pair-${id}"]`);
      if (tocLink) {
        const pairName = group.querySelector('.pairhead h2')?.textContent || '';
        tocLink.textContent = `${pairName}（${spec.count}件）— ${spec.state}`;
      }
      for (const number of spec.added) {
        if (document.getElementById(`pairconv-${number}`)) continue;
        const original = source.getElementById(`conv-${number}`);
        if (!original) continue;
        const card = original.cloneNode(true);
        card.id = `pairconv-${number}`;
        const links = card.querySelector('.links');
        if (links) {
          links.querySelectorAll('a').forEach(a => { if (a.getAttribute('href')?.includes('/pairs/')) a.remove(); });
          const time = document.createElement('a');
          time.className = 'chip';
          time.href = `../conversations/round42.html#conv-${number}`;
          time.textContent = '🕰️ 時系列位置';
          links.appendChild(time);
        }
        const foot = card.querySelector('.cardfoot');
        if (foot) foot.innerHTML = `<a href="#pair-${id}">↑ このペアの先頭へ</a> ・ <a href="#top">↑ 一覧へ</a>`;
        group.appendChild(card);
      }
    }
    const target = location.hash && document.querySelector(location.hash);
    if (target) requestAnimationFrame(() => target.scrollIntoView());
  };

  const syncWorldIndex = () => {
    if (!/\/world\.html$/.test(location.pathname)) return;
    const heading = document.querySelector('#current-world .mini');
    if (heading) heading.textContent = '#379終了後に確認した最新world_stateと、現在の観察方針・現行の仕組みをまとめています。';

    const facts = new Map(Array.from(document.querySelectorAll('#status dt')).map(dt => [dt.textContent.trim(), dt.nextElementSibling]));
    if (facts.get('確認済み天候')) facts.get('確認済み天候').textContent = '2026-08-26・花曇り・11℃';
    if (facts.get('会話状態分類')) facts.get('会話状態分類').innerHTML = '<strong>継続2組 / 終了34組</strong>（43周目 #378〜#379終了後）。<a href="elysion_observation/conversation_status.md">36組の判定一覧</a>';
    if (facts.get('次の周回')) facts.get('次の周回').textContent = '43周目は#379まで完了。次に採番する場合は#380以降。';
    if (facts.get('events / pending')) facts.get('events / pending').textContent = 'raw world_state.events 50件（scene 49・moved 1） / pending 3件。観察累計scene world_eventは136件。最終pendingは「鐘楼から、新しい一日の始まりを告げる鐘の音が響き渡った。」「鐘楼の鐘が、新しい朝の訪れを告げる音を響かせた。」「鐘楼の鐘が、夕暮れを告げる穏やかな音を響かせた。」。';
    if (facts.get('#368終了時のaffinity')) {
      const dt = Array.from(document.querySelectorAll('#status dt')).find(x => x.textContent.includes('#368終了時のaffinity'));
      if (dt) dt.textContent = '#379終了時のaffinity';
      facts.get('#368終了時のaffinity').innerHTML = '完全rawから全36ペア・72方向の現在値を確認。継続2組は双方100 / 100。#375でIris↔Campanula=78/78、#376でMimosa↔Nerine=79/79、#377でErica↔Lupinus=100/100へ更新。<a href="elysion_affinity.md">好感度台帳</a>参照。';
    }
    if (facts.get('movements')) facts.get('movements').innerHTML = '<strong>8件</strong>。43周目の追加movementなし。';
    if (facts.get('turns_since_event')) facts.get('turns_since_event').textContent = '6（#379終了時）';

    const tbody = document.querySelector('#daily-summary tbody');
    if (tbody && !tbody.textContent.includes('2026-08-24')) {
      tbody.insertAdjacentHTML('beforeend', '<tr><td>2026-08-22</td><td>霧雨・7℃</td><td>本文完全原文は未保存</td><td>1件（#369）</td><td>+0（scene累計130）</td></tr><tr><td>2026-08-23</td><td>霧雨・23℃</td><td>本文完全原文は未保存</td><td>1件（#370）</td><td>+1（scene累計130→131）</td></tr><tr><td>2026-08-24</td><td>通り雨・30℃</td><td>本文完全原文は未保存</td><td>7件（#371〜#377）</td><td>+4（scene累計131→135）</td></tr>');
    }

    const eventsCard = document.getElementById('events');
    const pendingList = eventsCard?.querySelector('.eventlist');
    if (pendingList) pendingList.innerHTML = '<li><strong>鐘楼から、新しい一日の始まりを告げる鐘の音が響き渡った。</strong><br/>空高く響く銀の調べが、新しい物語の幕開けを告げるでしょう。<br/><small>created_at: 2026-08-24T06:48:08</small></li><li><strong>鐘楼の鐘が、新しい朝の訪れを告げる音を響かせた。</strong><br/>眠れる街の目覚めを告げる、清らかな響きが空を渡るでしょう。<br/><small>created_at: 2026-08-24T06:53:44</small></li><li><strong>鐘楼の鐘が、夕暮れを告げる穏やかな音を響かせた。</strong><br/>空の色が変わる頃、時を刻む音が街を優しく包み込むでしょう。<br/><small>created_at: 2026-08-26T08:49:05</small></li>';
    if (eventsCard && !document.getElementById('round43-world-link')) {
      eventsCard.insertAdjacentHTML('afterbegin', '<p id="round43-world-link" class="callout"><strong>43周目：</strong> #378〜#379のworld_event、events 50件ローリング、pending、location、turns_since_eventの詳細は <a href="world/round43.html">第43周の世界記録</a> に保存。</p>');
    }
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
    syncPairIndex();
    syncWorldIndex();
    await syncPairGroups();
    document.querySelectorAll('.record-filter[data-filter-scope]').forEach(setup);
  });
})();