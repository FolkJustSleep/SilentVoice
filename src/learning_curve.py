import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import LearningCurveDisplay, ShuffleSplit
import pickle


data_dict = pickle.load(open("./data_new.pickle", "rb"))

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])


pickle_in = open('model_100pic.p', 'rb')
model_dict = pickle.load(pickle_in)
model = model_dict['model']
print("Total samples:", len(labels))
print("Unique labels:", len(np.unique(labels)))

fig, ax = plt.subplots(figsize=(6, 5))

common_params = {
    "X": data,
    "y": labels,
    "train_sizes": np.linspace(0.1, 1.0, 5),
    "cv": ShuffleSplit(n_splits=50, test_size=0.2, random_state=0),
    "score_type": "both",
    "n_jobs": 4,
    "line_kw": {"marker": "o"},
    "std_display_style": "fill_between",
    "score_name": "Accuracy",
}
print("Generating learning curves...")
LearningCurveDisplay.from_estimator(model, **common_params, ax=ax)
handles, label = ax.get_legend_handles_labels()
ax.legend(handles, ["Training Score", "Test Score"])
ax.set_title(f"Learning Curve for {model.__class__.__name__}")

plt.tight_layout()
plt.show()