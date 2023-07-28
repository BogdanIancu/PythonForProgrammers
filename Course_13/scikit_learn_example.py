import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
import joblib


# movie_data = pd.read_csv("data.csv")
# print(movie_data.info)
# print(movie_data.describe())
#
# ages = movie_data['age']
# plt.hist(ages, bins=10, edgecolor='black', color='blue')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.title('Distribution of Ages')
# plt.show()

# mean_age = np.mean(ages)
# std_age = np.std(ages)
# plt.hist(ages, bins=10, edgecolor='black', color='blue', density=True, alpha=0.7)
# x = np.linspace(min(ages), max(ages), 100)
# y = norm.pdf(x, mean_age, std_age)
# plt.plot(x, y, 'r--', label='Gaussian Distribution')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.title('Distribution of Ages with Gaussian Distribution')
# plt.legend()
# plt.show()

# movie_data = pd.read_csv("data.csv")
# cleared_data = movie_data[movie_data['IMDB_rating'] >= 6.5]
#
# cleared_data.to_csv('cleared_data.csv', index=False)

# movie_data = pd.read_csv("cleared_data.csv")
# # We will use a supervised learning algorithm (called Decision Tree)
#
# # X is the input
# X = movie_data.drop(columns=["movie_name"])
# # Y is the output or the predicted data
# y = movie_data["movie_name"]
#
# model = DecisionTreeClassifier()
# model.fit(X.values, y.values)
# predictions = model.predict([[35, 1, 17, 8], [25, 0, 19, 9]])
# print(predictions)

# movie_data = pd.read_csv("cleared_data.csv")
#
# X = movie_data.drop(columns=["movie_name"])
# y = movie_data["movie_name"]
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#
# model = DecisionTreeClassifier()
# model.fit(X_train.values, y_train)
# predictions = model.predict(X_test.values)
# score = accuracy_score(y_test, predictions)
# print("Accuracy:", score)
# score = f1_score(y_test, predictions, average="weighted")
# print("F1 score:", score)
# joblib.dump(model, "movie_recommender.joblib")

model = joblib.load("movie_recommender.joblib")
predictions = model.predict([[42, 1, 17, 8], [25, 0, 19, 9]])
print(predictions)

tree.export_graphviz(model, "movie_recommender.dot", feature_names=["age", "gender", "hour", "IMDB_rating"],
                     label="all", rounded=True, filled=True)

