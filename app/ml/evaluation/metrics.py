from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    mean_squared_error,
    r2_score
)

class ModelEvaluator:
    @staticmethod
    def evaluate_classification(y_true, y_pred, y_prob=None):
        """Evaluate classification model performance"""
        metrics = {
            'accuracy': accuracy_score(y_true, y_pred),
            'precision': precision_score(y_true, y_pred, average='weighted'),
            'recall': recall_score(y_true, y_pred, average='weighted'),
            'f1': f1_score(y_true, y_pred, average='weighted')
        }
        return metrics

    @staticmethod
    def evaluate_regression(y_true, y_pred):
        """Evaluate regression model performance"""
        metrics = {
            'mse': mean_squared_error(y_true, y_pred),
            'rmse': mean_squared_error(y_true, y_pred, squared=False),
            'r2': r2_score(y_true, y_pred)
        }
        return metrics
