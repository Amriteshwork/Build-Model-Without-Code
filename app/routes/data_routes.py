# app/routes/data_routes.py

from flask import Blueprint, render_template, jsonify, request
from sklearn import datasets
from app.ml.data_handlers.dataset_loader import DatasetLoader
from app.ml.models.supervised.regression.linear_regression import LinearRegressionModel

bp = Blueprint('data', __name__)

@bp.route('/')
def index():
    """Landing page with dataset selection"""
    available_datasets = DatasetLoader.get_available_datasets()
    return render_template('index.html', datasets=available_datasets)

@bp.route('/load_dataset', methods=['POST'])
def load_dataset():
    """Load selected dataset and return its details"""
    dataset_name = request.form.get('dataset_name')
    
    try:
        data = DatasetLoader.load_dataset(dataset_name)
        return jsonify({
            'success': True,
            'data': {
                'n_samples': data['n_samples'],
                'n_features': data['n_features'],
                'feature_names': data['feature_names']
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@bp.route('/train', methods=['POST'])
def train_model():
    """Train linear regression model with selected dataset"""
    dataset_name = request.form.get('dataset_name')
    
    try:
        # Load dataset
        data = DatasetLoader.load_dataset(dataset_name)
        
        # Initialize and train model
        model = LinearRegressionModel()
        results = model.train(data['X'], data['y'])
        
        return jsonify({
            'success': True,
            'metrics': results['metrics'],
            'coefficients': results['coefficients'].tolist(),
            'intercept': float(results['intercept'])
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})