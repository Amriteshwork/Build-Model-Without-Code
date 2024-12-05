from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np

class LinearRegressionModel:
    def __init__(self):
        self.model = LinearRegression()
        self.metrics = {}
        
    def train(self, X, y, test_size=0.2, random_state=42):
        """Train the model and return performance metrics"""
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        
        # Train the model
        self.model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = self.model.predict(X_test)
        
        # Calculate metrics
        self.metrics = {
            'r2_score': r2_score(y_test, y_pred),
            'mse': mean_squared_error(y_test, y_pred),
            'rmse': np.sqrt(mean_squared_error(y_test, y_pred)),
            'mae': mean_absolute_error(y_test, y_pred)
        }
        
        return {
            'metrics': self.metrics,
            'coefficients': self.model.coef_,
            'intercept': self.model.intercept_
        }
        
    def predict(self, X):
        """Make predictions on new data"""
        return self.model.predict(X)