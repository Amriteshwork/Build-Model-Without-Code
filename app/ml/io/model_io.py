import joblib
import os
import json
from datetime import datetime

class ModelIO:
    @staticmethod
    def save_model(model, model_path: str, metadata: dict = None):
        """Save model and its metadata"""
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        
        # Add timestamp to metadata
        if metadata is None:
            metadata = {}
        metadata['timestamp'] = datetime.now().isoformat()
        
        # Save model
        joblib.dump(model, model_path)
        
        # Save metadata
        metadata_path = model_path + '.json'
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f)

    @staticmethod
    def load_model(model_path: str):
        """Load model and return its metadata"""
        # Load model
        model = joblib.load(model_path)
        
        # Load metadata if exists
        metadata = {}
        metadata_path = model_path + '.json'
        if os.path.exists(metadata_path):
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)
                
        return model, metadata
