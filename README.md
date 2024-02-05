## Model 1
# The first model is a basic implementation of a machine learning model using the Breast Cancer Wisconsin (Diagnostic) dataset. It uses the Logistic Regression algorithm from the scikit-learn library in Python. The model first loads the dataset, preprocesses the data, splits it into a training set and a test set, trains the Logistic Regression model on the training data, makes predictions on the test data, and then prints the accuracy of the model. This model does not include any hyperparameter tuning or use of pipelines.

## Model 2
# The second model is an updated and more compact version of the first model. This model uses a pipeline to streamline the preprocessing and modeling process. It also uses GridSearchCV for hyperparameter tuning which can potentially improve the model’s accuracy by finding the best hyperparameters for the model. Using both the pipeline and GridSearchCV makes this model more compact than the first one. 
