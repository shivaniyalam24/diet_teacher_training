import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = {
    "score": [0, 40, 60, 80, 100],
    "level": ["Beginner", "Beginner", "Intermediate", "Advanced", "Advanced"]
}

df = pd.DataFrame(data)
X = df[["score"]]
y = df["level"]

model = DecisionTreeClassifier()
model.fit(X, y)

def get_recommendation(score):
    return model.predict([[score]])[0]
