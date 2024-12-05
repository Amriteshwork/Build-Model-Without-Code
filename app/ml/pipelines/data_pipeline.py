from typing import Dict, Any
import pandas as pd

class DataPipeline:
    def __init__(self):
        self.steps = []
        
    def add_step(self, name: str, transform_fn: callable, **params):
        """Add a transformation step to the pipeline"""
        self.steps.append({
            'name': name,
            'transform': transform_fn,
            'params': params
        })
        return self
        
    def fit_transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """Apply all transformation steps to the data"""
        transformed_data = data.copy()
        for step in self.steps:
            transform_fn = step['transform']
            params = step['params']
            transformed_data = transform_fn(transformed_data, **params)
        return transformed_data
