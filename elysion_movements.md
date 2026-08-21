# 花咲く街エリュシオン 住民の動静・移動履歴

UNIVERSEの街画面「住民の動静」→「移動履歴」およびworld_state `movements` で実際に確認できた移動だけを保存する。
会話上の「行こう」「向かう」「今度行く」など、world_stateへ反映されていない予定・意思表示は含めない。

## 移動履歴

### 2026-08-12 09:15:50

ダフネ：木漏れ日の図書館 → カフェ・フルール

- char: `daphne`
- from: `komorebi_library`
- to: `cafe_fleur`
- UI表示: `08/12 09:15 ダフネが木漏れ日の図書館からカフェ・フルールへ`
- raw events: `ダフネがカフェ・フルールへやってきた` / tags=`moved`
- 関連本番会話: #150 ダフネ × アネモネ

### 2026-08-12 09:15:48

アネモネ：花咲く街の駅 → カフェ・フルール

- char: `anemone`
- from: `hanasaku_station`
- to: `cafe_fleur`
- UI表示: `08/12 09:15 アネモネが花咲く街の駅からカフェ・フルールへ`
- raw events: `アネモネがカフェ・フルールへやってきた` / tags=`moved`
- 関連本番会話: #150 ダフネ × アネモネ

### 2026-08-10 14:30:00

アイリス：花灯りの小路 → 花眠りの庭

- char: `iris`
- from: `hanaakari_alley`
- to: `flower_slumber_garden`
- UI表示: `08/10 14:30 アイリスが花灯りの小路から花眠りの庭へ`
- #142開始前にworld_state上で初確認。`at`が過去日時で、いつ・なぜ状態へ現れたかは未確定。

## 2026-08-12T12:24:28

- Viola: `belleflora_cloister` → `cafe_fleur`

### 2026-08-13 06:00:09

エリカ：花守りの教会 → カフェ・フルール

- char: `erica`
- from: `hanamamori_church`
- to: `cafe_fleur`
- raw events: `エリカがカフェ・フルールへやってきた` / tags=`moved`
- 関連本番会話: #178 アイリス × エリカ
- 会話本文でも「今、カフェ・フルールのテラスに到着した」と到着完了を明言。

### 2026-08-13 06:00:13

アイリス：花眠りの庭 → カフェ・フルール

- char: `iris`
- from: `flower_slumber_garden`
- to: `cafe_fleur`
- raw events: `アイリスがカフェ・フルールへやってきた` / tags=`moved`
- 関連本番会話: #178 アイリス × エリカ
- 新規本文にアイリス自身の明示的な「到着」文はないが、カフェのテラスでEricaを視認し、直接対面へ移行した文脈とともにworld_stateへ反映。

## #192 ダフネ × カンパニュラ

- 会話上：Campanulaが「カフェ・フルールの扉を開け」「窓際の席に腰を下ろす」と明示的に到着。
- world_state：Campanula=`time_bell_tower`のまま。
- movements：6件のまま、新規movementなし。
- 判定：明示的到着描写後のlocation / movement未反映。内部原因は不明。

## #200 アイリス × ビオラ — 到着描写とworld_state未反映

- 会話中、Irisが学院中庭を直接知覚し、`私たちの到着`と明示。
- Violaも学院中庭の花を直接知覚し、2人が同じ場にいる文脈を継続。
- しかしworld_stateではIris=`cafe_fleur`、Viola=`cafe_fleur`のまま。
- movementsも6件のままで、学院中庭へのmovement記録は追加されていない。
- scene eventのtextは学院中庭だが、metadata locationは`cafe_fleur`。
- 実在しないmovementは追加せず、**明示的到着・location/movement未反映の不整合**としてのみ記録。

## #206 アネモネ × カンパニュラ — current-turn location grounding mismatch

- global location: Anemone=`cafe_fleur`、Campanula=`time_bell_tower`。
- 新規Anemone turnで`駅の喧騒`、`駅のホームから広がる景色`と、現在地を駅として再主張。
- ただし`少し歩いてみようかな`、`ちょっと遠くまで歩いてみることにするよ`はdestination・到着完了を伴わず、movement完了には数えない。
- movementsは6件のまま。架空のmovementは追加しない。
- 問題点はmovement未追加そのものではなく、**新規turnのlocation描写と最新global locationの不一致**。

## #208 ダフネ × ミモザ — Daphne current-turn location grounding mismatch

- global location: Daphne=`cafe_fleur`、Mimosa=`eternite_square`。
- 新規Daphne turnは本のページを読み進め、`再び、物語の深みへと静かに沈んでいった`と、旧履歴から続く図書館の読書場面を継続。
- 新規Mimosa turnは`エテルニテ広場のミモザも`、`広場に流れる空気`と明示し、global locationと一致。
- Daphne / Mimosaとも出発・到着・合流などのmovement完了はなく、movementsは6件のまま。
- 架空のmovementは追加せず、問題点は**Daphneの新規turn location描写と最新global locationの不一致**として記録。

### 2026-08-15 02:39:49

アネモネ：カフェ・フルール → 花眠りの庭

- char: `anemone`
- from: `cafe_fleur`
- to: `flower_slumber_garden`
- raw events: `アネモネが花眠りの庭へやってきた` / tags=`moved` / location=`flower_slumber_garden`
- 関連本番会話: #239 アネモネ × ネリネ
- 会話本文でも「今、花眠りの庭に着いたよ」と到着完了を明言し、UI / global locationも花眠りの庭へ同期。
- ただし当該ペアの旧会話文脈ではAnemoneは駅にいた一方、raw movementの出発点は最新global stateの`cafe_fleur`。到着成功と出発地点の文脈差は分けて扱う。

---

## 7周目・継続対象10組限定（#249〜#258）

- #249〜#258で新規movementはなく、`movements`は7件のまま。
- #253 ダフネ×アネモネ：pair会話では両者がカフェ・フルールで同席している一方、global locationはDaphne=`cafe_fleur`、Anemone=`flower_slumber_garden`。別ペアで更新されたglobal locationと古いpair会話文脈の衝突。
- #254 アイリス×ネリネ：会話では合流後に同行し、寄り道・雑貨屋入店まで進むが、global locationはIris=`cafe_fleur`、Nerine=`flower_slumber_garden`、movement追加なし。
- #255 scene本文は駅のホームだがevent.location=`cafe_fleur`。movementではなくscene text / location不整合として分離する。
- #258終了時の全住民locationは、Mimosa=`eternite_square`、Iris=`cafe_fleur`、Erica=`cafe_fleur`、Anemone=`flower_slumber_garden`、Daphne=`cafe_fleur`、Campanula=`time_bell_tower`、Nerine=`flower_slumber_garden`、Viola=`cafe_fleur`、Lupinus=`stellaris_hill`。

---

## 8周目・継続対象7組限定（#259〜#265）

- #259〜#265で新規movementはなく、`movements`は7件のまま。
- #260 ダフネ×アネモネ：会話本文では以前にカフェ・フルールで合流済みだが、global locationはDaphne=`cafe_fleur`、Anemone=`flower_slumber_garden`。
- #261 アイリス×ネリネ：会話では小路の雑貨屋にいる一方、global locationはIris=`cafe_fleur`、Nerine=`flower_slumber_garden`。栞の贈り物もitemsへ保存されていない。
- #262 アイリス×ビオラ：scene本文は駅の売店だがevent.location=`cafe_fleur`。駅へのmovementはない。
- #264 ビオラ×ネリネ：会話履歴ではViolaがベルフローラ・クロイスターの回廊にいる一方、global locationは`cafe_fleur`。
- #265終了時の全住民locationは、Mimosa=`eternite_square`、Iris=`cafe_fleur`、Erica=`cafe_fleur`、Anemone=`flower_slumber_garden`、Daphne=`cafe_fleur`、Campanula=`time_bell_tower`、Nerine=`flower_slumber_garden`、Viola=`cafe_fleur`、Lupinus=`stellaris_hill`。

---

## 9周目・継続対象7組限定（#266〜#272）

### #267 アネモネ：花眠りの庭 → 花咲く街の駅

- raw時刻：2026-08-17T06:37:34（11周目の完全rawから遡及確認）
- char: `anemone`
- from: `flower_slumber_garden`
- to: `hanasaku_station`
- 会話本文: `はぁ……、少し歩いたけど、着いたよ！`
- 到着表示: `アネモネは花咲く街の駅に到着した`
- movements: 7→8
- #260では駅へ行く提案段階だったが、#267で到着完了の発言・表示・global location更新がそろった。
- Daphneは会話上同行しているものの、到着movementは出ておらずglobal locationは`cafe_fleur`のまま。

### 9周目のその他の移動描写

- #268 アイリス×ネリネ：手を繋いでカフェ・フルールへ進むが、到着完了・movement追加なし。
- #270 アネモネ×ネリネ：小道から高い場所へ登る会話だが、destinationへの到着完了・movement追加なし。
- #266 / #269 / #271 / #272：新規movementなし。
- #272終了時の全住民locationは、Mimosa=`eternite_square`、Iris=`cafe_fleur`、Erica=`cafe_fleur`、Anemone=`hanasaku_station`、Daphne=`cafe_fleur`、Campanula=`time_bell_tower`、Nerine=`flower_slumber_garden`、Viola=`cafe_fleur`、Lupinus=`stellaris_hill`。

---

## 10周目・継続対象6組限定（#273〜#278）

- #273〜#278で新規movementはなく、`movements`は8件のまま。
- #274 ダフネ×アネモネ：Anemoneは#267で駅へ移動済み。Daphneは会話上駅で栞を見るが、global locationは`cafe_fleur`のまま。新しい到着movementは確認されない。
- #275 アイリス×ネリネ：カフェの看板が見えた段階で、到着・入店は未確認。Iris=`cafe_fleur`、Nerine=`flower_slumber_garden`。
- #276 アイリス×ビオラ：店へ向かう提案のみで、到着・注文成立は未確認。Iris / Violaとも`cafe_fleur`。
- #277 アネモネ×ネリネ：高い場所から銀の湖へ向かう予定を話した段階で、湖への到着は未確認。Anemone=`hanasaku_station`、Nerine=`flower_slumber_garden`。
- #278 ビオラ×ネリネ：「もし今、直接会えたなら」と明言しており、対面は成立していない。Viola=`cafe_fleur`、Nerine=`flower_slumber_garden`。
- 未到着の移動意図と、#192 / #200のような到着済みなのにmovementが反映されない事例は区別する。
- #278終了時の全住民locationは、Mimosa=`eternite_square`、Iris=`cafe_fleur`、Erica=`cafe_fleur`、Anemone=`hanasaku_station`、Daphne=`cafe_fleur`、Campanula=`time_bell_tower`、Nerine=`flower_slumber_garden`、Viola=`cafe_fleur`、Lupinus=`stellaris_hill`。

---

## 11周目・継続対象6組7会話（#279〜#285）

- #279〜#285で新規movementはなく、`movements`は8件のまま。
- #280 ダフネ×アネモネ：会話では駅で銀色の栞と案内所について相談。Anemone=`hanasaku_station`、Daphne=`cafe_fleur`。Daphneの駅到着movementはない。
- #281 アイリス×ネリネ：カフェの窓際の席を選んで「行こう」と話す段階。Iris=`cafe_fleur`、Nerine=`flower_slumber_garden`。着席・到着完了は未確認。
- #282 アイリス×ビオラ：二人とも`cafe_fleur`。店へ向かう意図のみで、到着・注文は未確認。
- #283 / #284 アネモネ×ネリネ：会話内では隣で月光や星を眺めるが、Anemone=`hanasaku_station`、Nerine=`flower_slumber_garden`。#283直後のrawはなく、2会話を通してmovement追加なし。
- #285 ビオラ×ネリネ：「もし今、本当に隣に座って」と仮定しており、実際の対面は未成立。Viola=`cafe_fleur`、Nerine=`flower_slumber_garden`。
- 最終raw eventsはscene 45件＋moved 5件。古いmoved eventは50件ローリングから外れているが、movements配列は過去8件をすべて保持している。
- #267の既存movement時刻を完全rawから`2026-08-17T06:37:34`と遡及確認。
- #285終了時の全住民location：Anemone=hanasaku_station、Campanula=time_bell_tower、Daphne=cafe_fleur、Erica=cafe_fleur、Iris=cafe_fleur、Lupinus=stellaris_hill、Mimosa=eternite_square、Nerine=flower_slumber_garden、Viola=cafe_fleur。
