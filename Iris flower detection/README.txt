
===========================================
Iris Flower Classification using KNN (Python)
===========================================

Description:
---------------
This is a machine learning project in Python using the Iris dataset. The model uses the **K-Nearest Neighbors (KNN)** algorithm to classify iris flowers into three species:
- Setosa
- Versicolor
- Virginica

It includes data visualization, model training, evaluation, and both manual and dataset-based prediction options.

Features:
------------
1. Load and preview the Iris dataset using seaborn.
2. Visualize data with pairplots.
3. Train a KNN classifier using scikit-learn.
4. Evaluate the model using accuracy and classification report.
5. Make predictions using:
   - Manual input
   - External CSV file input

How to Run:
--------------
1. Install required libraries (if not already installed):
   ```
   pip install pandas seaborn matplotlib scikit-learn
   ```

2. Save the Python code into a file, for example:
   ```
   iris_knn_classifier.py
   ```

3. Run the script:
   ```
   python iris_knn_classifier.py
   ```

4. Follow the on-screen instructions to enter:
   - Sepal/petal measurements manually
   - OR use a CSV file for bulk prediction (uncomment the CSV section in the code)

CSV Input Format:
---------------------
If using a CSV file for prediction, it should contain these column headers:
- sepal_length
- sepal_width
- petal_length
- petal_width

Example:

| sepal_length | sepal_width | petal_length | petal_width |
|--------------|-------------|--------------|-------------|
| 5.1          | 3.5         | 1.4          | 0.2         |
| 6.2          | 2.9         | 4.3          | 1.3         |

The predicted results will be saved in:
```
predicted_species.csv
```

Sample Usage:
-----------------

Enter sepal length (cm): 5.1
Enter sepal width (cm): 3.5
Enter petal length (cm): 1.4
Enter petal width (cm): 0.2

Predicted species: setosa
