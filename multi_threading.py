import pandas as pd
import threading

data = {
    "a": [3, 6, -1, 2, 4, 7, 10, 1, 8],
    "b": [2, 4, 6, 8, 10, 12, 14, 16, 18],
    "c": [1, 3, 5, 7, 9, 11, 13, 15, 17],
}
df = pd.DataFrame(data)

def calculate_column_mean(column, result_dict):
    print(f"Mean of column {column} is {df[column].mean()}")
    result_dict[column] = df[column].mean()

result_dict = {}

threads = []

for column in df.columns:
    thread = threading.Thread(targer=calculate_column_mean, args=(column, result_dict))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(result_dict)

    

