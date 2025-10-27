import pickle
import numpy as np
import matplotlib.pyplot as plt

# Models classifer
from sklearn.ensemble import RandomForestClassifier
# Funcrion to train model
from sklearn.model_selection import train_test_split

# Function to evaluate F1 Score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix , ConfusionMatrixDisplay
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

pickle_in = open('model.p', 'rb')
model_dict = pickle.load(pickle_in)
model = model_dict['model']
data_dict = pickle.load(open("./data.pickle", "rb"))
test_dict = pickle.load(open("./data_testset.pickle", "rb"))
test_data = np.asarray(test_dict['data'])
test_labels = np.asarray(test_dict['labels'])
data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])
#split the data into training and testing sets
x_train , x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

y_predicted = model.predict(test_data)
Accuracy = accuracy_score(y_predicted, test_labels)
print('Accuracy from prediction with test dataset: {}%'.format(Accuracy * 100))

display_labels = np.unique(labels)
# print("Labels:", display_labels)
# print(model.best_params_)
# Confusion Matrix
cf_matrix = confusion_matrix(y_true=test_labels, y_pred=y_predicted,labels=display_labels)
cf_matrix_display = ConfusionMatrixDisplay(confusion_matrix=cf_matrix, display_labels=display_labels)
cf_matrix_display.plot()
plt.title('Confusion Matrix')

# Precision
precision = precision_score(y_true=test_labels, y_pred=y_predicted,labels=display_labels, average='weighted')
print('Precision of model: ', precision)

# # Recall
recall = recall_score(y_true=test_labels, y_pred=y_predicted,labels=display_labels, average='weighted')
print('Recall of model: ', recall)

# # F1
f1_score = f1_score(y_true=test_labels, y_pred=y_predicted,labels=display_labels, average='weighted')
print('F1 Score of model: ', f1_score)

plt.show()