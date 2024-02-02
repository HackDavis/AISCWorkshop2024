import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# Plot ROC curves for all applicable models
def plot_roc(model, X_test, y_test, label):
    y_score = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_score)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, lw=2, label=f'{label} (AUC = {roc_auc:.2f})')

# Function to plot Precision-Recall Curve
def plot_precision_recall_curve(model, X_test, y_test, model_name):
    if hasattr(model, "predict_proba"):
        y_prob = model.predict_proba(X_test)[:, 1]
        precision, recall, _ = precision_recall_curve(y_test, y_prob)

        plt.plot(recall, precision, label=f'{model_name}')

def plot_all_roc(all_models, X_test, y_test):
        # Create a figure for ROC curves
    plt.figure(figsize=(10, 8))

    for model_name in all_models:
        plot_roc(all_models[model_name], X_test, y_test, model_name)

    # Plot the diagonal line (random guessing)
    plt.plot([0, 1], [0, 1], 'k--')

    # Set labels and title
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves')

    # Add legends for each model
    plt.legend(loc="lower right")

    plt.savefig('first_graph.png')
    plt.close()

# def plot_all_prc():
#     # Plotting Precision-Recall Curves for all applicable models

#     plt.figure(figsize=(10, 8))
#     plot_precision_recall_curve(lr_model, X_test, y_test, 'Logistic Regression')
#     plot_precision_recall_curve(svm_model, X_test, y_test, 'SVM')
#     plot_precision_recall_curve(rf_model, X_test, y_test, 'Random Forest')
#     plot_precision_recall_curve(gb_model, X_test, y_test, 'Gradient Boosting')
#     plot_precision_recall_curve(ab_model, X_test, y_test, 'AdaBoost')
#     plot_precision_recall_curve(xg_model, X_test, y_test, 'XGBoost')
#     plot_precision_recall_curve(knn_model, X_test, y_test, 'KNN')
#     plot_precision_recall_curve(dt_model, X_test, y_test, 'Decision Tree')
#     plot_precision_recall_curve(nb_model, X_test, y_test, 'Naive Bayes')
#     plot_precision_recall_curve(nn_model, X_test, y_test, 'Neural Network (MLP Classifier)')

#     plt.xlabel('Recall')
#     plt.ylabel('Precision')
#     plt.title('Precision-Recall Curves')
#     plt.legend(loc="lower left")
#     plt.savefig('second_graph.png')
#     plt.close()