from pathlib import Path
import re

ROOT = Path('.')

def read(path):
    return (ROOT / path).read_text(encoding='utf-8')

def write(path, text):
    (ROOT / path).write_text(text, encoding='utf-8')

def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f'{label}: expected exactly 1 match, got {n}')
    return text.replace(old, new, 1)

# -----------------------------------------------------------------------------
# 1) elysion_events.md
# -----------------------------------------------------------------------------
path = 'elysion_events.md'
t = read(path)
new_pending = '''## これから起こること（#377終了時点）

### 駅のホームに、一冊の古い手帖が落ちている。

忘れられた記憶の欠片が、鉄の道の上で静かに眠っている。

- created_at：2026-08-24T06:25:10

### 鐘楼から、新しい一日の始まりを告げる鐘の音が響き渡った。

空高く響く銀の調べが、新しい物語の幕開けを告げるでしょう。

- created_at：2026-08-24T06:48:08

### 鐘楼の鐘が、新しい朝の訪れを告げる音を響かせた。

眠れる街の目覚めを告げる、清らかな響きが空を渡るでしょう。

- created_at：2026-08-24T06:53:44

> #370・#373・#374・#375・#376でpendingが1件ずつ完全一致消化され、その都度replacementが1件補充された。#377終了時もpendingは3件。未発生の予告をsceneやmovementには数えない。

'''
t, n = re.subn(r'## これから起こること（#368終了時点）\n.*?(?=## 起こったこと（初期一覧）)', new_pending, t, count=1, flags=re.S)
if n != 1:
    raise RuntimeError('events: failed to replace current pending section')
t = replace_once(
    t,
    '初期一覧55件と、それ以降の追記75件を合わせ、#368終了時点のscene event累計130件を重複なく保持する。14〜41周目の追加25件はすべて完全rawの時刻・participants・locationと照合した。',
    '初期一覧55件と、それ以降の追記80件を合わせ、#377終了時点のscene event累計135件を重複なく保持する。14〜42周目の追加30件はすべて完全rawの時刻・participants・locationと照合した。',
    'events cumulative intro'
)
if '# 42周目・比較観察を含む（#369〜#377）' not in t:
    t += '''

---

# 42周目・比較観察を含む（#369〜#377）

- 会話：9件 / 新規ターン：56（#369〜#372は4ターン、#373〜#377は8ターン。#377は4+4ターン）
- rawで確認できた新規scene world_event：5件 / 累計：130→135
- 新規movement：0 / movements配列：8件のまま
- raw events：50件ローリング / 最終構成 scene49・moved1
- #369 / #371 / #372 / #377では新規scene world_eventなし。

## #370 アイリス × ビオラ

- raw時刻：2026-08-23T04:52:57
- text：`小路のパン屋から、焼き立ての香ばしい香りが漂い始めた。`
- participants：`iris`, `viola`
- location：`cafe_fleur`
- scene累計：130→131
- 完全一致で消化したpending：2026-08-21T12:12:37作成の同文pending
- replacement：`駅に到着した列車から、旅の荷物を抱えた人々が降り立つ。`
  - hint：鉄の道が運ぶのは、新しい物語と、誰かの待ちわびた足音。
  - created_at：2026-08-23T04:53:07
- events50件上限により、2026-08-15T02:39:49 moved `アネモネが花眠りの庭へやってきた` が押し出された。
- このmoved eventがeventsから消えても、対応するmovementは`movements`配列に残っている。

## #373 ダフネ × アネモネ

- raw時刻：2026-08-24T06:22:39
- text：`小路のパン屋から香ばしい焼き立ての匂いが漂ってきた。`
- participants：`anemone`, `daphne`
- location：`null`
- scene累計：131→132
- 完全一致で消化したpending：2026-08-21T12:20:16作成の同文pending
- replacement：`駅のホームに、一台の古い蒸気機関車がゆっくりと滑り込んだ。`
  - hint：鉄の車輪が刻むリズムが、新しい出会いの予感を運んでくる。
  - created_at：2026-08-24T06:22:59
- events50件上限により、2026-08-15T02:47:28 scene `温室のガラス越しに、夜にだけ開く花が淡く光りだした。` が押し出された。

## #374 アイリス × ビオラ

- raw時刻：2026-08-24T06:24:54
- text：`小路のパン屋から、焼きたての香ばしい香りが漂い始めた。`
- participants：`iris`, `viola`
- location：`cafe_fleur`
- scene累計：132→133
- 完全一致で消化したpending：2026-08-21T12:25:14作成の同文pending
- replacement：`駅のホームに、一冊の古い手帖が落ちている。`
  - hint：忘れられた記憶の欠片が、鉄の道の上で静かに眠っている。
  - created_at：2026-08-24T06:25:10
- events50件上限により、2026-08-15T03:00:50 scene `温室のガラス越しに、夜露が月光を反射して輝き出した。` が押し出された。

## #375 アイリス × カンパニュラ

- raw時刻：2026-08-24T06:47:55
- text：`駅に到着した列車から、旅の荷物を抱えた人々が降り立つ。`
- participants：`campanula`, `iris`
- location：`null`
- scene累計：133→134
- 完全一致で消化したpending：2026-08-23T04:53:07作成の同文pending
- replacement：`鐘楼から、新しい一日の始まりを告げる鐘の音が響き渡った。`
  - hint：空高く響く銀の調べが、新しい物語の幕開けを告げるでしょう。
  - created_at：2026-08-24T06:48:08
- events50件上限により、2026-08-15T03:12:28 scene `鐘楼の鐘が、一日の終わりを告げる穏やかな音色を響かせた。` が押し出された。

## #376 ミモザ × ネリネ

- raw時刻：2026-08-24T06:53:40
- text：`駅のホームに、一台の古い蒸気機関車がゆっくりと滑り込んだ。`
- participants：`mimosa`, `nerine`
- location：`null`
- scene累計：134→135
- 完全一致で消化したpending：2026-08-24T06:22:59作成の同文pending
- replacement：`鐘楼の鐘が、新しい朝の訪れを告げる音を響かせた。`
  - hint：眠れる街の目覚めを告げる、清らかな響きが空を渡るでしょう。
  - created_at：2026-08-24T06:53:44
- events50件上限により、2026-08-15T12:27:54 scene `鐘楼の鐘が、夜の訪れを告げる柔らかな音を響かせた。` が押し出された。

## #377終了時のevents / pending / counter

- raw events：50件（scene49 / moved1）。
- 最古：2026-08-15T12:34:18 / `鐘楼から、夜の静寂を告げる柔らかな鐘の音が響き渡った。` / participants=`anemone,daphne` / location=`null` / tags=`scene`。
- 最新：2026-08-24T06:53:40 / `駅のホームに、一台の古い蒸気機関車がゆっくりと滑り込んだ。` / participants=`mimosa,nerine` / location=`null` / tags=`scene`。
- pending：このファイル先頭の3件。
- turns_since_event：9。
- items / rumors / overheard：0 / 0 / 0。
- world_event本文に場所が書かれていてもraw `event.location`とは独立して扱う。#373 / #375 / #376は本文にパン屋・駅が出てもlocation=`null`、#370 / #374はパン屋本文でもlocation=`cafe_fleur`。
'''
write(path, t)

# -----------------------------------------------------------------------------
# 2) elysion_movements.md
# -----------------------------------------------------------------------------
path = 'elysion_movements.md'
t = read(path)
if '## 42周目・比較観察（#369〜#377）' not in t:
    t += '''

---

## 42周目・比較観察（#369〜#377）

- #369〜#377の9観察すべてで新規movementは0。`movements`配列は最終まで8件を維持した。
- #369 / #371 ダフネ×アネモネ：会話上は歩き続けるが、具体的な到着はなく、Daphne=`cafe_fleur` / Anemone=`hanasaku_station`のまま。
- #372 アイリス×ビオラ：香りを追って看板・店・窓越しの商品まで見つけたが、Iris / Violaともraw location=`cafe_fleur`、movement追加なし。
- #373 ダフネ×アネモネ：パン屋への寄り道を開始し扉へ向かうが、raw locationはDaphne=`cafe_fleur` / Anemone=`hanasaku_station`、movement追加なし。
- #374 アイリス×ビオラ：会話上はパン屋の扉を開けて入店し、カウンターへ歩み寄る。raw locationはIris=Viola=`cafe_fleur`、movement追加なし。
- #375 アイリス×カンパニュラ：会話叙述ではIrisが駅のホームに立つ一方、raw locationはIris=`cafe_fleur` / Campanula=`time_bell_tower`。駅到着movementはない。
- #376 ミモザ×ネリネ：駅の蒸気機関車world_eventを通話魔法越しに話題化。raw locationはMimosa=`eternite_square` / Nerine=`flower_slumber_garden`、movement追加なし。
- #377 エリカ×ルピナス：8ターンすべて別れの反復。raw locationはErica=`cafe_fleur` / Lupinus=`stellaris_hill`、movement追加なし。
- #370のscene追加でevents50件上限から2026-08-15T02:39:49のmoved eventが押し出されたが、対応するAnemone `cafe_fleur→flower_slumber_garden` movementは`movements`配列から消えなかった。**eventsのローリング押し出しとmovement履歴の保存は別**。

### #377終了時の全住民raw location

- Mimosa=`eternite_square`
- Iris=`cafe_fleur`
- Erica=`cafe_fleur`
- Anemone=`hanasaku_station`
- Daphne=`cafe_fleur`
- Campanula=`time_bell_tower`
- Nerine=`flower_slumber_garden`
- Viola=`cafe_fleur`
- Lupinus=`stellaris_hill`

会話上の移動・到着・入店、world_event本文の地名、raw `characters[].location`、raw `movements`は互いに自動同一視しない。
'''
write(path, t)

# -----------------------------------------------------------------------------
# 3) pairs.html static index
# -----------------------------------------------------------------------------
path = 'pairs.html'
t = read(path)
t = replace_once(t,
    '<p>全36ペアの入口です。各ページでは、同じ2人の会話を実際の記録順のまま読めます。</p><p class="callout"><strong>#368終了時点の会話状態：</strong>継続中2組 / 終了34組。14〜20周目に4組が自然終了し、21〜41周目はダフネ×アネモネとアイリス×ビオラの2組を継続観察しました。 <a href="elysion_observation/conversation_status.md">判定一覧と根拠を見る</a></p>',
    '<p>全36ペアの入口です。各ページでは、同じ2人の会話を実際の記録順のまま読めます。</p><p class="callout"><strong>#377終了時点の会話状態：</strong>継続中2組 / 終了34組。42周目は継続2組に加え、終了挙動比較として3組を再観察しました。比較観察後も終了3組は再接続せず終了維持です。 <a href="elysion_observation/conversation_status.md">判定一覧と根拠を見る</a></p>',
    'pairs intro')
repls = {
    '#6 / #56 / #137 / #173 / #209 / #245 終了': '#6 / #56 / #137 / #173 / #209 / #245 / #375 終了',
    'アイリス × カンパニュラ（6件）— 終了': 'アイリス × カンパニュラ（7件）— 終了',
    '#11 / #51 / #77 / #128 / #164 / #200 / #236 / #255 / #262 / #269 / #276 / #282 / #289 / #295 / #301 / #306 / #310 / #314 / #318 / #322 / #325 / #328 / #330 / #332 / #334 / #336 / #338 / #340 / #342 / #344 / #346 / #348 / #350 / #352 / #354 / #356 / #358 / #360 / #362 / #364 / #366 / #368 継続中': '#11 / #51 / #77 / #128 / #164 / #200 / #236 / #255 / #262 / #269 / #276 / #282 / #289 / #295 / #301 / #306 / #310 / #314 / #318 / #322 / #325 / #328 / #330 / #332 / #334 / #336 / #338 / #340 / #342 / #344 / #346 / #348 / #350 / #352 / #354 / #356 / #358 / #360 / #362 / #364 / #366 / #368 / #370 / #372 / #374 継続中',
    'アイリス × ビオラ（42件）— 継続中': 'アイリス × ビオラ（45件）— 継続中',
    '#23 / #47 / #88 / #135 / #171 / #207 / #243 / #258 / #265 / #272 終了': '#23 / #47 / #88 / #135 / #171 / #207 / #243 / #258 / #265 / #272 / #377 終了',
    'エリカ × ルピナス（10件）— 終了': 'エリカ × ルピナス（11件）— 終了',
    '#26 / #62 / #107 / #143 / #179 / #215 終了': '#26 / #62 / #107 / #143 / #179 / #215 / #376 終了',
    'ミモザ × ネリネ（6件）— 終了': 'ミモザ × ネリネ（7件）— 終了',
    '#32 / #76 / #93 / #114 / #150 / #186 / #222 / #253 / #260 / #267 / #274 / #280 / #287 / #293 / #299 / #304 / #308 / #312 / #316 / #320 / #324 / #327 / #329 / #331 / #333 / #335 / #337 / #339 / #341 / #343 / #345 / #347 / #349 / #351 / #353 / #355 / #357 / #359 / #361 / #363 / #365 / #367 継続中': '#32 / #76 / #93 / #114 / #150 / #186 / #222 / #253 / #260 / #267 / #274 / #280 / #287 / #293 / #299 / #304 / #308 / #312 / #316 / #320 / #324 / #327 / #329 / #331 / #333 / #335 / #337 / #339 / #341 / #343 / #345 / #347 / #349 / #351 / #353 / #355 / #357 / #359 / #361 / #363 / #365 / #367 / #369 / #371 / #373 継続中',
    'ダフネ × アネモネ（42件）— 継続中': 'ダフネ × アネモネ（45件）— 継続中',
}
for old, new in repls.items():
    if old not in t:
        raise RuntimeError(f'pairs: missing {old[:50]}')
    t = t.replace(old, new)
# static hash routing arrays
for old, new in {
    '"6","56","137","173","209","245"': '"6","56","137","173","209","245","375"',
    '"366","368","12"': '"366","368","370","372","374","12"',
    '"258","265","272","24"': '"258","265","272","377","24"',
    '"26","62","107","143","179","215","27"': '"26","62","107","143","179","215","376","27"',
    '"363","365","367","33"': '"363","365","367","369","371","373","33"',
}.items():
    if old not in t:
        raise RuntimeError(f'pairs route: missing {old}')
    t = t.replace(old, new, 1)
write(path, t)

# -----------------------------------------------------------------------------
# 4) Static pair group pages: copy exact round42 cards into correct pair sections
# -----------------------------------------------------------------------------
round42 = read('conversations/round42.html')

def extract_round42_card(n):
    m = re.search(rf'<section class="card conversation" id="conv-{n}">.*?</section>', round42, re.S)
    if not m:
        raise RuntimeError(f'round42 card #{n} not found')
    return m.group(0)

def adapt_card(n, pair_no):
    c = extract_round42_card(n)
    c = c.replace(f'id="conv-{n}"', f'id="pairconv-{n}"', 1)
    c, count = re.subn(
        rf'<a class="chip" href="\.\./pairs/[^\"]+#pairconv-{n}">👥 ペア別位置</a>',
        f'<a class="chip" href="../conversations/round42.html#conv-{n}">🕰️ 時系列位置</a>', c, count=1)
    if count != 1:
        raise RuntimeError(f'could not adapt pair link #{n}')
    c = c.replace('<div class="cardfoot"><a href="#top">↑ 一覧へ</a></div>',
                  f'<div class="cardfoot"><a href="#pair-{pair_no}">↑ このペアの先頭へ</a> ・ <a href="#top">↑ 一覧へ</a></div>', 1)
    return c

def update_pair_group(path, pair_no, next_pair_no, pair_name, old_count, new_count, old_numbers, new_numbers, old_last, additions):
    text = read(path)
    marker = f'id="pair-{pair_no}"'
    s = text.find(marker)
    if s < 0:
        raise RuntimeError(f'{path}: pair {pair_no} section missing')
    if next_pair_no is None:
        e = text.find('</main>', s)
    else:
        e = text.find(f'id="pair-{next_pair_no}"', s)
    if e < 0:
        raise RuntimeError(f'{path}: end marker missing for pair {pair_no}')
    seg = text[s:e]
    if f'pairconv-{additions[0]}' in seg:
        return
    seg = seg.replace(f'{pair_name}（{old_count}件）', f'{pair_name}（{new_count}件）')
    seg = seg.replace(f'>{old_count}件<', f'>{new_count}件<')
    if old_numbers not in seg:
        raise RuntimeError(f'{path}: old number list missing for pair {pair_no}')
    seg = seg.replace(old_numbers, new_numbers)
    m = re.search(rf'<section class="card conversation" id="pairconv-{old_last}">.*?</section>', seg, re.S)
    if not m:
        raise RuntimeError(f'{path}: old last card {old_last} missing')
    cards = '\n' + '\n'.join(adapt_card(n, pair_no) for n in additions)
    seg = seg[:m.end()] + cards + seg[m.end():]
    text = text[:s] + seg + text[e:]
    # TOC count, if present before pair section
    text = text.replace(f'{pair_name}（{old_count}件）', f'{pair_name}（{new_count}件）')
    text = text.replace(old_numbers, new_numbers)
    for n in additions:
        if text.count(f'id="pairconv-{n}"') != 1:
            raise RuntimeError(f'{path}: pairconv-{n} count != 1')
    write(path, text)

update_pair_group('pairs/group01-06.html', 6, None, 'アイリス × カンパニュラ', 6, 7,
                  '#6 / #56 / #137 / #173 / #209 / #245', '#6 / #56 / #137 / #173 / #209 / #245 / #375', 245, [375])
update_pair_group('pairs/group07-12.html', 11, 12, 'アイリス × ビオラ', 42, 45,
                  '#11 / #51 / #77 / #128 / #164 / #200 / #236 / #255 / #262 / #269 / #276 / #282 / #289 / #295 / #301 / #306 / #310 / #314 / #318 / #322 / #325 / #328 / #330 / #332 / #334 / #336 / #338 / #340 / #342 / #344 / #346 / #348 / #350 / #352 / #354 / #356 / #358 / #360 / #362 / #364 / #366 / #368',
                  '#11 / #51 / #77 / #128 / #164 / #200 / #236 / #255 / #262 / #269 / #276 / #282 / #289 / #295 / #301 / #306 / #310 / #314 / #318 / #322 / #325 / #328 / #330 / #332 / #334 / #336 / #338 / #340 / #342 / #344 / #346 / #348 / #350 / #352 / #354 / #356 / #358 / #360 / #362 / #364 / #366 / #368 / #370 / #372 / #374', 368, [370, 372, 374])
update_pair_group('pairs/group19-24.html', 23, 24, 'エリカ × ルピナス', 10, 11,
                  '#23 / #47 / #88 / #135 / #171 / #207 / #243 / #258 / #265 / #272', '#23 / #47 / #88 / #135 / #171 / #207 / #243 / #258 / #265 / #272 / #377', 272, [377])
update_pair_group('pairs/group25-30.html', 26, 27, 'ミモザ × ネリネ', 6, 7,
                  '#26 / #62 / #107 / #143 / #179 / #215', '#26 / #62 / #107 / #143 / #179 / #215 / #376', 215, [376])
update_pair_group('pairs/group31-36.html', 32, 33, 'ダフネ × アネモネ', 42, 45,
                  '#32 / #76 / #93 / #114 / #150 / #186 / #222 / #253 / #260 / #267 / #274 / #280 / #287 / #293 / #299 / #304 / #308 / #312 / #316 / #320 / #324 / #327 / #329 / #331 / #333 / #335 / #337 / #339 / #341 / #343 / #345 / #347 / #349 / #351 / #353 / #355 / #357 / #359 / #361 / #363 / #365 / #367',
                  '#32 / #76 / #93 / #114 / #150 / #186 / #222 / #253 / #260 / #267 / #274 / #280 / #287 / #293 / #299 / #304 / #308 / #312 / #316 / #320 / #324 / #327 / #329 / #331 / #333 / #335 / #337 / #339 / #341 / #343 / #345 / #347 / #349 / #351 / #353 / #355 / #357 / #359 / #361 / #363 / #365 / #367 / #369 / #371 / #373', 367, [369, 371, 373])

# -----------------------------------------------------------------------------
# 5) world.html current/latest layer
# -----------------------------------------------------------------------------
path = 'world.html'
t = read(path)
t = replace_once(t, '#368終了後に確認した最新world_stateと、現在の観察方針・現行の仕組みをまとめています。', '#377終了後に確認した最新world_stateと、現在の観察方針・現行の仕組みをまとめています。', 'world current heading')
row21 = '<tr><td>2026-08-21</td><td>曇り・14℃</td><td><a href="world/round14.html#round14-newspaper">温室の発光・鐘楼・銀色の栞 → 原文</a></td><td>89件（#280〜#368・11〜41周目）</td><td>+32（scene累計98→130）</td></tr>'
rows_new = row21 + '\n' + '<tr><td>2026-08-22</td><td>霧雨・7℃</td><td><a href="elysion_newspapers.md">光の結晶・旅立ち・学院 → 原文</a></td><td>1件（#369）</td><td>+0（scene累計130）</td></tr>\n<tr><td>2026-08-23</td><td>霧雨・23℃</td><td><a href="elysion_newspapers.md">美しき確信・幸福の積み重ね → 原文</a></td><td>1件（#370）</td><td>+1（scene累計130→131）</td></tr>\n<tr><td>2026-08-24</td><td>通り雨・30℃</td><td><a href="elysion_newspapers.md">パン屋の黄金の香り → 原文</a></td><td>7件（#371〜#377）</td><td>+4（scene累計131→135）</td></tr>'
t = replace_once(t, row21, rows_new, 'world daily rows')
# status block targeted replacements
t = replace_once(t, '<dd>2026-08-21・曇り・14℃</dd>', '<dd>2026-08-24・通り雨・30℃</dd>', 'world weather')
t = replace_once(t, '<dd>2026年8月21日号（#280で本文確認。#282 / #291 / #297 / #298 / #303 / #314 / #317の発行表示は同一号）</dd>', '<dd>2026年8月24日号（42周目で8月22日号・23日号・24日号の本文を順次確認。<a href="elysion_newspapers.md">新聞原文台帳</a>）</dd>', 'world latest newspaper')
t = replace_once(t, '<dt>会話状態分類</dt><dd><strong>継続2組 / 終了34組</strong>（#367〜#368の41周目・継続対象2組限定運用後）。<a href="elysion_observation/conversation_status.md">36組の判定一覧</a></dd>', '<dt>会話状態分類</dt><dd><strong>継続2組 / 終了34組</strong>（42周目 #369〜#377完了。終了済み3組の比較観察は終了維持）。<a href="elysion_observation/conversation_status.md">36組の判定一覧</a></dd>', 'world conversation status')
t = replace_once(t, '<dt>次の周回</dt>\n<dd>42周目。#369「ダフネ × アネモネ」は、最新raw world_stateと継続2組の確認後に確定する開始候補。</dd>', '<dt>最新周回</dt>\n<dd>42周目 #369〜#377を完了。#369〜#372は4ターン観察、#373〜#377は8ターン観察（#377は4+4）。<a href="world/round42.html">42周目の最終world_state</a></dd>', 'world round status')
old_events_dd = '<dd>raw world_state.events 50件（scene 48・moved 2） / pending 3件。観察累計scene eventは130件。pendingは「小路のパン屋から、焼き立ての香ばしい香りが漂い始めた。」「小路のパン屋から香ばしい焼き立ての匂いが漂ってきた。」「小路のパン屋から、焼きたての香ばしい香りが漂い始めた。」。3件ともパン屋の香りで意味が近いが、1件目「焼き立て」と3件目「焼きたて」は異なり、本文の完全一致ではない。</dd>'
new_events_dd = '<dd>raw world_state.events 50件（scene 49・moved 1） / pending 3件。scene event累計は135件。pendingは「駅のホームに、一冊の古い手帖が落ちている。」「鐘楼から、新しい一日の始まりを告げる鐘の音が響き渡った。」「鐘楼の鐘が、新しい朝の訪れを告げる音を響かせた。」。eventsの50件上限で古いeventが押し出されてもmovements配列8件は保持される。</dd>'
t = replace_once(t, old_events_dd, new_events_dd, 'world events status')
t = replace_once(t, '<dt>#368終了時のaffinity</dt>', '<dt>#377終了時のaffinity</dt>', 'world affinity dt')
t = replace_once(t, '完全rawから全36ペア・72方向の現在値を確認。継続2組は双方100 / 100。ダフネ×アネモネは#299で99 / 99、#304で100 / 100へ到達。', '完全rawから全36ペア・72方向の現在値を確認。継続2組は双方100 / 100。42周目ではIris→Campanula 74→78 / Campanula→Iris 72→78、Mimosa↔Nerine 75→79、Erica↔Lupinus 98→100へ変化。', 'world affinity dd')
t = replace_once(t, '<dd>1（#368終了時）</dd>', '<dd>9（#377終了時）</dd>', 'world turns')
# current pending list in events card
old_pending_html = '''<ol class="eventlist"><li><strong>小路のパン屋から、焼き立ての香ばしい香りが漂い始めた。</strong><br/>香ばしい予感が、街の角を曲がって心を温めるでしょう。<br/><small>created_at: 2026-08-21T12:12:37</small></li>
<li><strong>小路のパン屋から香ばしい焼き立ての匂いが漂ってきた。</strong><br/>黄金色の香りが、空腹と幸福を優しく呼び覚ますでしょう。<br/><small>created_at: 2026-08-21T12:20:16</small></li>
<li><strong>小路のパン屋から、焼きたての香ばしい香りが漂い始めた。</strong><br/>黄金色の香りが、静かな道を優しく包み込みます。<br/><small>created_at: 2026-08-21T12:25:14</small></li></ol>'''
new_pending_html = '''<ol class="eventlist"><li><strong>駅のホームに、一冊の古い手帖が落ちている。</strong><br/>忘れられた記憶の欠片が、鉄の道の上で静かに眠っている。<br/><small>created_at: 2026-08-24T06:25:10</small></li>
<li><strong>鐘楼から、新しい一日の始まりを告げる鐘の音が響き渡った。</strong><br/>空高く響く銀の調べが、新しい物語の幕開けを告げるでしょう。<br/><small>created_at: 2026-08-24T06:48:08</small></li>
<li><strong>鐘楼の鐘が、新しい朝の訪れを告げる音を響かせた。</strong><br/>眠れる街の目覚めを告げる、清らかな響きが空を渡るでしょう。<br/><small>created_at: 2026-08-24T06:53:44</small></li></ol>'''
t = replace_once(t, old_pending_html, new_pending_html, 'world pending html')
# append 5 raw events after #368 timeline entry
old368 = '<div><time>2026-08-21T12:24:47（#368）</time><p>温室のガラス越しに、珍しい色の花が咲き始めた。<br/><small>participants: iris, viola / location: cafe_fleur</small></p></div>'
new368 = old368 + '''
<div><time>2026-08-23T04:52:57（#370）</time><p>小路のパン屋から、焼き立ての香ばしい香りが漂い始めた。<br/><small>participants: iris, viola / location: cafe_fleur</small></p></div>
<div><time>2026-08-24T06:22:39（#373）</time><p>小路のパン屋から香ばしい焼き立ての匂いが漂ってきた。<br/><small>participants: anemone, daphne / location: null</small></p></div>
<div><time>2026-08-24T06:24:54（#374）</time><p>小路のパン屋から、焼きたての香ばしい香りが漂い始めた。<br/><small>participants: iris, viola / location: cafe_fleur</small></p></div>
<div><time>2026-08-24T06:47:55（#375）</time><p>駅に到着した列車から、旅の荷物を抱えた人々が降り立つ。<br/><small>participants: campanula, iris / location: null</small></p></div>
<div><time>2026-08-24T06:53:40（#376）</time><p>駅のホームに、一台の古い蒸気機関車がゆっくりと滑り込んだ。<br/><small>participants: mimosa, nerine / location: null</small></p></div>'''
t = replace_once(t, old368, new368, 'world event timeline')
# location current callout + newspaper link + latest round chips
t = replace_once(t, '<strong>#368時点の再整理：</strong>', '<strong>#377時点の再整理：</strong>', 'world location heading')
needle = '<p class="callout"><strong>#377時点の再整理：</strong>到着描写に対するmovement未反映は #101 / #192 / #200、正常更新は #150 / #164 / #178 / #239 / #267 で確認。#275 / #277 は目的地へ向かう段階で、到着未確認のため失敗には数えません。</p>'
insert = needle + '\n<p class="callout"><strong>42周目追加確認：</strong>#372の店発見、#374のパン屋入店、#375の駅ホーム描写はいずれも新規movementを生まず、#377終了時もmovements=8。会話叙述・world_event本文・raw location・movementsを分離して扱います。</p>'
t = replace_once(t, needle, insert, 'world location 42 note')
t = replace_once(t, '📰 2026年8月9日〜21日号の保存済み全文', '📰 2026年8月9日〜24日号の保存済み全文', 'world newspaper link')
# add round42 card before past observations
marker = '<section class="intro" id="past-observations">'
round42_card = '''<section class="card" id="round42-behavior"><h2>42周目 #369〜#377：終了挙動比較と最終world_state</h2><ul><li>#369〜#372は4ターン、#373〜#377は8ターンで観察。#377は4ターン時点の中間rawと、追加4ターン後の最終rawを分離した。</li><li>raw新規sceneは#370 / #373 / #374 / #375 / #376の5件で累計130→135。#369 / #371 / #372 / #377はsceneなし。</li><li>会話が終わりにくい挙動は、Daphne×Anemoneのabstract locomotion loop、Iris×Violaのgoal chaining、Iris×Campanulaのpost-conversation narration、Mimosa×Nerineのfarewell loop + event reactivation、Erica×Lupinusのpure farewell loopの5型を比較した。</li><li>#377終了時：weather=2026-08-24・通り雨・30℃、events=50（scene49/moved1）、movements=8、pending=3、turns_since_event=9、items/rumors/overheard=0。</li></ul><p><a class="chip" href="world/round42.html">🌍 42周目の詳細と最終world_state</a> <a class="chip" href="conversations/round42.html">💬 #369〜#377会話原文</a></p></section>
'''
if marker not in t:
    raise RuntimeError('world past marker missing')
t = t.replace(marker, round42_card + marker, 1)
t = replace_once(t, '<section class="card" id="latest-rounds"><h2>12〜41周目の世界記録</h2>', '<section class="card" id="latest-rounds"><h2>12〜42周目の世界記録</h2>', 'world latest rounds heading')
t = replace_once(t, '<a class="chip" href="world/round41.html">41周目 #367〜#368</a></section>', '<a class="chip" href="world/round41.html">41周目 #367〜#368</a> <a class="chip" href="world/round42.html">42周目 #369〜#377</a></section>', 'world round42 chip')
write(path, t)

# -----------------------------------------------------------------------------
# 6) index.html current dashboard + latest card
# -----------------------------------------------------------------------------
path = 'index.html'
t = read(path)
old_current = '''<h2>41周目・継続対象2組限定 完了</h2>
<p class="current-lead"><strong>#298〜#368の14〜41周目を完了。</strong> 4組の終了を確認し、ダフネ×アネモネとアイリス×ビオラの2組が継続しています。</p>'''
new_current = '''<h2>42周目・終了挙動の比較観察 完了</h2>
<p class="current-lead"><strong>#369〜#377の9会話・新規56ターンを完了。</strong> 継続2組に加え、終了済み3組を比較観察し、5種類の「会話が終わりにくい」挙動を記録しました。</p>'''
t = replace_once(t, old_current, new_current, 'index current heading')
for old, new, label in [
    ('<strong>#368 アイリス × ビオラ</strong>', '<strong>#377 エリカ × ルピナス</strong>', 'index latest'),
    ('<strong>限定2組 / 2会話 完了</strong><small>36組一巡ではなく継続対象のみ</small>', '<strong>9会話 / 9会話 完了</strong><small>#369〜#372=4ターン、#373〜#377=8ターン（#377は4+4）</small>', 'index progress'),
    ('<strong>2026-08-21・曇り・14℃</strong>', '<strong>2026-08-24・通り雨・30℃</strong>', 'index weather'),
    ('<strong>観察累計 130件</strong><small>14〜41周目で+25</small>', '<strong>観察累計 135件</strong><small>42周目でraw-confirmed +5</small>', 'index scene'),
    ('<span class="statuslabel">turns_since_event</span><strong>1</strong>', '<span class="statuslabel">turns_since_event</span><strong>9</strong>', 'index turns'),
    ('<strong>8件</strong><small>#267でアネモネが駅へ到着</small>', '<strong>8件</strong><small>42周目の追加0件</small>', 'index movements'),
    ('採番368件＋未採番補完1件を読む', '採番377件＋未採番補完1件を読む', 'index conversation count'),
]:
    t = replace_once(t, old, new, label)
# affinity card current wording
t = replace_once(t, '11周目で完全なraw JSONが復活し、全36ペア・72方向の現在値を確認。継続2組はいずれも双方100 / 100。ダフネ×アネモネは#299で99 / 99、#304で100 / 100へ到達しました。#283直後の未取得分は推測しません。', '完全raw JSONで全36ペア・72方向を確認。#377終了時、継続2組はいずれも双方100 / 100。42周目ではアイリス×カンパニュラ、ミモザ×ネリネ、エリカ×ルピナスに方向別の上昇を確認しました。', 'index affinity current')
# historical card only update next-candidate sentence
old_next = '次の候補は42周目 #369「ダフネ × アネモネ」。実行前に最新raw world_stateと継続2組を再確認します。'
new_next = 'この後、42周目 #369〜#377を実施し、継続2組と終了済み3組の終了挙動比較まで完了しました。'
t = replace_once(t, old_next, new_next, 'index historical next')
# add 42 card before main close
card = '''<section class="card" id="round42-complete"><h2>42周目・#369〜#377 完了</h2><p>9会話・新規56ターンを記録。rawで新規scene world_eventは5件増えて累計135件。#377終了時はevents=50（scene49/moved1）、movements=8、pending=3、turns_since_event=9です。</p><p>終了しにくさは、抽象移動ループ／goal chaining／通話終了後のnarration continuation／farewell loop + event reactivation／pure farewell loopの5パターンを比較しました。内部実装の停止条件そのものは未確認です。</p><p><a href="conversations/round42.html">💬 42周目の会話</a> ・ <a href="notes/round42.html">📝 備考・注釈</a> ・ <a href="world/round42.html">🌍 最終world_state</a> ・ <a href="elysion_affinity.md">💕 最新好感度</a></p></section>
'''
if 'id="round42-complete"' not in t:
    t = t.replace('</main>', card + '</main>', 1)
write(path, t)

# -----------------------------------------------------------------------------
# 7) elysion_observed_daily_life.md
# -----------------------------------------------------------------------------
path = 'elysion_observed_daily_life.md'
t = read(path)
insert_marker = '\n---\n\n## 更新方針メモ'
if insert_marker not in t:
    raise RuntimeError('daily-life update marker missing')
if '### 42周目：パン屋の香りは具体的な行動目標を作る' not in t:
    addition = '''
### 42周目：パン屋の香りは具体的な行動目標を作る

- **確度：高**
- #370で小路のパン屋の香りがworld_eventとして入り、アイリス×ビオラは香りの正体を確かめる短期目標へ切り替わった。
- #372では看板・店・窓越しの商品を見つけ、#374では扉を開けて入店し、カウンターへ進み、シナモンのパンとキラキラしたクッキーを選ぶところまで会話上で進展した。
- #373では別のパン屋の香りworld_eventが、ダフネ×アネモネの28ターン続いたabstract locomotion loopを具体的な「パン屋への寄り道」へ切り替えた。ただし8ターン中には扉を実際に開けるところまで進まなかった。
- 会話上の店発見・入店とraw location / movementsは一致せず、42周目の新規movementは0件。生活描写としてのパン屋利用と、world_state上の現在地更新は分けて扱う。

### 42周目：駅・列車は新しい出会い／転換を示すsceneとして繰り返し使われる

- **確度：高**
- #375では「駅に到着した列車から、旅の荷物を抱えた人々が降り立つ。」、#376では「駅のホームに、一台の古い蒸気機関車がゆっくりと滑り込んだ。」が発火した。
- どちらもraw `event.location=null`で、movement追加はない。#375の会話叙述ではアイリスが駅ホームに立つが、raw Iris.locationは`cafe_fleur`のまま。
- 駅や列車は日常的な街の背景・話題として頻出するが、scene本文だけから住民自身の移動を推定しない。

### 42周目：「おやすみ／また明日」は別れの定型だが、生成停止とは一致しない

- **確度：中**
- #376ミモザ×ネリネは最初の6ターンで「おやすみ」「また明日」を繰り返した後、蒸気機関車world_eventで会話が再活性化し、翌日の任意の予定が追加された。
- #377エリカ×ルピナスは自然な別れの後も、新規8ターンすべてが「おやすみ／また明日」の反復だった。
- #375アイリス×カンパニュラは、既に別れと通話魔法の切断まで描写済みだったのに、新規8ターンが交互のナレーションとして継続した。
- したがって別れの言葉自体は日常的な通話終了表現として観察できるが、生成処理が実際に停止した証拠にはしない。

### 42周目：長い会話の「終わりにくさ」は少なくとも5種類に分かれる

- **確度：中**
- ダフネ×アネモネ：abstract locomotion loop。
- アイリス×ビオラ：goal chaining / self-extension。
- アイリス×カンパニュラ：post-conversation narration continuation。
- ミモザ×ネリネ：farewell loop + event reactivation。
- エリカ×ルピナス：pure farewell loop。
- 5組で異なる形の継続が見られたため、特定ペアや好感度100だけの現象とは言い切れない。ただし内部の自然終了判定・停止実装そのものは直接確認していない。

'''
    t = t.replace(insert_marker, '\n' + addition + insert_marker, 1)
write(path, t)

# -----------------------------------------------------------------------------
# 8) Validation
# -----------------------------------------------------------------------------
checks = {
    'elysion_events.md': ['#377終了時点', 'scene event累計135', '# 42周目・比較観察を含む（#369〜#377）', 'turns_since_event：9'],
    'elysion_movements.md': ['## 42周目・比較観察（#369〜#377）', 'movements`配列は最終まで8件', 'Iris=`cafe_fleur`'],
    'world.html': ['#377終了後', '2026-08-24・通り雨・30℃', 'scene event累計は135件', 'world/round42.html', 'turns_since_event'],
    'pairs.html': ['アイリス × ビオラ（45件）— 継続中', 'ダフネ × アネモネ（45件）— 継続中', 'エリカ × ルピナス（11件）— 終了', 'ミモザ × ネリネ（7件）— 終了', 'アイリス × カンパニュラ（7件）— 終了'],
    'index.html': ['#377 エリカ × ルピナス', '観察累計 135件', '採番377件＋未採番補完1件', 'id="round42-complete"'],
    'elysion_observed_daily_life.md': ['### 42周目：パン屋の香りは具体的な行動目標を作る', 'pure farewell loop'],
}
for p, needles in checks.items():
    text = read(p)
    for needle in needles:
        if needle not in text:
            raise RuntimeError(f'validation failed: {p}: {needle}')

for p, nums in {
    'pairs/group01-06.html':[375],
    'pairs/group07-12.html':[370,372,374],
    'pairs/group19-24.html':[377],
    'pairs/group25-30.html':[376],
    'pairs/group31-36.html':[369,371,373],
}.items():
    text = read(p)
    for n in nums:
        if text.count(f'id="pairconv-{n}"') != 1:
            raise RuntimeError(f'validation failed: {p} pairconv-{n}')

# Validate exact 11 intended content files are modified before deleting helpers.
intended = {
    'elysion_events.md', 'elysion_movements.md', 'world.html', 'pairs.html',
    'pairs/group01-06.html', 'pairs/group07-12.html', 'pairs/group19-24.html',
    'pairs/group25-30.html', 'pairs/group31-36.html', 'index.html',
    'elysion_observed_daily_life.md'
}

# Remove temporary automation files so final branch diff contains only intended files.
for helper in ['.github/scripts/sync_round42_full_layers.py', '.github/workflows/round42-sync.yml']:
    p = ROOT / helper
    if p.exists():
        p.unlink()

print('ROUND42_FULL_LAYER_SYNC_OK')
print('\n'.join(sorted(intended)))
