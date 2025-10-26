import pickle
import numpy as np

# Models classifer
from sklearn.ensemble import RandomForestClassifier
# Funcrion to train model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


data_dict = pickle.load(open("./data_new.pickle", "rb"))

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

#split the data into training and testing sets
x_train , x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)
# define the model
model = RandomForestClassifier()
from sklearn.model_selection import RandomizedSearchCV

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30, None],
    'max_features': ['sqrt', 'log2'],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
search = RandomizedSearchCV(model, param_grid, n_iter=20, cv=5, n_jobs=-1)

#input the data to the model
search.fit(x_train, y_train)
# model.fit(x_train, y_train)

# make predictions
y_predicted = search.predict(x_test)
# calculate the accuracy
accuracy = accuracy_score(y_predicted, y_test)
print('Accuracy: {}%'.format(accuracy * 100))


f = open('model_new.p', 'wb')
pickle.dump({'model': search}, f)
f.close()
print("Model trained and saved to model.p")
# print(data_dict.keys())
# print(data_dict)
