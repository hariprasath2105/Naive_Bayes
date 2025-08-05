import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
column_names = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
df = pd.read_csv('iris.data', header=None, names=column_names)

le = LabelEncoder()
df['Species'] = le.fit_transform(df['Species'])

X = df[['PetalLength', 'PetalWidth']]
y = df['Species']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = GaussianNB()
model.fit(X_train, y_train)

# Save model and label encoder
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(le, f)

