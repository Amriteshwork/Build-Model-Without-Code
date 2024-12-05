# ML Web Platform

A comprehensive web-based platform for building and deploying machine learning models with minimal coding.

## Features

- Data loading from local files or popular ML libraries
- Automatic preprocessing detection and application
- Interactive data visualization
- Support for both supervised and unsupervised learning
- Model evaluation and comparison tools
- Local model saving and loading
- Caching system for better performance

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy .env.example to .env and configure:
   ```bash
   cp .env.example .env
   ```
5. Run the application:
   ```bash
   python run.py
   ```

## Project Structure

```
ml_web_platform/
├── app/                    # Main application package
│   ├── ml/                # Machine learning components
│   ├── routes/            # Flask routes
│   ├── static/            # Static files
│   └── templates/         # HTML templates
├── cache/                 # Cache storage
├── saved_models/         # Saved model storage
├── saved_visualizations/ # Saved plots
└── tests/               # Test suite
```

## Development

- Run tests: `pytest`
- Format code: `black .`
- Lint code: `flake8`

## Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for contribution guidelines.
