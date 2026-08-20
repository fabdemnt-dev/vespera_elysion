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

- 日付：2026-08-17（時刻は共有記録で未確認）
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
