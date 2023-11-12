import pandas as pd
s = pd.Series([1, 1, 1, 1, 2, 2, 2, 3, 3, 4])
s.count()
print(s.count())

s.sum()
print(s.sum())

s.cumsum()
print(s.cumsum())

s.value_counts(normalize=True)
print(s.value_counts(normalize=True))

s.min()
print(s.min())

s.max()
print(s.max())



