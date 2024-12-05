// app/static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    const datasetForm = document.getElementById('dataset-form');
    const trainButton = document.getElementById('train-button');
    let currentDataset = null;

    // Handle dataset form submission
    datasetForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData(datasetForm);
        currentDataset = formData.get('dataset_name');
        
        try {
            const response = await fetch('/load_dataset', {
                method: 'POST',
                body: formData
            });
            
            const data = await response.json();
            
            if (data.success) {
                // Show dataset information
                document.getElementById('dataset-info').style.display = 'block';
                document.getElementById('n-samples').textContent = data.data.n_samples;
                document.getElementById('n-features').textContent = data.data.n_features;
                document.getElementById('feature-names').textContent = data.data.feature_names.join(', ');
                
                // Show training section
                document.getElementById('training-section').style.display = 'block';
            } else {
                alert('Error loading dataset: ' + data.error);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error loading dataset');
        }
    });

    // Handle training button click
    trainButton.addEventListener('click', async function() {
        if (!currentDataset) {
            alert('Please load a dataset first');
            return;
        }
        
        try {
            const response = await fetch('/train', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `dataset_name=${currentDataset}`
            });
            
            const data = await response.json();
            
            if (data.success) {
                // Show results
                document.getElementById('results').style.display = 'block';
                
                // Update metrics
                document.getElementById('r2-score').textContent = data.metrics.r2_score.toFixed(4);
                document.getElementById('mse').textContent = data.metrics.mse.toFixed(4);
                document.getElementById('rmse').textContent = data.metrics.rmse.toFixed(4);
                document.getElementById('mae').textContent = data.metrics.mae.toFixed(4);
                
                // Update coefficients
                const coefficientsDiv = document.getElementById('coefficients');
                coefficientsDiv.innerHTML = '<p>Coefficients:</p><ul>' + 
                    data.coefficients.map((coef, index) => 
                        `<li>Feature ${index}: ${coef.toFixed(4)}</li>`
                    ).join('') + '</ul>';
                
                // Update intercept
                document.getElementById('intercept').textContent = data.intercept.toFixed(4);
            } else {
                alert('Error training model: ' + data.error);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error training model');
        }
    });
});