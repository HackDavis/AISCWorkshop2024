import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.datasets import load_breast_cancer

def analysis():
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns = data.feature_names)
    df['target'] = data.target

    cat_cols=df.select_dtypes(include=['object']).columns
    num_cols = df.select_dtypes(include=np.number).columns.tolist()
    
    plt.figure(figsize=(13,17))
    sns.pairplot(data=df)
    plt.savefig('analysis.png')