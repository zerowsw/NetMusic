from sklearn.externals import joblib

clf = joblib.load('classifier.pkl')
# [genre_id, language, city, age]
print(clf.predict([[1000, 12.0, 13, 55]]))
