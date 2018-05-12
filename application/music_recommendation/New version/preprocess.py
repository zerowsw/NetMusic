from __init__ import *

# some notes, 52 may be English; 3 may be Chinese; -1 may be Japanese

# df = pd.read_csv(SONG_FILE_ORIGIN)
# df_en = df.loc[df['language'] == 52.0].fillna("").head(10000)
# df_en.to_pickle("train")

df = pd.read_csv(TRAIN_FILE_ORIGIN)
df = df.head(1000000).loc[df['target'] == 1].fillna("")
df = df[['msno','song_id']]
df.to_pickle(TRAIN_FILE)

# We define 2 structures here, one is user-> songs-> rating; another is song-> users

print("hello")
