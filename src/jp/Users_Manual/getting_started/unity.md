# Unity版チュートリアル

Unity版のライブラリは座標系がz軸反転の左手系になり, 距離の基本単位がmになっているので注意すること.

## インストール (via GitHub)

Unity Package Manager経由でインストールする.

1. 「メニューバー」→「Window」→「Package Manager」を開く
1. 左上の「+」ボタンから, 「Add package from git URL」を選択する
1. `https://github.com/shinolab/AUTD3Sharp.git#upm/latest`を入力し, 「Add」をクリックする
    1. 特定のバージョンが必要な場合は, `#upm/vX.X.X`を指定する.

## インストール (via npm)

1. 「メニューバー」→「Edit」→「Project Settings」から「Package Manager」を開く
1. 「Scoped Registry」にて以下を追加し, 保存する
    - Name    : shinolab
    - URL     : https://registry.npmjs.com
    - Scope(s): com.shinolab
1. 「メニューバー」→「Window」→「Package Manager」を開く
1. 左上の「Packages」ドロップダウンメニューから, 「My Registries」を選択する 
1. `autd3-unity`パッケージをインストールする

> NOTE: npm経由でインストールする場合は, 最新のものがインストールされない可能性がある.
> 例えば, `v22.0.1-1`は`v22.0.1`よりも**新しい**. Version Historyを確認すること.

## Sample

Unity版はサンプルプログラムが付属しているので, そちらを参照されたい.
