import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load Iris dataset
df = sns.load_dataset("iris")
print("Sample Data:")
print(df.head())

# Step 2: Visualize the data
sns.pairplot(df, hue="species")
plt.title("Iris Flower Pairplot")
plt.show()

# Step 3: Split data into features (X) and labels (y)
X = df.drop("species", axis=1)  # features (sepal/petal length/width)
y = df["species"]              # labels (flower names)

# Step 4: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Step 5: Build and train the KNN model
model = KNeighborsClassifier()
model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = model.predict(X_test)

# Step 7: Evaluate performance
print("\n✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred))
# Step 8: Custom input for prediction
print("\n🔍 Predict species from your own input:")

try:
    sl = float(input("Enter sepal length (cm): "))
    sw = float(input("Enter sepal width (cm): "))
    pl = float(input("Enter petal length (cm): "))
    pw = float(input("Enter petal width (cm): "))

    sample = [[sl, sw, pl, pw]]
    prediction = model.predict(sample)
    print(f"\n🌼 Predicted species: {prediction[0]}")
except ValueError:
    print("❌ Invalid input! Please enter numbers only.")
