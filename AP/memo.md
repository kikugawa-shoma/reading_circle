## NAPT
### Q
ネットワークの書籍を読むと
内部PCから外部へアクセスする際、送信元IPとポート番号がルーターのNATテーブルに保持され
その変換テーブルを元にして、PATにおけるIPとポートの変換が実現されるとあるのですが
いくつか疑問がありましたので質問させてください

(1)内部ネットワーク側から通信を開始したなら問題なく通信出来ると思いますが
外部サーバーから始まる通信だとNATテーブルに情報がないためプライベートIPとポートに変換出来ないのではないでしょうか？
その場合は、どういう技術や対象方法があるのでしょうか？

(2)例えば複数の内部PCからPATで外部へアクセスする場合
内部PCのポート番号は65535までのポートをランダムに使用することになると思います。
しかし、もし内部PCが使用するポートが重複してしまった場合はアクセス不能になってしまわないのですか？

つまり、外部サーバーから見ると、10.0.1.1:65535、10:0.1.1:65534のようにポート番号だけ変えてアクセスしてくるわけですし、もしポート番号が重複してしまうと変換出来ないと思います。

ポート番号はそれぞれのPCが独自に設定するものなので重複することもありえると思うのですがどのように処理されているのでしょうか？

### A

>(1)内部ネットワーク側から通信を開始したなら問題なく通信出来ると思いますが
>外部サーバーから始まる通信だとNATテーブルに情報がないためプライベートIPとポートに変換出来ないのではないでしょうか？
>その場合は、どういう技術や対象方法があるのでしょうか？

はい。変換できませんので通信不可です。
対策としてはポートフォワーディングとか言われるものになりますね。
ルータのメーカによって、微妙に呼び方が変わります。
「ポート解放」「ポート転送」「仮想サーバ」等々……。
ルータのWAN側に届いたパケットを事前に設定したLAN側IPの特定のポートに転送します。
TCPならこの後内部テーブルに「接続済み」などのステータスとともに状態を持ち続けるでしょう。
で、ポートフォワーディングの設定はルータの方に静的に設定する場合と、UPnPで動的に変更を受け付ける場合があります。
さらに、DMZとして全ポートのパケットを転送する。という設定もあります。

>(2)例えば複数の内部PCからPATで外部へアクセスする場合
>内部PCのポート番号は65535までのポートをランダムに使用することになると思います。
>しかし、もし内部PCが使用するポートが重複してしまった場合はアクセス不能になってしまわないのですか？

ルータはクライアント側のIPアドレスとポート番号をセットで保持しています。

PC-A(192.168.1.1)とPC-B(192.168.1.2)が外部の同じポート(80番)にアクセスした場合の状態を見ると……
PC-A(送信元ポート33333)=>ルータのLAN側(送信元ポート33333)=ルータのWAN側(送信元ポート12345)=>サーバ
PC-B(送信元ポート33333)=>ルータのLAN側(送信元ポート33333)=ルータのWAN側(送信元ポート12346)=>サーバ
というような変換を行います。
ルータはクライアント側のIPアドレスと送信元ポートのセットで記憶していますので、サーバ側からの送信先ポート12346のパケットはPC-Bへ送信先ポート33333に書き換えて転送します。
同様にサーバ側からのサーバ側からの送信先ポート12345のパケットはPC-Aへ送信先ポート33333に書き換えて転送します。


## B木
- https://qiita.com/higuo/items/c4d6629d28725118bc2d