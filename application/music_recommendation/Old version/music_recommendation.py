import pandas as pd
import numpy as np
from sklearn import svm, tree
from sklearn.externals import joblib

train_df = pd.read_csv('train.csv', header=0, iterator=True)
# song_df = pd.read_csv('songs.csv', header=0)[['song_id', 'genre_ids', 'artist_name',
#                                               'composer', 'lyricist', 'language']]
song_df = pd.read_csv('songs.csv', header=0)[['song_id', 'genre_ids', 'language']]
user_df = pd.read_csv('members.csv', header = 0)[['msno', 'city', 'bd', 'gender']]

temp = pd.merge(train_df.get_chunk(100000)[['msno', 'song_id', 'target']], song_df, on='song_id')
features = pd.merge(temp, user_df, on='msno').drop(columns=['msno','song_id', 'gender'])

features['genre_ids'] = features['genre_ids'].fillna(value='0')
# features['artist_name'] = features['artist_name'].fillna(value='')
# features['composer'] = features['composer'].fillna(value='')
# features['lyricist'] = features['lyricist'].fillna(value='')
features['language'] = features['language'].fillna(value=0.0)
features['city'] = features['city'].fillna(value=0)
features['bd'] = features['bd'].fillna(value=0)

print(features.head(10))
features = features[~features.genre_ids.str.contains('\\|')]
# features = features.convert_objects(convert_numeric=True)

# features['gender'] = features['gender'].fillna(value='')
print(features.head(20))
features = features.as_matrix()

clf = tree.DecisionTreeClassifier()
X = features[:,1:]
y = features[:,0].astype('int')
clf.fit(X, y)

joblib.dump(clf, 'classifier.pkl')