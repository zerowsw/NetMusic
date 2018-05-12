from __init__ import *

df = pd.read_pickle(TRAIN_FILE)

df_user2songs = df.groupby("msno")
df_song2users = df.groupby("song_id")
# df_user2songs.to_pickle(USER2SONGS)
# df = pd.read_pickle(USER2SONGS)
# print(df_user2songs.first())
user2songs = {}
song2users = {}

# class User2Songs:
#     def __init__(self, name, group):
#         self.name = name
#         self.songs = group.values
#         self.avg_weight = float(1) / len(self.songs)

for name, group in df_user2songs:
    values = group['song_id']
    avg_weight = float(1)/values.size
    user2songs[name]=[avg_weight,values.tolist()]

for name, group in df_song2users:
    values = group['msno']
    song2users[name]=values.tolist()

with open(USER2SONGS, 'wb') as handle:
    pickle.dump(user2songs, handle)
with open(SONG2USERS, 'wb') as handle:
    pickle.dump(song2users,handle)

print("wait")
