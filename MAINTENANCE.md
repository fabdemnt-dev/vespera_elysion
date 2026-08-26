# Markdownファイルの保守・分割方針

## 対象

観察記録本体は[`elysion_observation/`](elysion_observation/)で周別ファイルに分割済みです（分割前は単一ファイルが肥大化し、読みにくくなったための対応）。

それ以外のルート直下のMarkdownファイル（`elysion_events.md` / `elysion_movements.md` / `elysion_newspapers.md` / `elysion_official_settings.md` / `elysion_official_settings_changelog.md` / `elysion_observed_daily_life.md` / `elysion_affinity.md`）にも、同じ問題が将来起きないよう次の基準を適用します。

## 肥大化しきい値

1ファイルが概ね**200KB**を超えたら分割を検討します。

2026-08-25時点で最大の`elysion_events.md`は約60KBのため、当面は分割不要です。

## 分割方法

`elysion_observation/`と同じ考え方で、対象ファイル名と同じ名前のサブフォルダ（例：`elysion_events/`）を作り、日付や周（round）単位でファイルを分けます。サブフォルダ内の`README.md`で一覧・運用ルールを明文化します。

## 分割時に守ること

- 完結済みの過去分は編集しない。
- 本文（会話記録・観察内容）は変更せず、移動のみ行う。
- 旧ファイルは分割後に削除し、リンクを更新する。
- HTML側の閲覧レイヤーは変更しない。

## 実施手順

分割が必要になった時点で、対象ファイルごとに`elysion_observation`移行時と同様の手順で対応します。

1. 内容を照合する。
2. フォルダを作成する。
3. `README.md`を作成する。
4. 旧ファイルを削除する。
5. リンクを更新する。
6. 一連の変更を1コミットにまとめる。
