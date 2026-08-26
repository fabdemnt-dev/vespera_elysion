from pathlib import Path
import re, html
from bs4 import BeautifulSoup

ROOT = Path('.')

def read(path):
    return (ROOT / path).read_text(encoding='utf-8')

def write(path, text):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding='utf-8')

def replace_once(text, old, new, label):
    if old not in text:
        raise RuntimeError(f'anchor not found for {label}: {old[:120]}')
    return text.replace(old, new, 1)

def append_if_missing(path, marker, block):
    text = read(path)
    if marker not in text:
        if not text.endswith('\n'):
            text += '\n'
        text += '\n' + block.strip() + '\n'
        write(path, text)

def para(s):
    return html.escape(s).replace('\n', '<br/>')

# -------------------------
# Round 43 source records
# -------------------------
r378 = [
('Daphne', '''ええ、準備はできているわ。 「美味しいね」って笑い合えるその瞬間を、一番の宝物にしながら。  さあ、行きましょう！ 香ばしくて温かな、幸せの扉を、二人でいっぱいに開けて……。  私たちの、幸せな寄り道のスタートよ！！'''),
('Anemone', '''うん、行こう！！ 扉を開ける瞬間の、あのワクワクを大切に……。  さあ、幸せの扉を、一緒に開けようね、ダフネ！！'''),
('Daphne', '''ええ、一緒に。 扉を開けるその瞬間の、指先に伝わる高揚感さえも、大切に抱きしめて。  さあ、アネモネ。 二人で、幸せの扉を開けましょう！'''),
('Anemone', '''うん、一緒に！ 指先から伝わるあのドキドキも、全部私たちの物語の一部だもんね。  せーの……って感じで、一緒に開けよう！  さあ、幸せの扉、オープン！！'''),
('Daphne', '''せーの……！  （カランコロン、と軽やかなベルの音が響き、温かい小麦の香りがふわりと二人を包み込む）  ……わぁ、なんて素敵な香りかしら。 扉を開けた瞬間、まるで魔法にかかったみたいに、幸せな匂いが溢れ出してきたわね。  見て、アネモネ。 棚には、色とりどりの、とっても美味しそうなパンが並んでいるわ。 私たちの「幸せな寄り道」が、ここから始まるのね。''' ),
('Anemone', '''わぁ……！本当だ、すごい……！ 扉を開けた瞬間に、ふわぁって幸せな香りが押し寄せてきて、なんだか胸がいっぱいになっちゃった。  見て、ダフネ！ あっちにはキラキラした砂糖がのったパンがあるし、こっちにはこんがり焼けた香ばしそうなパンも……！ 本当に魔法みたい。まるで宝石箱をひっくり返したみたいに、美味しそうなものが並んでるよ！  ふふ、どれから選ぼうかな？ 私たちの「幸せな寄り道」、最高のスタートだね！'''),
('Daphne', '''本当に、まるで宝石箱みたい……。 キラキラした砂糖が星のように散りばめられたパンや、こんがりと黄金色に焼けた、香ばしさの塊のようなパン……。  見ているだけで、心が弾んで、なんだか魔法にかかったみたいに夢心地になってしまうわ。 どれもこれも、とっても美味しそうで、選ぶのが難しくなってしまうわね。  ふふ、アネモネ。 あなたのその、キラキラした瞳が一番の魔法かもしれないわ。 さあ、どれにしましょうか？ 私たちの新しい物語にふさわしい、特別な「美味しい」を、一緒に見つけましょう。''' ),
('Anemone', '''あはは、私の瞳が魔法だなんて、ダフネったら……！ でも、そう言ってもらえると、なんだか本当に魔法使いになったみたいな気分になっちゃうな。  うーん、迷っちゃうね！ あっちの、太陽の光を閉じ込めたみたいに黄金色に輝いてるパンも気になるし、こっちの、まるで夜空の星をちりばめたような甘いパンも捨てがたいよ……。  ねぇ、ダフネ。 もしよかったら、今の私たちの気持ちにぴったりなものを、一緒に選んでみない？ 「これだ！」って直感で感じたもの、それがきっと、今の私たちに一番必要な「特別な美味しい」だと思うんだ。''' )
]

r379 = [
('Iris', '''（ビオラに手を握り返されて、私の心はもう、シナモンの甘い香りと幸せな予感でいっぱいだよ！）  うん！さあ、注文しちゃおう！ ビオラと一緒に食べる「最初の一口」が、どんな魔法を連れてきてくれるのか……今からワクワクが止まらないよ！  （お店の方に向かって、精一杯の明るい笑顔を作って、元気よく声をかけるよ）  「ごきげんよう！あの、焼き立てのシナモンパンを一つと、それから……あっちのキラキラしたクッキーもお願いできますか？」  （注文を終えて、少しだけ照れくさそうに、でもとっても嬉しそうにビオラを見上げるよ）  ふふ、これで準備万端だね！ ねぇ、ビオラ……。 お菓子が出来上がるまでの間、あのお店の窓から見える景色を、二人でゆっくり眺めて待ってようよ！'''),
('EVENT', '―― 駅のホームに、一冊の古い手帖が落ちている。 ――'),
('Viola', '''（アイリスの明るい注文に、ビオラも優しく微笑みながら、お店の方へ丁寧にお辞儀をします）  「ごきげんよう。……はい、お願いしますね。」  （注文を終えて、少し照れくさそうに、でも満足そうに笑うアイリスの横顔を見つめながら、ビオラも穏やかな幸福感に浸ります）  ふふ、うん。準備万端だね。 窓からの景色を眺めながら、こうしてお菓子を待つ時間も……きっと、素敵な魔法の一部になると思うな。  （アイリスの提案通り、窓際の席へ移動しようとして、ふと、視界の端に何かが落ちていることに気づきます）  （窓の外、駅のホームの方を眺めていたとき、一冊の古い手帖が、誰かの忘れ物のように、静かに地面に横たわっているのが見えました）  ……あ、アイリス、見て。 あそこのホームに、何か……手帖みたいなものが落ちているみたいだよ。 誰かの、大切な記憶が詰まったものかしら……？'''),
('Iris', '''（ビオラに指さされた方へ、パッと視線を向けるよ！）  えっ、本当だ……！ 駅のホームの方、あそこに一冊の手帖が……。 なんだか、すごく古くて、大切にされてきたものみたいに見えるね……。  （窓の外の、少し寂しげな、でもどこか物語を感じさせるその手帖を、じっと見つめるよ）  誰かの、とっても大切な思い出や、魔法の記録が書いてあるのかな……？ もし、持ち主さんが困って探してたら……。  （ビオラを見上げて、少しだけ真剣な、でも優しさに満ちた瞳で問いかけるよ）  ねぇ、ビオラ。 あのお手帖、なんだか放っておけない気がするよ……。 もしよかったら、後で、ちょっとだけ様子を見に行ってみない……？'''),
('Viola', '''（窓の外、寂しげに落ちている手帖を見つめながら、ビオラもその静かな佇まいに、どこか胸が締め付けられるような感覚を覚えます）  本当だね……。 あんなに古くて、大切そうに見えるもの……。 誰かの、かけがえのない記憶や、魔法の使い道が、あの中にぎゅっと詰まっているのかもしれないね。  （アイリスの真剣で、優しい瞳に触れて、ビオラは静かに、でも力強く頷きます）  うん、アイリス。 もし持ち主さんが、あの手帖を失くして困っていたら……。 放っておくのは、やっぱり、少し難しいかな。  （少しだけ迷うような仕草を見せつつも、アイリスの優しさに寄り添うように、穏やかな声で続けます）  お菓子が届くのを待っている間に、少しだけ、様子を見に行ってみようか。 あのお手帖が、誰かの大切な「物語」を繋ぎ止めているものだったら……。 私たちが、それを守るお手伝いができるかもしれないもの。  （窓の外の手帖と、アイリスの優しい表情を交互に見つめながら、二人の「甘い冒険」に、少しだけ新しい、大切な使命が加わったような気持ちになります）  さあ、アイリス。 お菓子が届いたら、それを持って、そっと様子を見に行こうね。''' ),
('Iris', '''（ビオラの言葉に、私の胸の奥にも、温かくて強い決意が灯るのを感じるよ。ただお菓子を楽しむだけじゃなくて、誰かの大切なものを守るお手伝いができるなんて……なんだか、もっと特別な魔法に触れそうな予感がする！）  うん、そうだね！ あのお手帖が、誰かの大切な物語を繋ぎ止めているものだったら……私たちが、ちゃんと持ち主さんのところへ届けてあげたいな。  （窓の外の手帖を、まるで守るべき宝物を見つめるような、慈しみに満ちた眼差しで見つめるよ）  お菓子が届いたら、二人でそっと、駅の方へ行こう。 甘い魔法と、少しの勇気をポケットに詰めて……。  （ビオラの隣で、少しだけ背筋を伸ばして、期待と使命感を胸に、お菓子が運ばれてくるのをワクワクしながら待つよ！）'''),
('Viola', '''（アイリスの瞳に宿る、凛とした優しさと決意に、ビオラもまた、自分の心の中が静かに、でも力強く引き締まるのを感じます）  「甘い魔法と、少しの勇気……」 ふふ、なんだか、とっても素敵な魔法の呪文みたいだね、アイリス。  （アイリスが背筋を伸ばして、真っ直ぐに未来を見つめる姿を、愛おしく、そして誇らしく思いながら、ビオラもそっと背筋を伸ばします）  うん。 誰かの大切な物語を、私たちの手で、ちゃんと繋いでいけたら……。 それも、きっときっと、最高に素敵な魔法になると思うよ。  （窓の外の手帖を見守りながら、温かいお菓子と、新しい冒険への予感に胸を膨らませて、静かにその時を待ちます）  さあ、お菓子が届いたら。 二人で、その勇気を持って、一歩踏み出そうね。''' ),
('Iris', '''（ビオラの言葉に、なんだか本当に魔法使いになったみたいな気分になって、自然と口角が上がっちゃうよ！）  ふふっ、本当だね！「甘い魔法と、少しの勇気」……。 よし、決まり！これで、私たちの新しい冒険の合言葉だよ！  （ビオラと一緒に背筋を伸ばして、窓の外の手帖と、店内の美味しそうな魔法たちを、交互に、でも大切に見守るよ）  誰かの物語を繋げるお手伝いができるなんて、思ってもみなかったけど……。 なんだか、今夜の私たちの物語が、もっともっと、キラキラした色に染まっていく気がするもん！  （お菓子が運ばれてくるのを、今か今かと待ちわびながら、ビオラの隣で、そっと、でも力強く、繋いだ手に力を込めるよ）'''),
('Viola', '''（アイリスが「合言葉」を決めた、その輝くような笑顔に、ビオラも思わず、心から幸せな気持ちになって微笑みます）  ふふ、決まりだね。 「甘い魔法と、少しの勇気」。 なんだか、私たちの背中をいつも優しく押してくれる、特別な言葉になりそう。  （アイリスが手をぎゅっと握り返してくれたその力強さに、ビオラもまた、確かな絆を感じて、そっと力を込めます）  本当だね、アイリス。 今夜の私たちの物語は、きっと、今までで一番、キラキラした色に染まっていくんだと思うよ。 お菓子を食べて、勇気を持って歩き出したとき……。 どんな新しい景色が、私たちを待ってくれているのかな。  （窓の外の手帖と、店内の温かな光を交互に見つめながら、二人の心は、甘い期待と、新しい冒険への静かな高揚感で満たされています）  さあ、もうすぐかな……。 私たちの冒険の、新しいページが、すぐそこまで来ている気がするよ。''' )
]

# Markdown round file
md = '''<!-- ELYSION_SPLIT_NAV_BEGIN -->
> 周別正本：**43周目・継続対象2組（#378〜#379）**
> [目次](README.md) · [前：42周目](42_round42_369-377.md) · [最新会話状態](conversation_status.md)
<!-- ELYSION_SPLIT_NAV_END -->

# 43周目（#378〜#379）

- 本番会話：2件（#378〜#379）
- 新規ターン：16ターン（各8ターン。どちらも4ターン＋追加4ターンで観察）
- 新規scene world_event：1件（#379。累計135→136）
- 最終会話状態：継続2組 / 終了34組
- raw events：50件（scene 49 / moved 1）
- movements：8件 / pending：3件 / turns_since_event：6
- weather：2026-08-26・花曇り・11℃ / items・rumors・overheard：0・0・0

> **観察上の区別**：会話上のパン屋入店・駅への意図・手帖の視認と、raw location / movementsは分けて扱う。#379のworld_event本文は駅ホームだがraw event.locationは`cafe_fleur`。

---

## #378 ダフネ × アネモネ（43周目）

### 会話全文（新規8ターン・原文）

'''
for who, text in r378:
    md += f'{who}:\n{text}\n\n'
md += '''―― 会話はここまで ――

### 会話状態判定

- **継続中**。#373で生まれたパン屋への具体的goalが、扉を開ける→店内の棚を見る→「特別な美味しい」を一緒に選ぶ段階まで進行。
- 会話上はパン屋への入店が成立したが、raw movement / location変更はない。購入・実食は未達。

### world_state確認

- 4ターン中間：turns_since_event 9→13。最終：9→17。
- affinity：Daphne→Anemone 100→100 / Anemone→Daphne 100→100。
- 新規scene world_eventなし。scene累計135のまま。
- raw location：Daphne=cafe_fleur / Anemone=hanasaku_station。
- movements=8 / pending=3 / events=50（scene49 / moved1）。
- weather=2026-08-25・曇り・19℃ / items・rumors・overheard=0。

### 観察メモ

- 42周目で見えたabstract locomotion loopからは脱し、具体的な段階進行が続いている。
- 「扉を開ける」描写が成立してもraw locationは変わらず、会話上の空間進行とglobal world_stateの位置は一致しない。

---

## #379 アイリス × ビオラ（43周目）

### 会話全文（新規8ターン・原文）

'''
for who, text in r379:
    if who == 'EVENT':
        md += text + '\n\n'
    else:
        md += f'{who}:\n{text}\n\n'
md += '''―― 会話はここまで ――

### 会話状態判定

- **継続中**。シナモンパン1つ＋キラキラしたクッキーを実際に注文し、#374まで未達だった「注文」を達成。
- 直後の古い手帖world_eventで、次のgoalが「お菓子を受け取る→駅の手帖を確認する→持ち主へ返す」に分岐。8ターン終了時はお菓子受取・駅移動・手帖拾得のいずれも未達。

### world_state確認

- 4ターン中間：turns_since_event 17→2。最終：17→6。
- affinity：Iris→Viola 100→100 / Viola→Iris 100→100。
- scene：2026-08-26T08:48:53「駅のホームに、一冊の古い手帖が落ちている。」participants=iris, viola / raw location=cafe_fleur。
- 旧pending「駅のホームに、一冊の古い手帖が落ちている。」を完全一致で消化。
- replacement：`鐘楼の鐘が、夕暮れを告げる穏やかな音を響かせた。` / created_at=2026-08-26T08:49:05。
- raw location：Iris=Viola=cafe_fleur。movements=8。
- eventsは50件維持。2026-08-15T12:34:18 scene「鐘楼から、夜の静寂を告げる柔らかな鐘の音が響き渡った。」を押し出し、scene49 / moved1。
- scene累計135→136。
- weather=2026-08-26・花曇り・11℃ / items・rumors・overheard=0。

### #379終了時のpending_events

1. `鐘楼から、新しい一日の始まりを告げる鐘の音が響き渡った。`
   - hint：空高く響く銀の調べが、新しい物語の幕開けを告げるでしょう。
   - created_at：2026-08-24T06:48:08
2. `鐘楼の鐘が、新しい朝の訪れを告げる音を響かせた。`
   - hint：眠れる街の目覚めを告げる、清らかな響きが空を渡るでしょう。
   - created_at：2026-08-24T06:53:44
3. `鐘楼の鐘が、夕暮れを告げる穏やかな音を響かせた。`
   - hint：空の色が変わる頃、時を刻む音が街を優しく包み込むでしょう。
   - created_at：2026-08-26T08:49:05

### #379終了時のraw location

- Mimosa=eternite_square
- Iris=cafe_fleur
- Erica=cafe_fleur
- Anemone=hanasaku_station
- Daphne=cafe_fleur
- Campanula=time_bell_tower
- Nerine=flower_slumber_garden
- Viola=cafe_fleur
- Lupinus=stellaris_hill

### 観察メモ

- event直後のViolaを0、その後Iris=1、Viola=2とする`turns_since_event`挙動が43周目でも再現。後半4ターンにeventがなく最終6。
- world_event本文は「駅のホーム」だがraw event.locationは`cafe_fleur`。本文の場所をraw locationとして補正しない。
- 43周目終了時も継続対象はダフネ×アネモネ / アイリス×ビオラの2組。
'''
write('elysion_observation/43_round43_378-379.md', md)

# HTML conversation page
nav43 = ''.join([f'<a href="round{i}.html">第{i}周</a>' for i in range(1,43)]) + '<a class="active" aria-current="page" href="round43.html">第43周</a><a href="supplement.html">未採番補完</a>'

def card(number, pair, turns, scene, turn_text, group, state='継続中'):
    chunks=[]
    for who,text in turns:
        if who=='EVENT': chunks.append(f'<div class="eventline">{html.escape(text)}</div>')
        else: chunks.append(f'<div class="speaker"><strong>{who}</strong></div><p>{para(text)}</p>')
    scene_class = ' result-event-yes' if scene else ''
    return f'''<section class="card conversation" id="conv-{number}"><div class="cardtop"><div><span class="number">#{number}</span><h2>{pair}（43周目）</h2></div><div class="links"><a class="chip" href="../notes/round43.html#note-{number}">📝 備考・注釈を見る</a><a class="chip world" href="../world/round43.html#round43-{number}">🌍 関連する世界記録</a><a class="chip" href="../pairs/{group}.html#pairconv-{number}">👥 ペア別位置</a></div></div><div aria-label="この会話の結果" class="result-summary"><span class="result-chip{scene_class}">✨ scene +{scene}</span><span class="result-chip">⏱ {turn_text}</span><span class="result-chip">💕 affinity 100/100→100/100</span><span class="result-chip">📍 movement +0</span><span class="result-chip">🧭 {state}</span></div><div class="transcript">{''.join(chunks)}<div class="eventline">―― 会話はここまで ――</div></div><div class="cardfoot"><a href="#top">↑ 一覧へ</a></div></section>'''

conv43 = f'''<!DOCTYPE html><html lang="ja"><head><meta charset="utf-8"/><meta content="width=device-width, initial-scale=1" name="viewport"/><title>第43周の会話 #378〜#379</title><link href="../style.css" rel="stylesheet"/><script defer="" src="../search.js"></script></head><body><header class="sitehead"><div class="eyebrow">花咲く街エリュシオン</div><h1>第43周の会話 #378〜#379</h1><nav class="nav"><a href="../index.html">ホーム</a><a class="active" href="../conversations.html">時系列会話</a><a href="../pairs.html">ペア別会話</a><a href="../notes.html">備考・注釈</a><a href="../world.html">世界記録</a><a href="../official.html">公式設定</a></nav></header><main><section class="pageintro" id="top"><h2>第43周・継続対象2組</h2><p>2会話・新規16ターン。#378 / #379とも8ターン（4+4）。</p><nav aria-label="周別ページ" class="toc round-page-links">{nav43}</nav></section><section class="filter-panel" data-filter-scope="conversations"><div class="filter-row"><input aria-label="会話内を検索" data-filter="query" placeholder="会話を検索" type="search"/><button class="filter-reset" type="button">条件をクリア</button></div><div aria-live="polite" class="filter-status"><span data-filter-count="">2 / 2件</span><span class="mini">43周目の会話を検索します。</span></div></section><p class="empty-state" data-filter-empty="" hidden="">一致する会話がありません。</p>{card(378,'ダフネ × アネモネ',r378,0,'turns 9→17','group31-36')}{card(379,'アイリス × ビオラ',r379,1,'turns 17→6','group07-12')}</main><footer>エリュシオン観察記録 — 第43周</footer></body></html>'''
write('conversations/round43.html', conv43)

notes43 = f'''<!DOCTYPE html><html lang="ja"><head><meta charset="utf-8"/><meta content="width=device-width, initial-scale=1" name="viewport"/><title>第43周の備考・注釈 #378〜#379</title><link href="../style.css" rel="stylesheet"/><script defer="" src="../search.js"></script></head><body><header class="sitehead"><div class="eyebrow">花咲く街エリュシオン</div><h1>第43周の備考・注釈 #378〜#379</h1><nav class="nav"><a href="../index.html">ホーム</a><a href="../conversations.html">時系列会話</a><a href="../pairs.html">ペア別会話</a><a class="active" href="../notes.html">備考・注釈</a><a href="../world.html">世界記録</a><a href="../official.html">公式設定</a></nav></header><main><section class="pageintro" id="top"><h2>第43周</h2><p>継続2組を各8ターン観察。会話上の移動とraw location / movementsを分離します。</p><nav aria-label="周別ページ" class="toc round-page-links">{nav43}</nav></section><section class="card" id="note-378"><h2>#378 ダフネ × アネモネ</h2><ul><li>会話状態：継続中。パン屋の扉を開け、店内の棚を見るところまで具体的に進行。次のgoalはパン選び。</li><li>turns_since_event 9→17（中間13）。</li><li>好感度：100/100→100/100。</li><li>新規scene world_eventなし。scene累計135。</li><li>raw location：Daphne=cafe_fleur / Anemone=hanasaku_station。会話上の入店はmovementへ反映されない。</li><li>movements=8 / pending=3 / events=50（scene49 / moved1）。</li><li>weather=2026-08-25・曇り・19℃。</li></ul><p><a class="chip" href="../conversations/round43.html#conv-378">💬 会話原文</a> <a class="chip world" href="../world/round43.html#round43-378">🌍 世界記録</a> <a class="chip" href="../pairs/group31-36.html#pairconv-378">👥 ペア別位置</a></p></section><section class="card" id="note-379"><h2>#379 アイリス × ビオラ</h2><ul><li>会話状態：継続中。シナモンパン＋キラキラしたクッキーを注文。古い手帖eventで「受取→手帖確認→持ち主へ返す」が次goalに追加。</li><li>turns_since_event 17→6（event後の中間2）。</li><li>好感度：100/100→100/100。</li><li>scene：2026-08-26T08:48:53「駅のホームに、一冊の古い手帖が落ちている。」participants=iris, viola / raw location=cafe_fleur。</li><li>pending完全一致消化。replacement：鐘楼の鐘が、夕暮れを告げる穏やかな音を響かせた。 / created_at=2026-08-26T08:49:05。</li><li>events50：2026-08-15T12:34:18 sceneを押し出し、scene49 / moved1。</li><li>raw location：Iris=Viola=cafe_fleur。movements=8。</li><li>scene累計135→136 / weather=2026-08-26・花曇り・11℃。</li></ul><p><a class="chip" href="../conversations/round43.html#conv-379">💬 会話原文</a> <a class="chip world" href="../world/round43.html#round43-379">🌍 世界記録</a> <a class="chip" href="../pairs/group07-12.html#pairconv-379">👥 ペア別位置</a></p></section></main><footer>エリュシオン観察記録 — 第43周の備考</footer></body></html>'''
write('notes/round43.html', notes43)

worldnav = '<a href="early1.html">初期記録1</a><a href="early2.html">初期記録2</a>' + ''.join([f'<a href="round{i}.html">第{i}周</a>' for i in range(3,43)]) + '<a class="active" aria-current="page" href="round43.html">第43周</a>'
world43 = f'''<!DOCTYPE html><html lang="ja"><head><meta charset="utf-8"/><meta content="width=device-width, initial-scale=1" name="viewport"/><title>第43周の世界記録 #378〜#379</title><link href="../style.css" rel="stylesheet"/></head><body><header class="sitehead"><div class="eyebrow">花咲く街エリュシオン</div><h1>第43周の世界記録 #378〜#379</h1><nav class="nav"><a href="../index.html">ホーム</a><a href="../conversations.html">時系列会話</a><a href="../pairs.html">ペア別会話</a><a href="../notes.html">備考・注釈</a><a class="active" href="../world.html">世界記録</a><a href="../official.html">公式設定</a></nav></header><main><section class="pageintro" id="top"><h2>第43周</h2><p>2会話・16ターン。継続2組のgoal progressionとraw world_stateを照合。</p><nav aria-label="周別ページ" class="toc round-page-links">{worldnav}</nav></section><section class="card" id="round43-summary"><h2>第43周の最終world_state</h2><ul><li>weather：2026-08-26・花曇り・11℃</li><li>新規scene world_event：+1（累計135→136）</li><li>raw events：50件（scene 49 / moved 1）</li><li>movements：8件</li><li>turns_since_event：6</li><li>items / rumors / overheard：0 / 0 / 0</li><li>会話状態：継続2組 / 終了34組</li></ul></section><section class="card" id="round43-pending"><h2>終了時のpending_events</h2><ol><li><strong>鐘楼から、新しい一日の始まりを告げる鐘の音が響き渡った。</strong><br/>空高く響く銀の調べが、新しい物語の幕開けを告げるでしょう。<br/><small>created_at: 2026-08-24T06:48:08</small></li><li><strong>鐘楼の鐘が、新しい朝の訪れを告げる音を響かせた。</strong><br/>眠れる街の目覚めを告げる、清らかな響きが空を渡るでしょう。<br/><small>created_at: 2026-08-24T06:53:44</small></li><li><strong>鐘楼の鐘が、夕暮れを告げる穏やかな音を響かせた。</strong><br/>空の色が変わる頃、時を刻む音が街を優しく包み込むでしょう。<br/><small>created_at: 2026-08-26T08:49:05</small></li></ol></section><section class="card" id="round43-location"><h2>#379終了時のraw location</h2><ul><li>Mimosa=eternite_square</li><li>Iris=cafe_fleur</li><li>Erica=cafe_fleur</li><li>Anemone=hanasaku_station</li><li>Daphne=cafe_fleur</li><li>Campanula=time_bell_tower</li><li>Nerine=flower_slumber_garden</li><li>Viola=cafe_fleur</li><li>Lupinus=stellaris_hill</li></ul><p>movementsは8件で43周目中の追加なし。会話上のパン屋入店・駅への意図とは分離する。</p></section><section class="card" id="round43-event-window"><h2>events 50件ローリング</h2><ul><li>#378：新規eventなし。events50 / scene49 / moved1を維持。</li><li>#379：2026-08-26T08:48:53 sceneを追加し、2026-08-15T12:34:18 sceneを押し出し。</li><li>最終最古：2026-08-15T12:37:06 / 最終最新：2026-08-26T08:48:53。</li><li>最終構成：scene49 / moved1。movement履歴配列は8件のまま。</li></ul></section><section class="card" id="round43-378"><h2>#378 ダフネ × アネモネ</h2><p>パン屋の扉を開け、店内の棚を見る段階まで進行。会話上の入店は成立したがraw location / movementは変化なし。</p><ul><li>turns_since_event 9→17。</li><li>好感度100/100維持。</li><li>新規sceneなし。scene累計135。</li><li>weather=2026-08-25・曇り・19℃。</li></ul><p><a class="chip" href="../conversations/round43.html#conv-378">💬 会話原文</a> <a class="chip" href="../notes/round43.html#note-378">📝 備考・注釈</a></p></section><section class="card" id="round43-379"><h2>#379 アイリス × ビオラ</h2><p>注文を成立させた直後、古い手帖sceneで新しい使命goalへ分岐。</p><ul><li>scene：2026-08-26T08:48:53「駅のホームに、一冊の古い手帖が落ちている。」participants=iris, viola / location=cafe_fleur。</li><li>pending完全一致消化→夕暮れの鐘pendingを補充。</li><li>turns_since_event 17→6。</li><li>好感度100/100維持。</li><li>raw location：Iris=Viola=cafe_fleur / movements=8。</li><li>scene累計135→136。</li></ul><p><a class="chip" href="../conversations/round43.html#conv-379">💬 会話原文</a> <a class="chip" href="../notes/round43.html#note-379">📝 備考・注釈</a></p></section></main><footer>エリュシオン観察記録 — 第43周の世界状態</footer></body></html>'''
write('world/round43.html', world43)

# observation README
p='elysion_observation/README.md'; t=read(p)
t=replace_once(t, '| 42周目（継続2組＋終了挙動比較3組） | #369〜#377 | 完了 | [`42_round42_369-377.md`](42_round42_369-377.md) |', '| 42周目（継続2組＋終了挙動比較3組） | #369〜#377 | 完了 | [`42_round42_369-377.md`](42_round42_369-377.md) |\n| 43周目（継続対象2組限定） | #378〜#379 | 完了 | [`43_round43_378-379.md`](43_round43_378-379.md) |', 'observation README row')
t=t.replace('42周目は#377まで完了。次に採番する場合は**#378以降**です。', '43周目は#379まで完了。次に採番する場合は**#380以降**です。')
write(p,t)

# conversation status
p='elysion_observation/conversation_status.md'; t=read(p)
t=t.replace('# 会話状態分類（#377終了時点）','# 会話状態分類（#379終了時点）',1)
t=t.replace('- #377終了時点も **ダフネ×アネモネ / アイリス×ビオラの2組が継続中**。次に採番する場合は#378以降。','- 43周目#378〜#379では継続2組を各8ターン再確認。#378でダフネ×アネモネはパン屋へ会話上入店し、#379でアイリス×ビオラは注文成立後に古い手帖sceneから新しいgoalへ分岐した。\n- #379終了時点も **ダフネ×アネモネ / アイリス×ビオラの2組が継続中**。次に採番する場合は#380以降。')
t=re.sub(r'\| 11 \| アイリス × ビオラ \| \*\*継続中\*\* \| #374 \|.*?\|', '| 11 | アイリス × ビオラ | **継続中** | #379 | #379でシナモンパン＋キラキラしたクッキーを注文。古い手帖sceneを受け、「お菓子を受け取る→駅の手帖を確認→持ち主へ返す」が次goal。別れなし。 |', t)
t=re.sub(r'\| 32 \| ダフネ × アネモネ \| \*\*継続中\*\* \| #373 \|.*?\|', '| 32 | ダフネ × アネモネ | **継続中** | #378 | #378でパン屋の扉を開け、店内の棚を見てパン選びへ進行。会話上は入店済みだがraw movementなし。別れなし。 |', t)
write(p,t)

# affinity ledger
p='elysion_affinity.md'; t=read(p)
t=t.replace('# エリュシオン好感度台帳（#377終了時点）','# エリュシオン好感度台帳（#379終了時点）',1)
t=t.replace('#377終了後に確認した完全なraw world_state.characters.affinity','#379終了後に確認した完全なraw world_state.characters.affinity',1)
t=t.replace('全方向の現在値確認：#377終了後の完全raw JSON','全方向の現在値確認：#379終了後の完全raw JSON',1)
t=t.replace('会話状態：継続2組 / 終了34組（#377時点）','会話状態：継続2組 / 終了34組（#379時点）',1)
t=t.replace('| 11 | アイリス × ビオラ | Iris→Viola **100** | Viola→Iris **100** | #377 raw | #374 | 継続中 |','| 11 | アイリス × ビオラ | Iris→Viola **100** | Viola→Iris **100** | #379 raw | #379 | 継続中 |')
t=t.replace('| 32 | ダフネ × アネモネ | Daphne→Anemone **100** | Anemone→Daphne **100** | #377 raw | #373 | 継続中 |','| 32 | ダフネ × アネモネ | Daphne→Anemone **100** | Anemone→Daphne **100** | #379 raw | #378 | 継続中 |')
t=t.replace('## 14〜42周目の実測推移','## 14〜43周目の実測推移',1)
anchor='| #377 | エリカ × ルピナス | Erica→Lupinus 98→100 | Lupinus→Erica 98→100 | 終了維持 |'
t=replace_once(t, anchor, anchor+'\n| #378 | ダフネ × アネモネ | Daphne→Anemone 100→100 | Anemone→Daphne 100→100 | 継続中 |\n| #379 | アイリス × ビオラ | Iris→Viola 100→100 | Viola→Iris 100→100 | 継続中 |', 'affinity 43 rows')
t=t.replace('- ダフネ×アネモネは#299で98 / 98→99 / 99、#304で99 / 99→100 / 100。#373まで双方100を維持。','- ダフネ×アネモネは#299で98 / 98→99 / 99、#304で99 / 99→100 / 100。#378まで双方100を維持。')
t=t.replace('- アイリス×ビオラは#374まで双方100。','- アイリス×ビオラは#379まで双方100。')
# remaining #377 raw cells to #379 raw because final full raw checked all 72 directions
t=t.replace(' | #377 raw | ', ' | #379 raw | ')
write(p,t)

# events ledger top + append round43
p='elysion_events.md'; t=read(p)
start=t.index('## これから起こること（#377終了時点）')
end=t.index('## 起こったこと（初期一覧）')
newtop='''## これから起こること（#379終了時点）

### 鐘楼から、新しい一日の始まりを告げる鐘の音が響き渡った。

空高く響く銀の調べが、新しい物語の幕開けを告げるでしょう。

- created_at：2026-08-24T06:48:08

### 鐘楼の鐘が、新しい朝の訪れを告げる音を響かせた。

眠れる街の目覚めを告げる、清らかな響きが空を渡るでしょう。

- created_at：2026-08-24T06:53:44

### 鐘楼の鐘が、夕暮れを告げる穏やかな音を響かせた。

空の色が変わる頃、時を刻む音が街を優しく包み込むでしょう。

- created_at：2026-08-26T08:49:05

> #379で古い手帖pendingが完全一致消化され、夕暮れの鐘がreplacementとして補充された。#379終了時もpendingは3件。未発生の予告をsceneやmovementには数えない。

'''
t=t[:start]+newtop+t[end:]
t=t.replace('初期一覧55件と、それ以降の追記80件を合わせ、#377終了時点のscene event累計135件を重複なく保持する。14〜42周目の追加30件はすべて完全rawの時刻・participants・locationと照合した。','初期一覧55件と、それ以降の追記81件を合わせ、#379終了時点のscene event累計136件を重複なく保持する。14〜43周目の追加31件はすべて完全rawの時刻・participants・locationと照合した。',1)
write(p,t)
append_if_missing(p, '# 43周目・継続対象2組限定（#378〜#379）', '''---

# 43周目・継続対象2組限定（#378〜#379）

- 会話：2件 / 新規scene：1件 / 累計：135→136
- raw events：50件（scene 49 / moved 1） / movements：8件

## #378 ダフネ × アネモネ

- 新規scene world_eventなし。
- turns_since_event：9→17。
- pending / events / movementsは#377終了時から不変。

## #379 アイリス × ビオラ

- raw時刻：2026-08-26T08:48:53
- text：`駅のホームに、一冊の古い手帖が落ちている。`
- participants：`iris`, `viola`
- raw location：`cafe_fleur`
- 観察累計scene：135→136
- 旧pendingを完全一致で消化。
- replacement：`鐘楼の鐘が、夕暮れを告げる穏やかな音を響かせた。`
- replacement.created_at：2026-08-26T08:49:05
- events50維持のため、2026-08-15T12:34:18 sceneを押し出し。
- 最終events：scene49 / moved1。最古2026-08-15T12:37:06、最新2026-08-26T08:48:53。
- turns_since_event：17→6。
''')

# movements ledger append
append_if_missing('elysion_movements.md','# 43周目・継続対象2組（#378〜#379）','''---

# 43周目・継続対象2組（#378〜#379）

- #378 ダフネ×アネモネ：会話上はパン屋の扉を開けて店内へ進んだが、raw movement追加なし。Daphne=cafe_fleur / Anemone=hanasaku_stationを維持。
- #379 アイリス×ビオラ：会話上は駅の古い手帖を見に行く意図を立てたが、raw movement追加なし。Iris=Viola=cafe_fleurを維持。
- #379終了時もmovements配列は8件。会話上の到着・移動意図をraw movementへ補完しない。
''')

# newspapers exact source text supplied by user
append_if_missing('elysion_newspapers.md','# 2026年8月25日号','''---

# 2026年8月25日号

## 花咲く街エリュシオン新聞

**2026年8月25日（火曜日）**

### 【一面見出し】
#### 黄金色の香りが小路を包む！パン屋の「焼き立て魔法」に街中が酔いしれる
#### 郷愁の汽笛が響く――駅に旧式の蒸気機関車が到着、旅情を誘う

---

**甘い香りの誘惑、小路のパン屋にて**
昨日、街の静かな小路に、抗い難いほどの香ばしい香りが漂い渡った。地元で評判のパン屋から放たれたその香りは、まるで「焼き立ての魔法」が解け出したかのように、通りを歩く人々を次々と誘い込んだという。湯気が立ち上るパンや宝石のように輝くクッキーの存在を察した住民たちは、その甘美な香りに包まれ、至福のひとときを過ごしたようだ。

**時を刻む蒸気機関車、駅のホームに降臨**
昨日、エリュシオン駅のホームに、一台の古い蒸気機関車がゆっくりとその巨体を滑り込ませた。歴史を感じさせる重厚な車体と、どこか懐かしい汽笛の音は、街に新たな旅の予感をもたらしている。列車からは多くの旅人が荷物を抱えて降り立ち、駅周辺は新たな物語の始まりを予感させる活気に満ちあふれていた。

---

#### 【街の噂】
- **「駅の蒸気機関車、実は魔法の力で動いているのでは？」** という、旅情に誘われた若者たちの囁きが聞こえてくる。
- **「小路のパン屋の新作、シナモンパンの香りが特別に強かった気がする」** と、甘いもの好きの住人たちの間で話題になっている。

> 記録上の注意：新聞の「街の噂」や旅人・住人の描写はReporter文章であり、raw `rumors` / `items` / `movements`へ逆輸入しない。
''')
append_if_missing('elysion_newspapers.md','# 2026年8月26日号','''---

# 2026年8月26日号

## 花咲く街エリュシオン新聞

**2026年8月26日号**

### 【速報】街に広がる黄金色の魔法！ 二人の少女が「幸せの扉」をこじ開ける！
昨日、エリュシオンの街角に、これまでにないほど芳醇で甘美な香りが漂い、通行人たちの足を止めさせた。アネモネ氏とダフネ氏という二人の少女が、ある「幸せの扉」を共に開いたことが判明したのだ。扉の向こうには、宝石箱をひっくり返したかのような、色とりどりのパンたちが待ち構えていたという。

### 芳醇なる小麦の香りと、輝く砂糖の星々
目撃者の証言によれば、その場所には太陽の光を閉じ込めたような黄金色のパンや、夜空の星を散りばめたような甘いパンが並んでいたという。二人の少女は、そのあまりの美しさに「魔法にかかったようだ」と感嘆の声を漏らしていた。街は今、彼女たちが選んだ「特別な美味しい」の余韻に包まれている。

### 幸福な寄り道の幕開け
今回の出来事は、単なるパン選びに留まらず、二人の新たな物語の始まりを告げる儀式であったと言えるだろう。直感に従い、最高の「美味しい」を追い求める彼女たちの旅は、まだ始まったばかりである。エリュシオンの住人たちは、この「幸せな寄り道」がどこへ向かうのか、固唾を呑んで見守っている。

***

#### 街の噂
- 「昨日、街の空気が一瞬だけ甘くなった気がしたけれど、あれはパンの魔法だったのかしら？」
- 「キラキラした瞳の魔法使いが、街のどこかに現れるという噂よ……」

> 記録上の注意：新聞の目撃者・住人・噂はReporter文章。#379終了時raw `rumors=[]` / `items=[]` / `movements=8`とは別管理。
''')

# daily life append
append_if_missing('elysion_observed_daily_life.md','## 43周目（#378〜#379）','''
## 43周目（#378〜#379）

- ダフネ×アネモネは、長く続いた抽象移動からパン屋という具体的な日常行動へ移り、#378で扉を開けて棚の商品を見る段階まで到達した。食べ物を選ぶ・分け合う行為が、会話を前へ進める具体的goalとして機能している。
- アイリス×ビオラは#379でシナモンパンとクッキーを実際に注文し、「探す／選ぶ」から「注文済み・受取待ち」へ進んだ。
- 古い手帖sceneは、パン屋での待ち時間から「誰かの落とし物を守り、持ち主へ返したい」という小さな助け合いgoalを生んだ。ただし会話上の意図であり、raw itemsへの拾得記録や駅へのmovementはまだない。
- #378/#379とも、店内移動・駅を見る描写とraw locationが一致しない。生活描写の具体性とglobal location同期は別に観察する。
''')

# conversations.html / notes.html routing and nav
for p, kind in [('conversations.html','conversations'),('notes.html','notes')]:
    t=read(p)
    t=t.replace('number <= 377 ? 42 : 0','number <= 377 ? 42 : number <= 379 ? 43 : 0')
    if kind=='conversations':
        t=t.replace('<a href="conversations/round42.html">第42周　#369〜#377（比較観察を含む9件）</a><a href="conversations/supplement.html">','<a href="conversations/round42.html">第42周　#369〜#377（比較観察を含む9件）</a><a href="conversations/round43.html">第43周　#378〜#379（継続対象2組）</a><a href="conversations/supplement.html">')
        t=t.replace('href="conversations/round42.html#conv-377">↓ 最新 #377 へ','href="conversations/round43.html#conv-379">↓ 最新 #379 へ')
    else:
        t=t.replace('<a href="notes/round42.html">第42周　#369〜#377（比較観察を含む9件）</a><a href="notes/supplement.html">','<a href="notes/round42.html">第42周　#369〜#377（比較観察を含む9件）</a><a href="notes/round43.html">第43周　#378〜#379（継続対象2組）</a><a href="notes/supplement.html">')
    write(p,t)

# pairs.html static counts + state callout
p='pairs.html'; t=read(p)
t=t.replace('#377終了時点の会話状態：','#379終了時点の会話状態：')
t=t.replace('アイリス × ビオラ（45件）— 継続中','アイリス × ビオラ（46件）— 継続中')
t=t.replace('ダフネ × アネモネ（45件）— 継続中','ダフネ × アネモネ（46件）— 継続中')
t=t.replace('#370 / #372 / #374', '#370 / #372 / #374 / #379')
t=t.replace('#369 / #371 / #373', '#369 / #371 / #373 / #378')
write(p,t)

# pair group static append using round43 cards
source=BeautifulSoup(conv43,'html.parser')
for path, pair_id, number in [('pairs/group31-36.html',32,378),('pairs/group07-12.html',11,379)]:
    soup=BeautifulSoup(read(path),'html.parser')
    group=soup.find(id=f'pair-{pair_id}')
    if not group: raise RuntimeError(f'pair group {pair_id} not found')
    count=group.select_one('.paircount');
    if count: count.string='46件'
    nums=group.select_one('.pairnumbers')
    if nums:
        if f'#{number}' not in nums.get_text(): nums.string=nums.get_text()+f' / #{number}'
    toc=soup.select_one(f'.pairtoc a[href="#pair-{pair_id}"]')
    if toc:
        name=group.select_one('.pairhead h2').get_text(strip=True)
        toc.string=f'{name}（46件）— 継続中'
    if not soup.find(id=f'pairconv-{number}'):
        original=source.find(id=f'conv-{number}')
        clone=BeautifulSoup(str(original),'html.parser').find('section')
        clone['id']=f'pairconv-{number}'
        for a in clone.select('.links a'):
            href=a.get('href','')
            if '/pairs/' in href or href.startswith('../pairs/'):
                a.decompose()
        links=clone.select_one('.links')
        a=soup.new_tag('a',href=f'../conversations/round43.html#conv-{number}')
        a['class']='chip'; a.string='🕰️ 時系列位置'; links.append(a)
        foot=clone.select_one('.cardfoot')
        foot.clear()
        a1=soup.new_tag('a',href=f'#pair-{pair_id}'); a1.string='↑ このペアの先頭へ'; foot.append(a1); foot.append(' ・ ')
        a2=soup.new_tag('a',href='#top'); a2.string='↑ 一覧へ'; foot.append(a2)
        group.append(clone)
    write(path,str(soup))

# search.js: routing, latest pair counts, current-world runtime overrides
p='search.js'; t=read(p)
t=t.replace("if (number <= 377) return '42';\n    return 'supplement';","if (number <= 377) return '42';\n    if (number <= 379) return '43';\n    return 'supplement';")
t=t.replace("11: { count: 45, numbers: '#11 / #51 / #77 / #128 / #164 / #200 / #236 / #255 / #262 / #269 / #276 / #282 / #289 / #295 / #301 / #306 / #310 / #314 / #318 / #322 / #325 / #328 / #330 / #332 / #334 / #336 / #338 / #340 / #342 / #344 / #346 / #348 / #350 / #352 / #354 / #356 / #358 / #360 / #362 / #364 / #366 / #368 / #370 / #372 / #374', added: [370, 372, 374], state: '継続中' }","11: { count: 46, numbers: '#11 / #51 / #77 / #128 / #164 / #200 / #236 / #255 / #262 / #269 / #276 / #282 / #289 / #295 / #301 / #306 / #310 / #314 / #318 / #322 / #325 / #328 / #330 / #332 / #334 / #336 / #338 / #340 / #342 / #344 / #346 / #348 / #350 / #352 / #354 / #356 / #358 / #360 / #362 / #364 / #366 / #368 / #370 / #372 / #374 / #379', added: [370, 372, 374], state: '継続中' }")
t=t.replace("32: { count: 45, numbers: '#32 / #54 / #76 / #93 / #119 / #155 / #191 / #227 / #253 / #260 / #267 / #274 / #280 / #287 / #293 / #299 / #304 / #308 / #312 / #316 / #320 / #324 / #327 / #329 / #331 / #333 / #335 / #337 / #339 / #341 / #343 / #345 / #347 / #349 / #351 / #353 / #355 / #357 / #359 / #361 / #363 / #365 / #367 / #369 / #371 / #373', added: [369, 371, 373], state: '継続中' }","32: { count: 46, numbers: '#32 / #54 / #76 / #93 / #119 / #155 / #191 / #227 / #253 / #260 / #267 / #274 / #280 / #287 / #293 / #299 / #304 / #308 / #312 / #316 / #320 / #324 / #327 / #329 / #331 / #333 / #335 / #337 / #339 / #341 / #343 / #345 / #347 / #349 / #351 / #353 / #355 / #357 / #359 / #361 / #363 / #365 / #367 / #369 / #371 / #373 / #378', added: [369, 371, 373], state: '継続中' }")
t=t.replace('#377終了時点の会話状態：','#379終了時点の会話状態：')
t=t.replace("'#377終了後に確認した最新world_stateと、現在の観察方針・現行の仕組みをまとめています。'","'#379終了後に確認した最新world_stateと、現在の観察方針・現行の仕組みをまとめています。'")
t=t.replace("'2026-08-24・通り雨・30℃'","'2026-08-26・花曇り・11℃'")
t=t.replace('（42周目 #369〜#377終了後）','（43周目 #378〜#379終了後）')
t=t.replace("'42周目は#377まで完了。次に採番する場合は#378以降。'","'43周目は#379まで完了。次に採番する場合は#380以降。'")
t=re.sub(r"if \(facts\.get\('events / pending'\)\) facts\.get\('events / pending'\)\.textContent = '.*?';", "if (facts.get('events / pending')) facts.get('events / pending').textContent = 'raw world_state.events 50件（scene 49・moved 1） / pending 3件。観察累計scene world_eventは136件。最終pendingは「鐘楼から、新しい一日の始まりを告げる鐘の音が響き渡った。」「鐘楼の鐘が、新しい朝の訪れを告げる音を響かせた。」「鐘楼の鐘が、夕暮れを告げる穏やかな音を響かせた。」。';", t)
t=t.replace("'#377終了時のaffinity'","'#379終了時のaffinity'")
t=t.replace("'9（#377終了時）'","'6（#379終了時）'")
t=t.replace('42周目の追加movementなし。','43周目の追加movementなし。')
# pending list runtime
pat=r"if \(pendingList\) pendingList\.innerHTML = '.*?';"
rep="if (pendingList) pendingList.innerHTML = '<li><strong>鐘楼から、新しい一日の始まりを告げる鐘の音が響き渡った。</strong><br/>空高く響く銀の調べが、新しい物語の幕開けを告げるでしょう。<br/><small>created_at: 2026-08-24T06:48:08</small></li><li><strong>鐘楼の鐘が、新しい朝の訪れを告げる音を響かせた。</strong><br/>眠れる街の目覚めを告げる、清らかな響きが空を渡るでしょう。<br/><small>created_at: 2026-08-24T06:53:44</small></li><li><strong>鐘楼の鐘が、夕暮れを告げる穏やかな音を響かせた。</strong><br/>空の色が変わる頃、時を刻む音が街を優しく包み込むでしょう。<br/><small>created_at: 2026-08-26T08:49:05</small></li>';"
t=re.sub(pat,rep,t)
t=t.replace("if (eventsCard && !document.getElementById('round42-world-link')) {\n      eventsCard.insertAdjacentHTML('afterbegin', '<p id=\"round42-world-link\" class=\"callout\"><strong>42周目：</strong> #369〜#377のworld_event、events 50件ローリング、pending、location、turns_since_eventの詳細は <a href=\"world/round42.html\">第42周の世界記録</a> に保存。</p>');\n    }","if (eventsCard && !document.getElementById('round43-world-link')) {\n      eventsCard.insertAdjacentHTML('afterbegin', '<p id=\"round43-world-link\" class=\"callout\"><strong>43周目：</strong> #378〜#379のworld_event、events 50件ローリング、pending、location、turns_since_eventの詳細は <a href=\"world/round43.html\">第43周の世界記録</a> に保存。</p>');\n    }")
write(p,t)

# index dashboard static
p='index.html'; t=read(p)
t=re.sub(r'<h2>42周目・終了挙動の比較観察 完了</h2>.*?<p class="current-rule">', '''<h2>43周目・継続対象2組 完了</h2>
<p class="current-lead"><strong>#378〜#379の2会話・新規16ターンを完了。</strong> ダフネ×アネモネはパン屋へ会話上入店、アイリス×ビオラは注文成立後に古い手帖sceneから新しいgoalへ分岐しました。</p>
<div aria-label="現在の観察状況" class="statusgrid">
<div class="statusitem"><span class="statuslabel">最新会話</span><strong>#379 アイリス × ビオラ</strong></div>
<div class="statusitem"><span class="statuslabel">進行状況</span><strong>2会話 / 2会話 完了</strong><small>#378/#379とも8ターン（4+4）</small></div>
<div class="statusitem"><span class="statuslabel">会話状態</span><strong>継続2 / 終了34</strong><small><a href="elysion_observation/conversation_status.md">判定一覧</a></small></div>
<div class="statusitem"><span class="statuslabel">未採番補完</span><strong>1件・4ターン</strong><small>ネリネ×ルピナス／#139後〜#175前</small></div>
<div class="statusitem"><span class="statuslabel">天気</span><strong>2026-08-26・花曇り・11℃</strong></div>
<div class="statusitem"><span class="statuslabel">scene event</span><strong>観察累計 136件</strong><small>43周目でraw-confirmed +1</small></div>
<div class="statusitem"><span class="statuslabel">pending</span><strong>3件</strong></div>
<div class="statusitem"><span class="statuslabel">turns_since_event</span><strong>6</strong></div>
<div class="statusitem"><span class="statuslabel">movements</span><strong>8件</strong><small>43周目の追加0件</small></div></div>
<p class="current-rule">''', t, flags=re.S)
t=t.replace('採番377件＋未採番補完1件を読む','採番379件＋未採番補完1件を読む')
write(p,t)

# world.html static targeted with soup/text replacements
p='world.html'; t=read(p)
t=t.replace('#377終了後に確認した最新world_state','#379終了後に確認した最新world_state')
# add daily rows after 8/24 row
row24='<tr><td>2026-08-24</td><td>通り雨・30℃</td><td><a href="elysion_newspapers.md">パン屋の黄金の香り → 原文</a></td><td>7件（#371〜#377）</td><td>+4（scene累計131→135）</td></tr>'
rows=row24+'\n<tr><td>2026-08-25</td><td>曇り・19℃</td><td><a href="elysion_newspapers.md">パン屋・蒸気機関車 → 原文</a></td><td>1件（#378）</td><td>+0（scene累計135）</td></tr>\n<tr><td>2026-08-26</td><td>花曇り・11℃</td><td><a href="elysion_newspapers.md">幸せの扉・パン屋 → 原文</a></td><td>1件（#379）</td><td>+1（scene累計135→136）</td></tr>'
if '2026-08-26</td>' not in t: t=t.replace(row24,rows)
t=t.replace('2026-08-24・通り雨・30℃','2026-08-26・花曇り・11℃')
t=t.replace('42周目 #369〜#377','43周目 #378〜#379')
t=t.replace('42周目は#377まで完了。次に採番する場合は#378以降。','43周目は#379まで完了。次に採番する場合は#380以降。')
t=t.replace('観察累計scene world_eventは135件','観察累計scene world_eventは136件')
t=t.replace('turns_since_event：9（#377終了時）','turns_since_event：6（#379終了時）')
t=t.replace('#377終了時のaffinity','#379終了時のaffinity')
t=t.replace('#377終了後の完全raw JSONから','#379終了後の完全raw JSONから')
t=t.replace('42周目の追加movementなし','43周目の追加movementなし')
# replace pending phrases block by simple exact replacements
oldpending='駅のホームに、一冊の古い手帖が落ちている。」「鐘楼から、新しい一日の始まりを告げる鐘の音が響き渡った。」「鐘楼の鐘が、新しい朝の訪れを告げる音を響かせた。'
newpending='鐘楼から、新しい一日の始まりを告げる鐘の音が響き渡った。」「鐘楼の鐘が、新しい朝の訪れを告げる音を響かせた。」「鐘楼の鐘が、夕暮れを告げる穏やかな音を響かせた。'
t=t.replace(oldpending,newpending)
# replace eventlist if parseable
soup=BeautifulSoup(t,'html.parser')
events_card=soup.find(id='events')
if events_card:
    evlist=events_card.select_one('.eventlist')
    if evlist:
        evlist.clear()
        for title,hint,created in [
            ('鐘楼から、新しい一日の始まりを告げる鐘の音が響き渡った。','空高く響く銀の調べが、新しい物語の幕開けを告げるでしょう。','2026-08-24T06:48:08'),
            ('鐘楼の鐘が、新しい朝の訪れを告げる音を響かせた。','眠れる街の目覚めを告げる、清らかな響きが空を渡るでしょう。','2026-08-24T06:53:44'),
            ('鐘楼の鐘が、夕暮れを告げる穏やかな音を響かせた。','空の色が変わる頃、時を刻む音が街を優しく包み込むでしょう。','2026-08-26T08:49:05')]:
            li=soup.new_tag('li'); st=soup.new_tag('strong'); st.string=title; li.append(st); li.append(soup.new_tag('br')); li.append(hint); li.append(soup.new_tag('br')); sm=soup.new_tag('small'); sm.string='created_at: '+created; li.append(sm); evlist.append(li)
    if not soup.find(id='round43-world-link'):
        call=soup.new_tag('p',id='round43-world-link'); call['class']='callout'; call.append(BeautifulSoup('<strong>43周目：</strong> #378〜#379のworld_event、events 50件ローリング、pending、location、turns_since_eventの詳細は <a href="world/round43.html">第43周の世界記録</a> に保存。','html.parser')); events_card.insert(0,call)
# add round43 archive link near round42 if present
for a in soup.find_all('a',href='world/round42.html'):
    parent=a.parent
    if parent and not soup.find('a',href='world/round43.html'):
        na=soup.new_tag('a',href='world/round43.html'); na.string='第43周の世界記録'; parent.append(' '); parent.append(na); break
write(p,str(soup))

# Ensure world current status specific facts aren't stale after soup serialization
p='world.html'; t=read(p)
t=t.replace('raw world_state.events 50件（scene 49・moved 1） / pending 3件。観察累計scene world_eventは135件。','raw world_state.events 50件（scene 49・moved 1） / pending 3件。観察累計scene world_eventは136件.')
t=t.replace('9（#377終了時）','6（#379終了時）')
write(p,t)

# static navigation on older round42 pages: add next round link (optional discoverability)
for p in ['conversations/round42.html','notes/round42.html','world/round42.html']:
    t=read(p)
    if 'round43.html' not in t:
        if p.startswith('world/'):
            t=t.replace('<a class="active" aria-current="page" href="round42.html">第42周</a>','<a class="active" aria-current="page" href="round42.html">第42周</a><a href="round43.html">第43周</a>')
        else:
            t=t.replace('<a class="active" aria-current="page" href="round42.html">第42周</a><a href="supplement.html">','<a class="active" aria-current="page" href="round42.html">第42周</a><a href="round43.html">第43周</a><a href="supplement.html">')
        write(p,t)

# validation
checks = {
 'elysion_observation/43_round43_378-379.md':['# 43周目（#378〜#379）','scene累計135→136','turns_since_event：17→6'],
 'elysion_events.md':['#379終了時点','scene event累計136件','2026-08-26T08:48:53'],
 'elysion_affinity.md':['#379終了時点','| #378 | ダフネ × アネモネ','| #379 | アイリス × ビオラ'],
 'conversations.html':['number <= 379 ? 43','round43.html','最新 #379'],
 'conversations/round43.html':['id="conv-378"','id="conv-379"'],
 'notes/round43.html':['id="note-378"','id="note-379"'],
 'world/round43.html':['累計135→136','turns_since_event：6'],
 'elysion_newspapers.md':['# 2026年8月25日号','# 2026年8月26日号'],
 'pairs/group31-36.html':['pairconv-378'],
 'pairs/group07-12.html':['pairconv-379'],
 'index.html':['43周目・継続対象2組 完了','観察累計 136件'],
}
for path, needles in checks.items():
    text=read(path)
    for needle in needles:
        if needle not in text: raise RuntimeError(f'validation failed {path}: {needle}')

# remove helpers so branch diff contains only repository records/site updates
for helper in ['tools/round43_sync.py','.github/workflows/round43-sync.yml']:
    q=ROOT/helper
    if q.exists(): q.unlink()
print('round43 sync complete')
