# vespera_elysion

UNIVERSEエディタを使って作成した「エリュシオン」という街の観察記録です。

## 内容

- 会話記録(織り手・新聞記者による生成)
- 世界記録・出来事
- 公式設定
- 新聞記事

## 利用方法

GitHub Pagesで公開しているページを開き、観察記録を閲覧できます。

## Markdownファイルの肥大化しきい値・分割方針

観察記録本体は[`elysion_observation/`](elysion_observation/)で周別ファイルに分割済みです（分割前は単一ファイルが肥大化し読みにくくなったための対応）。それ以外のルート直下のMarkdownファイル（`elysion_events.md` / `elysion_movements.md` / `elysion_newspapers.md` / `elysion_official_settings.md` / `elysion_official_settings_changelog.md` / `elysion_observed_daily_life.md` / `elysion_affinity.md`）にも、同じ問題が将来起きないよう次の基準を適用します。

- **しきい値**：1ファイルが概ね**200KB**を超えたら分割を検討する（2026-08-25時点で最大の`elysion_events.md`は約60KBのため、当面は分割不要）。
- **分割方法**：`elysion_observation/`と同じ考え方で、対象ファイル名と同じ名前のサブフォルダ（例：`elysion_events/`）を作り、日付や周（round）単位でファイルを分け、`README.md`で一覧・運用ルールを明文化する。
- **分割時に守ること**：完結済みの過去分は編集しない、本文（会話記録・観察内容）は変更せず移動のみ、旧ファイルは分割後に削除しリンクを更新する、HTML側の閲覧レイヤーは変更しない。
- 分割が必要になった時点で、対象ファイルごとに`elysion_observation`移行時と同様の手順（照合→フォルダ作成→README作成→旧ファイル削除→リンク更新→1コミット）で対応する。

## 注意

このリポジトリは個人利用を目的としています。コードやコンテンツの無断転載・再配布はご遠慮ください。
