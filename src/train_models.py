import pickle
import numpy as np

# Models classifer
from sklearn.ensemble import RandomForestClassifier
# Funcrion to train model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data_dict = pickle.load(open("./data_75pics.pickle", "rb"))

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

#split the data into training and testing sets
x_train , x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)
# define the model
model = RandomForestClassifier()
#input the data to the model
model.fit(x_train, y_train)

# make predictions
y_predicted = model.predict(x_test)
# calculate the accuracy
accuracy = accuracy_score(y_predicted, y_test)
print('Accuracy: {}%'.format(accuracy * 100))

f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
print("Model trained and saved to model.p")
# print(data_dict.keys())
# print(data_dict)