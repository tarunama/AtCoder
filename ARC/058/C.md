# 問題
http://arc058.contest.atcoder.jp/tasks/arc058_a

# なぜ解けなかったか
数Nに、数列Kの各要素が含まれるかの判定が書けなかった

# どうすればよいのか
それぞれをsetにして、NにKの各要素が含まれるか判定すればよかった。
```python
N_str = str(N)
is_include = set(N_str) & set(K)
```
