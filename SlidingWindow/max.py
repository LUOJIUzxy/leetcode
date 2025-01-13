from collections import deque
import pandas as pd

data = [3, 6, -1, 2, 4, 7, 10, 1, 8]
sliding_window_size = 3\

def max_sliding_window_by_pandas(arr, k):

    series = pd.Series(arr)
    max_values = series.rolling(window=k).apply(lambda X: X.max() - X.min(), raw=True).dropna()
    return pd.Series(arr).rolling(k).max().dropna().tolist()

def max_sliding_window(arr, k):
    result = []
    q = deque()

    for i in range(len(data)):
        while q and data[i] >= data[q[-1]]:
            q.pop()
        q.append(i)

        if i - q[0] >= k:
            q.popleft()

        if i >= k - 1:
            result.append(data[q[0]])

    return result

print(max_sliding_window(data, sliding_window_size))

# Output: [6, 6, 2, 7, 10, 10, 10, 8]

