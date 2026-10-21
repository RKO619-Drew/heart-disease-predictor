import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# 1. Load the dataset
heart_data = pd.read_csv('heart_disease_data.csv')

# 2. Separate features and target
X = heart_data.drop(columns=['target'])
Y = heart_data['target']

# 3. Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, stratify=Y, random_state=2
)

# 4. Train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

# 5. Save the trained model
with open('heart_disease_model.sav', 'wb') as file:
    pickle.dump(model, file)

print("Model successfully trained and saved as 'heart_disease_model.sav'!")