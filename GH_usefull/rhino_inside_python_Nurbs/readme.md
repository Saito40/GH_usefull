# Rhino Inside python

このコードでは、Rhino Inside Pythonを使ってNurbsカーブを描いています。

## やった内容
まず、origin.3dmのNurbsカーブデータからPoint、Weigth、KnotsのデータをGHで取り出し、PWK.csvに保存します。\
次に、pythonでデータ読み込み、Nurbsカーブの構成、Nurbsカーブから逐次的に座標の構成、xy.csvに出力しています。\
最後にpythonの別環境でmatplotlibのグラフを出します。

## 参考
Steve Baer
 : [Rhino Inside Python](https://discourse.mcneel.com/t/rhino-inside-python/78987)\
Hiroaki Saito : [GH C#_Divide Distance With List](https://openddl.com/post/166/)
