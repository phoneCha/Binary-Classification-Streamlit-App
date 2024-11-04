# Binary Classification Streamlit App 🍄

This Streamlit app is designed to classify mushrooms as either edible or poisonous using binary classification models. It provides an interactive interface for training, evaluating, and comparing different machine learning models.

**Note**: This project is part of the **CPE312 Intro to Data Science** course for Computer Engineering at SWU.

## Features
- **Model Selection**: Choose between SVM, Logistic Regression, and Random Forest
- **Hyperparameter Tuning**: Adjust model hyperparameters for customized training
- **Performance Metrics**: View metrics including Accuracy, Precision, Recall, Confusion Matrix, ROC Curve, and Precision-Recall Curve
- **Data Display**: Option to view raw mushroom dataset

## Getting Started

### Prerequisites
Ensure you have the required libraries:

```bash
pip install -r requirements.txt
```

Required packages:
- streamlit
- pandas
- numpy
- matplotlib
- scikit-learn
- seaborn

### Running the App

```bash
streamlit run app.py
```

### Project Structure
```
.
├── README.md
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
└── data/
    └── mushrooms.csv  # Mushroom dataset
```

### Usage
1. Select a classifier from the sidebar (SVM, Logistic Regression, or Random Forest)
2. Adjust the model hyperparameters:
   - SVM: C, kernel type, gamma
   - Logistic Regression: C, maximum iterations
   - Random Forest: number of trees, maximum depth, bootstrap option
3. Choose visualization metrics to display
4. Click "Classify" to train the model and view results
5. Optionally view the raw dataset using the checkbox

## Model Details

### Support Vector Machine (SVM)
- Best for: Non-linear classification with kernel tricks
- Adjustable parameters:
  - C: Controls regularization (0.01-10.0)
  - Kernel: RBF or Linear
  - Gamma: Scale or Auto

### Logistic Regression
- Best for: Binary classification with linear decision boundaries
- Adjustable parameters:
  - C: Regularization strength (0.01-10.0)
  - Maximum iterations: Convergence limit (100-1000)

### Random Forest
- Best for: Complex datasets with potential overfitting concerns
- Adjustable parameters:
  - Number of trees: 10-500
  - Maximum depth: 1-20
  - Bootstrap: Enable/disable sample bootstrapping

## Performance Metrics

The app provides several metrics to evaluate model performance:

1. **Basic Metrics**
   - Accuracy: Overall prediction accuracy
   - Precision: True positive rate
   - Recall: Sensitivity measure

2. **Visual Metrics**
   - Confusion Matrix: Visualization of prediction errors
   - ROC Curve: True vs. false positive rate trade-off
   - Precision-Recall Curve: Precision vs. recall trade-off

## Data Processing
- Automatic label encoding for categorical features
- 70-30 train-test split
- Cached data loading for improved performance

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a Pull Request

## Citations
1. Mushroom [Dataset]. (1981). UCI Machine Learning Repository. https://doi.org/10.24432/C5959T
2. Build a Machine Learning Web App with Streamlit and Python. Coursera Project Network

## Academic Context
This project is developed as part of the CPE312 Intro to Data Science curriculum at SWU's Computer Engineering department. It demonstrates practical applications of:
- Machine learning algorithms
- Data preprocessing
- Model evaluation
- Interactive visualization
- Web application development

## License
This project is licensed under the MIT License - see the LICENSE file for details.
