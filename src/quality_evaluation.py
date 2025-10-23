import seaborn as sns
import numpy as np
from train_models import x_train, x_test, y_train, y_test, y_predicted, labels, model

# Function to evaluate F1 Score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

# Function for Confusion Matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

classes = np.unique(labels)

# คำนวณ Confusion Matrix
cm = confusion_matrix(y_test, y_predicted, labels=classes)# แสดงเป็นกราฟ

plt.figure(figsize=(10, 8))
sns.heatmap(cm,
            annot=True,              # แสดงตัวเลขในช่อง
            fmt='d',                 # รูปแบบตัวเลข: d = integer
            cmap='Blues',            # โทนสี (เลือกได้ เช่น 'YlGnBu', 'coolwarm', 'magma')
            xticklabels=classes,     # ชื่อคลาสในแนวแกน X
            yticklabels=classes)     # ชื่อคลาสในแนวแกน Y

plt.title("Confusion Matrix (Heatmap)", fontsize=18, pad=20)
plt.xlabel("Predicted Label", fontsize=14)
plt.ylabel("True Label", fontsize=14)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()



# Accuracy Score
# Accuracy on training data
x_train_prediction = model.predict(x_train)
training_data_accuracy = accuracy_score(y_train, x_train_prediction)
print('Accuracy on Training data : ', round(training_data_accuracy*100,2),'%')
# Accuracy on test data
x_test_prediction = model.predict(x_test)
test_data_accuracy = accuracy_score(y_test,x_test_prediction)
print('Accuracy on Test data : ', round(test_data_accuracy*100,2),'%')

# Precision
# precision for training data predictions
precision_train = precision_score(y_train, x_train_prediction, average='weighted')
print('Training data Precision = ', precision_train)
# precision for test data predictions
precision_test = precision_score(y_test, x_test_prediction, average='weighted')
print('Test data Precision = ', precision_test)

# Recall
# recall for training data predictions
recall_train = recall_score(y_train, x_train_prediction, average='weighted')
print('Training data Recall = ', recall_train)
# recall for test data predictions
recall_test = recall_score(y_test, x_test_prediction, average='weighted')
print('Test data Recall = ', recall_test)

# F1
# f1 score for training data predictions
f1_score_train = f1_score(y_train, x_train_prediction, average='weighted')
print('Training data F1 Score = ', f1_score_train)
# f1 score for test data predictions
f1_score_test = f1_score(y_test, x_test_prediction, average='weighted')
print('Test data F1 Score = ', f1_score_test)


# Precision Recall and F1 function
def precision_recall_f1_score(true_labels, pred_labels):
    precision_value = precision_score(true_labels, pred_labels, average='weighted')
    recall_value = recall_score(true_labels, pred_labels, average='weighted')
    f1_score_value = f1_score(true_labels, pred_labels, average='weighted')

    print('Precision =', precision_value)
    print('Recall =', recall_value)
    print('F1 Score =', f1_score_value)

print('---------- Classification metrics for training data ------------')
precision_recall_f1_score(y_train, x_train_prediction)

print('---------- Classification metrics for test data ----------------')
precision_recall_f1_score(y_test, x_test_prediction)

