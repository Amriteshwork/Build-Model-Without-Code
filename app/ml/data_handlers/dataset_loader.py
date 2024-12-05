# app/ml/data_handlers/dataset_loader.py

from sklearn import datasets
import numpy as np

class DatasetLoader:
    """Handler for loading sklearn datasets"""
    
    @staticmethod
    def get_available_datasets():
        """Return list of available sklearn datasets"""
        return [
            {'name': 'boston', 'description': 'Boston House Prices'},
            {'name': 'diabetes', 'description': 'Diabetes Disease Progression'},
            {'name': 'california', 'description': 'California Housing Prices'}
        ]
    
    @staticmethod
    def load_dataset(dataset_name):
        """Load a specific dataset"""
        if dataset_name == 'boston':
            data = datasets.load_boston()
        elif dataset_name == 'diabetes':
            data = datasets.load_diabetes()
        elif dataset_name == 'california':
            data = datasets.fetch_california_housing()
        else:
            raise ValueError(f"Dataset {dataset_name} not found")
            
        return {
            'X': data.data,
            'y': data.target,
            'feature_names': data.feature_names,
            'n_samples': data.data.shape[0],
            'n_features': data.data.shape[1],
            'description': data.DESCR
        }