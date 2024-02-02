"""
Weekend Workshop 2: mondel_name Madness

Original file is located at
    https://colab.research.google.com/drive/1D9n5qeIeSIAs1vAuYnI640nvLR1QZBW1

"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve, auc, precision_recall_curve

from models import *
from plot import *

def evaluate(y_true, y_pred, y_prob, model_name):
    """
    Function to evaluate and print the model_name performance.
    """
    metrics = {}

    # Store mondel_name name
    metrics['model_name'] = model_name

    # Classification Report
    metrics['classification_report'] = classification_report(y_true, y_pred, output_dict=True)

    if y_prob is not None:
        metrics['auc_score'] = roc_auc_score(y_true, y_prob)

    return metrics


def run_algorithm(models_to_run):
    # Getting and preprocessing data
    data = load_breast_cancer()
    X = data.data
    y = data.target

    result = {}

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    df = pd.DataFrame(data=np.c_[X, y], columns=np.append(data.feature_names, ["target"]))

    # Splitting the data
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

    all_models = {}

    for model_name in models_to_run:
        if model_name in globals() and callable(globals()[model_name]):
            model_func = globals()[model_name]
            model, y_pred, y_prob = model_func(X_train, y_train, X_test)
            all_models[model_name] = model

        result[model_name] = evaluate(y_test, y_pred, y_prob, model_name)

    if(len(models_to_run) == 10):
        #first image
        plot_all_roc(all_models, X_test, y_test)

        #second image
        # plot_all_prc(all_models)

    return result