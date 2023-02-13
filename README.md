# 行列でモンティ・ホール問題を解く。

<!-- Time-stamp: "2023-02-13T19:35:38Z" -->

中平健治『図式と操作的確率論による量子論』(森北出版, 2022年10月)を読ん
だことを↓で書いた。

《中平健治『図式と操作的確率論による量子論』を読んだ。わかった気にさせ
てくれるよい本だった。モンティ・ホール問題をプロセスでどう表現するか？
機械学習のパーセプトロン的なものが必要では？…とか考えた。 - JRF のひ
とこと》
http://jrf.cocolog-nifty.com/statuses/2023/02/post-202817.html

そこでモンティ・ホール問題をプロセスとして行列的に書くのに、私はパーセ
プトロン的枠組みが必要でないかと考えた。

しかしこの本の補遺が↓にあるが、その『図式で学ぶ量子論』にモンティ・ホー
ル問題が載っていて、行列で解けるという書きぶりである。

《図式と操作的確率論による量子論｜森北出版株式会社》  
https://www.morikita.co.jp/books/mid/017061

私は驚いて「単純な行列ではダメだと思うのだが、著者がここで間違えるはず
がないから、方法はあるのかもしれない。ぜひ教えていただきたい。」と書い
たところ、なんと、著者から Twitter で反応があって、行列での表し方を教
わった。

その検算を行ったのがこの GitHub の Python コードになる。

私がまだ間違っている可能性もあるが、中平氏の示した行列だとうまくいかず、
少し変更する必要があったものの、うまく行列で表すことができたのだった。


## 内容

 * matrix_monty_hall_1.py - 私のパーセプトロンのアイデアによる実装。

 * matrix_monty_hall_2.py - 中平氏の Twitter でのアイデアによる実装。

 * matrix_monty_hall_3.py - 中平氏の『図式で学ぶ量子論』による実装。


## Author

JRF ( http://jrf.cocolog-nifty.com/statuses )


## License

Public Domain.

…でいいのですが、Public Domain が通用しないなら、

MIT License.

…とします。
