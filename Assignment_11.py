import pandas as pd
import numpy as np
data = np.random.randint(10, size=10)
series = pd.Series(data)
print("original series: ", series)
print(f"\nFirst item: {series[0]}")
print(f"Fifth item: {series[4]}")
filtered = series[series > 5]
print("\n Numbers > 5")
print(filtered)

# 4. Statistical Operations
print("\n--- Statistics ---")
print(f"Mean:{series.mean()}")
print(f"Median:{series.median()}")
print(f"Minimum:{series.min()}")
print(f"Maximum:{series.max()}")
Output :
original series:  0    5
1    5
2    6
3    5
4    1
5    0
6    2
7    2
8    5
9    4
dtype: int32

First item: 5
Fifth item: 1

--- Numbers > 5 ---
2    6
dtype: int32

--- Statistics ---
Mean (Average): 3.5
Median:         4.5
Minimum:        0
Maximum:        6
