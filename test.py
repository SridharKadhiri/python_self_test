import pandas as pd
df = pd.read_csv("txt.txt",sep = '\t')
print("\n"*2)
print(df.sample().iloc[0][0])