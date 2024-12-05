import os
import sys
from app import create_app

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)