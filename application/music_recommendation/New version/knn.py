from __init__ import *


class KNN:
    def __init__(self, u2s, s2u):
        self.u2s = u2s
        self.s2u = s2u

    def get_neighbour_ranking(self, user):
        table = []
        users_set = set()
        songs = self.u2s[user][1]
        for s in songs:
            # for item in self.s2u[s]:
            users_set = users_set.union(set(self.s2u[s]))
        users = list(users_set)

        print("wait")
        for u in users:
            tmp = list()
            for s in songs:
                if s in self.u2s[u][1]:
                    tmp.append(self.u2s[u][0])
                else:
                    tmp.append(0)
            if u == user:
                user_scores = tmp
                continue
            table.append([u, tmp])
        distance_table = []
        for i in range(len(table)):
            distance_table.append((table[i][0], self.get_distance(user_scores, table[i][1])))
        best = sorted(distance_table, key=lambda x: x[1], reverse=False)
        return best
        # print("wait")


    @staticmethod
    def get_distance(x, y):
        result = 0
        for i in range(len(x)):
            result += pow((x[i] - y[i]), 2)
        return result


with open(SONG2USERS, 'rb') as handle:
    song2users = pickle.load(handle)

with open(USER2SONGS, 'rb') as handle:
    user2songs = pickle.load(handle)

test_user = "Xumu+NIjS6QYVxDS4/t3SawvJ7viT9hPKXmf0RtLNx8="
algo = KNN(user2songs, song2users)
neighbour_rank = algo.get_neighbour_ranking(test_user)
min_n = min(10, len(neighbour_rank))
recommend_num =10
print(neighbour_rank)

for x in range(min_n):
    neighbour = user2songs[neighbour_rank[x][0]]
    for x in neighbour[1]:
        if test_user not in song2users[x]:
            print(x)
            recommend_num-=1
            if recommend_num<=0:
                print("Output ends")
                exit()

