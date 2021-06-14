import twint
import nest_asyncio
import os
import pandas as pd

nest_asyncio.apply()
dir = os.getcwd()
# Configure for apziva's request
t = twint.Config()
t.Search = "\"request for startup\""
t.Limit=200
t.Store_csv = True
#crop csv file for better visualization
t.Output = dir+"\\dl.csv"
twint.run.Search(t)
df = pd.read_csv(dir+"\\dl.csv")
temp = df[['date','time','username','name','tweet','replies_count','likes_count']]
temp.to_csv(dir+"\\UI\\data\\tweets.csv",index=False)
os.remove(dir+"\\dl.csv")


