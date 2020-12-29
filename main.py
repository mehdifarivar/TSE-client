import os
import pandas as pd

path = os.getcwd()


def get_all(path):
    path = os.listdir(path + '\data')
    return path


print(get_all(path))
i = 1
for file in get_all(path):

    df = pd.read_excel(path + '/data/' + file)
    price = df['<CLOSE>'].values.tolist()
    print(file)

    Output = [sum(price[i:i + 13]) / 13
              for i in range(len(price) - 13 + 1)]
    for i in range(12):
        Output.insert(0, 0)

    df['MA13'] = Output
    df.to_excel(path + '/data/' + file, index=False)
