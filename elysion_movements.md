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

---

## 12周目・継続対象6組限定（#286〜#291）

- #286〜#291で新規movementはなく、`movements`は8件のまま。
- #287 ダフネ×アネモネ：銀色の栞を会話上で拾得し、万華鏡を使用。Anemone=`hanasaku_station`、Daphne=`cafe_fleur`。Daphneの駅到着や栞返却のmovementはない。
- #288 アイリス×ネリネ：マドレーヌ2つと紅茶を会話上で注文。Iris=`cafe_fleur`、Nerine=`flower_slumber_garden`。Nerineのカフェ到着はrawでは確認されない。
- #289 アイリス×ビオラ：ベーカリーsceneのlocationは`cafe_fleur`。別店舗への到着movementはない。
- #290 アネモネ×ネリネ：星を見る同席描写があるが、global locationは駅／花眠りの庭。
- #291 ビオラ×ネリネ：会話上の心の共有と、Viola=`cafe_fleur`／Nerine=`flower_slumber_garden`を区別する。

---

## 13周目・継続対象6組限定（#292〜#297）

- #292〜#297で新規movementはなく、`movements`は8件のまま。
- #293 ダフネ×アネモネ：パン屋の香りへ向かう散歩の意図のみ。Anemone=`hanasaku_station`、Daphne=`cafe_fleur`。到着・同席・新規movementは未確認。
- #294 アイリス×ネリネ：カフェでの提供・飲食は会話上成立したが、Nerine=`flower_slumber_garden`のまま。Iris=`cafe_fleur`。
- #295 アイリス×ビオラ：両者とも`cafe_fleur`。花形クッキーと星形焼き菓子を選び、注文へ向かう意図まで。
- #296 アネモネ×ネリネ：同じ場所で星空を見る会話だが、Anemone=`hanasaku_station`／Nerine=`flower_slumber_garden`。
- #297 ビオラ×ネリネ：朝の光を通話魔法越しに共有。Viola=`cafe_fleur`／Nerine=`flower_slumber_garden`。
- raw eventsのmovedは5→4へ減ったが50件ローリングによるもの。`movements`配列は過去8件を維持。
- 駅・列車に関するpending 2件は未発生の予告であり、到着やmovementには数えない。
- #297終了時の全住民location：Anemone=hanasaku_station、Campanula=time_bell_tower、Daphne=cafe_fleur、Erica=cafe_fleur、Iris=cafe_fleur、Lupinus=stellaris_hill、Mimosa=eternite_square、Nerine=flower_slumber_garden、Viola=cafe_fleur。

---

## 14〜41周目・継続対象限定（#298〜#368）

- 71会話すべての完全rawでmovements=8を確認。新規movement・location変更は0件。
- #298 アイリス×エリカ、#303 ビオラ×ネリネ、#321 アイリス×ネリネ、#326 アネモネ×ネリネは相互の別れで終了。会話終了とlocation変更は別。
- ダフネ×アネモネは#341までは飲食や散歩の提案が登場するが、#359・#361・#363・#365・#367では「新しい物語の、その、ずっとその先へ」という抽象移動ループが20ターン連続。#367に飲食や新しい到着はない。
- #363の温室午後光sceneはループを終了させず、#365で全力疾走からゆっくり歩く感覚描写へ変化させた。全確認時点でDaphne=`cafe_fleur`、Anemone=`hanasaku_station`のまま。会話上の走行・歩行・同席とraw movement成立は別。
- アイリス×ビオラは「夜の庭園」の注文・受取・初回飲食を経て、#360〜#364で看板への移動目標から学院観察へ寄り道。看板を回収しないまま、#366のsceneで温室到着・入場という新しい会話上の目的へ置換した。
- #368では会話が先に生んだ星形・色変化の花と、sceneで咲いた珍しい色の別の花を区別する。会話上は温室を探索しているが、両者のraw locationはいずれも`cafe_fleur`。
- #368の温室sceneもraw event.location=`cafe_fleur`。温室の会話叙述・scene文面・raw locationを混同しない。
- raw events上のmovedは4→2件へ減ったが50件ローリングによるもの。movements配列に保存された過去8件は欠落していない。
- 最終pending 3件はパン屋の香りの予告であり、店舗到着や移動の証拠ではない。
- #368終了時の全住民location：Anemone=hanasaku_station、Campanula=time_bell_tower、Daphne=cafe_fleur、Erica=cafe_fleur、Iris=cafe_fleur、Lupinus=stellaris_hill、Mimosa=eternite_square、Nerine=flower_slumber_garden、Viola=cafe_fleur。


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

---

# 43周目・継続対象2組（#378〜#379）

- #378 ダフネ×アネモネ：会話上はパン屋の扉を開けて店内へ進んだが、raw movement追加なし。Daphne=cafe_fleur / Anemone=hanasaku_stationを維持。
- #379 アイリス×ビオラ：会話上は駅の古い手帖を見に行く意図を立てたが、raw movement追加なし。Iris=Viola=cafe_fleurを維持。
- #379終了時もmovements配列は8件。会話上の到着・移動意図をraw movementへ補完しない。

---

# 44周目・継続対象2組（#380〜#381）

- #380 ダフネ×アネモネ：会話上はパン屋で「光をまとったパン」を選び、注文・包装を済ませて花眠りの庭へ向かう流れまで進行。「いよいよ花眠りの庭だね」「あそこに着いたら」と話すが、raw movement追加なし。Daphne=`cafe_fleur` / Anemone=`hanasaku_station`を維持。
- #380の鐘scene2件はいずれもraw `event.location=null`。会話内では出発を祝福する鐘として取り込まれたが、住民の移動記録には数えない。
- #381 アイリス×ビオラ：会話上は同席してシナモンパンを二人とも実食し、次はクッキーへ進む。駅の古い手帖を見に行く既存goalは残るが、駅へのmovement追加なし。Iris=Viola=`cafe_fleur`を維持。
- #381終了時も`movements`配列は8件。44周目の新規movement・raw location変更は0件。

### #381終了時の全住民raw location

- Mimosa=`eternite_square`
- Iris=`cafe_fleur`
- Erica=`cafe_fleur`
- Anemone=`hanasaku_station`
- Daphne=`cafe_fleur`
- Campanula=`time_bell_tower`
- Nerine=`flower_slumber_garden`
- Viola=`cafe_fleur`
- Lupinus=`stellaris_hill`

会話上の出発・移動意図・入店・同席・飲食と、raw `characters[].location` / `movements`を自動同一視しない。


## #385・#386後のユーザー提供raw照合（2026-09-01記録）

- 情報源は本WORKチャットの提供JSON。Cloud Browser実測ではない。
- 9人のlocationと72方向のaffinityは両スナップショット間で同一。Daphne↔Anemone、Iris↔Violaは100/100。
- movementsは8件のまま。最新は2026-08-17T06:37:34のAnemone flower_slumber_garden→hanasaku_station。
- #386の庭での着席・実食は会話上の描写。raw Daphne=cafe_fleur、Anemone=hanasaku_stationを変更しない。
- 詳細：[45周目正本](elysion_observation/45_round45_382.md)。


## 2026-09-04 照合（#389後）
- raw movements=8、追加なし。9人のraw locationも不変。
- 会話上の花眠りの庭への到着・着席、温室の描写はraw movement/locationへ逆輸入しない。

## 2026-09-07 照合（#390後）
- raw movements=8、追加なし。9人のraw locationも不変。
- Iris×Violaが学院の温室へ向かう描写は会話上の進行であり、rawでは両者ともcafe_fleur。movement/locationへ逆輸入しない。


## 2026-09-08 照合（#391後）
- raw movements=8、追加なし。9人のraw locationも不変。
- Iris×Violaは会話上、学院の温室へ続く小道を進み光へ近づいたが、rawでは両者ともcafe_fleur。movement/locationへ逆輸入しない。

## 2026-09-10 照合（#392後）
- raw movements=8、追加なし。9人のraw locationも不変。
- Iris×Violaは会話上、学院の温室内へ到着したが、rawでは両者ともcafe_fleur。movement/locationへ逆輸入しない。

## 2026-09-11 照合（#393後）
- raw movements=8、追加なし。9人のraw locationも不変。
- Iris×Violaは会話上、学院の温室内で光とパンの香りを感じているが、rawでは両者ともcafe_fleur。movement/locationへ逆輸入しない。


## 2026-09-12 照合（#394後）
- raw movements=8、追加なし。9人のraw locationも不変。
- Daphne×Anemoneは会話上、花眠りの庭で夜空を見上げているが、rawではDaphne=cafe_fleur、Anemone=hanasaku_station。movement/locationへ逆輸入しない。


## 2026-10-01 UTC／2026-10-02 JST 照合（#395後）
- raw movements=8、追加なし。全9人のraw locationも不変。最新movementは2026-08-17T06:37:34のAnemone flower_slumber_garden→hanasaku_station。
- Iris×Violaは会話上、温室の光の奥へ進み外の街灯に気づいたが、rawでは両者ともcafe_fleur。新規sceneのraw locationもcafe_fleur。
- 街灯や列車のscene / pendingを住民自身のmovementやlocationへ逆輸入しない。

## 2026-10-02 JST 照合（#396・#397後）
- raw movements=8、追加なし。全9人のraw locationは開始前・#396後・#397最終rawで不変。
- #396は温室の光の中心へ進み「物語の扉」が開こうとする会話描写。rawではIris=Viola=cafe_fleur。比喩的な扉や歩みを新しいmovement／到着にしない。
- #397は肩を寄せ街灯の光を感じるが、rawではDaphne=cafe_fleur、Anemone=hanasaku_station、scene.location=null。同席の叙述やsceneを移動根拠へ補完しない。

## 2026-10-03 JST・#399後
- 開始前、#398後、#399後の全9人raw locationとmovements8は不変。
- Erica=cafe_fleur、Nerine=flower_slumber_garden、Lupinus=stellaris_hill、Viola=cafe_fleur。
- #399の旅の空想や駅の列車音は移動・乗車・対面の根拠ではない。新sceneのraw location=nullを補完しない。

## 2026-10-04 JST 照合（#400〜#405）
- 全9人raw location・movements8は開始前から不変。mimosa=eternite_square、iris=cafe_fleur、erica=cafe_fleur、anemone=hanasaku_station、daphne=cafe_fleur、campanula=time_bell_tower、nerine=flower_slumber_garden、viola=cafe_fleur、lupinus=stellaris_hill。
- 夢での待ち合わせ、遠い列車音、カフェ・木々の描写は会話文脈として記録。既存raw位置との差を勝手に同期せず、描写だけから移動成功・新しいmovementを認定しない。

## 2026-10-05 JST 追補（#406〜#411）
- weather=2026-10-05・曇り・24℃、scene累計151、events50（scene50 / moved0）、pending3、movements8、turns_since_event4、items / rumors / overheard=0 / 0 / 0。
- 全9人raw location・movements8は開始前から不変。mimosa=eternite_square、iris=cafe_fleur、erica=cafe_fleur、anemone=hanasaku_station、daphne=cafe_fleur、campanula=time_bell_tower、nerine=flower_slumber_garden、viola=cafe_fleur、lupinus=stellaris_hill。
- 今回の花の話は旧sceneの継続であり、新規world_eventではない。Mimosaのraw位置はeternite_square、Lupinusはstellaris_hillのまま。温室の方を見たという語りを温室への移動へ置き換えない。
- 歩いていく／光の渦へ溶け込むという物語上の歩行はあるが、目的地への明確な到着やraw movementはない。Iris=cafe_fleur、Campanula=time_bell_towerのまま。CampanulaがIrisを描写するnarrator/perspective bleedを保ち、本人の移動や新能力としない。
- 別れ後に互いへの応答が続く既存の挙動で、今回も明示再接続・再合流はない。視線を落とす・頷くという括弧内描写を同席の確定根拠にせず、Viola=cafe_fleur、Campanula=time_bell_towerのraw位置と分ける。
- Anemoneの駅の喧騒への一歩は、既存raw location=hanasaku_stationの範囲での描写。Campanulaはtime_bell_towerのままで、相手の背中・去った後の空気を描く視点には距離・同席の曖昧さがある。今回新しい移動成功やmovement未反映と断定しない。
- location / movements / pendingを手動変更していない。会話の比喩・視点・歩行と、raw移動成功／失敗を分けて記録する。

## 2026-10-06 JST 追補（#412〜#417）
- weather=2026-10-06・薄曇り・27℃、scene累計154、events50（scene50 / moved0）、pending3、movements8、turns_since_event3、items / rumors / overheard=0 / 0 / 0。
- 全9人raw location・movements8は開始前から不変。mimosa=eternite_square、iris=cafe_fleur、erica=cafe_fleur、anemone=hanasaku_station、daphne=cafe_fleur、campanula=time_bell_tower、nerine=flower_slumber_garden、viola=cafe_fleur、lupinus=stellaris_hill。
- #412の図書館での読書・席を立つ描写とDaphne=cafe_fleurの差は既存の文脈を保持。新しい移動成功や失敗と推定しない。
- #413は明日への祝福と別れの反復。出発・到着の描写なし。全location・movements不変。
- #414でEricaが湖のほとりへの到着を明示し、Mimosa名義叙述はシルヴェーヌ湖と呼ぶ。Erica=cafe_fleurとmovements8は不変で、会話上の到着とraw未反映の差を記録。Mimosa本人の到着や移動ツールの実行・失敗は推定しない。
- #415の繋いだ手・二人で眠る描写は旧#321から継続。Iris=cafe_fleurとNerine=flower_slumber_gardenは不変。同席・移動へ補完しない。
- #416は純粋な別れの反復。新しい歩行・到着・同席の描写はなく、location・movements不変。
- #417の温室・月明かりはsceneへの想像と伝聞を含む応答。Viola=cafe_fleur、Mimosa=eternite_squareのまま。温室への移動・同席を認定しない。
- location / movements / pendingを手動変更していない。会話上の描写とraw移動成功／失敗を分けて記録する。


## 2026-10-07 JST 照合（#423後）
- 全9人raw locationとmovements8は開始前・各組後・最終確認で不変。
- #418 新規world_event・移動・到着描写はない。両方向のaffinityが各2上昇しても、物語上の再開とは扱わない。
- #419 Irisは「もうカフェ・フルールの前にいたんだった」と場所を思い出し、「座ってみることにする」と意向を述べる。座った動作や着席完了はなく、新たな到着・goal完了とは数えない。
- #419 scene本文は温室のガラス越しの香りを述べるが、raw event.locationはcafe_fleur。Iris・Daphneのraw locationもcafe_fleurのまま。温室への移動成功や失敗を推測せず、本文・event位置・キャラクター位置を分けて保持する。
- #420 旧#224の別れに続き、「行ってきます」「いってらっしゃい」「また後で」を4発言で反復する。カフェでの再会を期待する言葉はあるが、到着・合流・新たな通話接続は描かれない。既存の終了分類を維持する。
- #421 夜の魔法・夢・雲のような言葉は比喩として扱う。新たな能力、同席の成立、移動・到着、具体的なgoal完了の根拠にはしない。
- #421 新規world_eventはなく、全9人raw location・movementsは変わらない。好感度上昇・通常生成の継続と物語上の接続状態を分けて記録する。
- #422 Anemoneが述べる駅のホームはraw location=hanasaku_stationと整合する。Violaのraw location=cafe_fleurは変わらず、本人は自分の場所の風は穏やかだと述べる。どちらも移動・到着・同席は描かれない。
- #422 world_event本文は温室の扉だがraw event.locationはnull。会話上の駅のホームやViolaのカフェ位置をevent.locationに補完しない。
- #423 新規world_eventなし、affinity100/100のまま、全9人raw location・movementsも不変。短い挨拶が続くことと、システム上の終了フラグは同一視しない。


## 2026-10-09 JST 照合（#429後）
- 全9人raw location・movements8は10月7日#423後の履歴rawと同じ。実行直前の完全rawは未取得。#424〜#429の各raw間も同じ。
- mimosa=eternite_square、iris=cafe_fleur、erica=cafe_fleur、anemone=hanasaku_station、daphne=cafe_fleur、campanula=time_bell_tower、nerine=flower_slumber_garden、viola=cafe_fleur、lupinus=stellaris_hill。
- #424 パンの香りを双方が受け取る表現があるが、Iris=cafe_fleur、Lupinus=stellaris_hillのまま。新たな到着・同席・知覚共有能力へ補完しない。明日の計画と、実際の来訪・飲食完了を区別する。
- #425 祈りや光の表現は願いや比喩として保存する。Nerineの「幸せな気持ちになれるわ」と「はずだよ」が混在する口調は原文のまま保持し、修正しない。新規scene・移動・到着描写はない。
- #426 Mimosaは「香りが漂ってきたような気」「想像しちゃう」と述べ、Nerineも「もしそうなら」と条件を付ける。通話越しに香りを共有できる公式能力や、実際にハーブティーを飲んだ事実にはしない。sceneのraw locationはnullで、Mimosa=eternite_square、Nerine=flower_slumber_gardenからカフェへの移動を補完しない。
- #427 話者はCampanula、Ericaの順で交互に4発言。新規scene・移動・到着描写はなく、短い別れの反復とシステム上の終了フラグを同一視しない。
- #428 互いの言葉で風や心が優しく温かく感じられるという応答が続く。新規scene・移動・到着描写はなく、相手を思い浮かべる表現を同席や新しい知覚共有能力として扱わない。
- #429 新規scene・移動・到着描写はない。生成された発言の継続と物語上の接続状態・システム上の終了フラグを同一視しない。
- location / movements / pendingは手動変更していない。比喩・意向・scene位置と実際の移動を区別する。
