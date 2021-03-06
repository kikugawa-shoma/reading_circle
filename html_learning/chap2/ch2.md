# chapter 2 HTML の基本

## 1.HTML とは？

- <strong>H</strong>yper <strong>T</strong>ext <strong>M</strong>arkup <strong>L</strong>anguage
  - Hyper Text ：文書と文書を関連付ける仕組み。いわゆるリンク
  - Markup Language：普通のテキストは文字列のみ。
    マークアップ言語は文字列に文書の構造上の
    意味を与えるための言語
- タグを使って文書構造上の役割を文字列へ指定する

## 2.HTML ファイルの作り方

- エディタで書いてブラウザで開く
- ファイル名の規則
  - 拡張子をつける。.html
  - 半角英数、ハイフン、アンダーバーのみ
  - 基本的に小文字？
  - トップページのファイルの名前は index.html
    (ドメイン名だけでアクセスできるため)

## 3.HTML ファイルの骨組み

とても簡素なページの例

```html

<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
	<title>ホームページのタイトル<title>
	<meta name="description" content="ホームページの説明">
  </head>
  <body>
	  本体部分
	  表示される部分
  </body>
</html>
```

上の html をブラウザで開くと、、、

- `<!DOCTYPE html>` : ドクタイプ宣言。html のバージョンを宣言
- `<html></html>` : ドクタイプ宣言の直後に置く。html の文書であることを
  表す。lang 属性で言語を指定
- `<head></head>` : 本文には表示されないページの
  メタ情報を記述していく部分
  - `<meta charset="utf-8">` : ファイルの文字コードを指定
  - `<meta name="description" content="~~~">` :
    ページについての説明文を書く。検索エンジンでタイトルと共に表示される。
  - `<title></title>` : ページのタイトルを書く
- `<body>~~~</body>` : 本体部分。ページに表示される。ここにコンテンツ
  を作成していく。

## 4. HTML の基本の書き方

### 3 通りのタグ

タグの基本形：`<tagname>hogehoge</tagname>`

1. 終了タグが必ず必要なもの (例)`<ul>`、`<h1>`
1. 終了タグを省略できるもの (例)`<li>`、`<th>`、`<tr>`<br>
   次のタグが始まると自動でブラウザが終了タグを補完する
1. 終了タグがないもの。void 要素と呼ばれる (例)`<br>`、`<img>`、

開始タグと終了タグで囲まれた
(必ずしも開始タグと終了タグが存在するわけではないがそこには目をつぶって)
ものを要素(element)という。

---

実は開始タグと終了タグの両方を省略できるものもある（ブラウザ側が補完してくれる）

(例)`<html>`、`<head>`、`<body>`

(HTML のバージョンが進むごとに省略できるものが増えてきたらしい)

---

### タグを書くときのルール

- 半角英数字
- 大文字小文字は区別しない（ただし小文字統一が推奨）
- 入れ子の終了タグの順番に注意。要素は包含関係になくてはならない
- タグに付加情報を加えられる。属性を使う。属性値はダブルクオテーションで囲む<br>
  `<tagname attr="value">hogehoge<tagname>`

## 5~12

html で書いたので別ファイル

## 13.ブロック要素でグループ分け

以下のタグは html だけではブラウザ上の表示は変わらない。

CSS と合わせて使う際に効果を発揮する

なぜなら同じグループのものには同じような装飾を施す（ことが多い）ため、
グループで区切っているとまとめてセレクタで捕捉できるから

- `<header>` : ページ上部のヘッダー
- `<nav>` : ナビゲーションメニュー
- `<article>` : 読み物、記事
- `<section>` : テーマを持ったグループ
- `<main>` : ページのメインコンテンツ
- `<aside>` : メインではない補足情報
- `<footer>` : ページ下部のフッター
- `<div>` : 意味を持たないグループ要素

迷ったら div でいい説

## Appx. インライン要素とブロックレベル要素

- [HTML5 ではインライン要素とブロック要素は廃止](https://www.tohoho-web.com/html/memo/elem.htm)
- その代わり[カテゴリとコンテンツモデル](https://programmercollege.jp/column/1927/)と言う概念を採用
- HTML5 より前は「ブロックレベル要素には
  ブロックレベル要素とインライン要素を内包でき、
  インライン要素には無理」というルールだった

## 疑問点
- チェックボックスで送られる値
- メールリンクに件名とか本文とか自動でいれられるようにするには？
- div以外のブロック要素の個数制限