from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import AdaBoostClassifier
import xgboost as xgb

def logistic_regression(X_train, y_train, X_test):
    lr_model = LogisticRegression(max_iter=1000, solver='saga')
    lr_model.fit(X_train, y_train)
    y_pred_lr = lr_model.predict(X_test)
    y_prob_lr = lr_model.predict_proba(X_test)[:, 1]

    return lr_model, y_pred_lr, y_prob_lr

def k_nearest_neighbors(X_train, y_train, X_test):
    knn_model = KNeighborsClassifier()
    knn_model.fit(X_train, y_train)
    y_pred_knn = knn_model.predict(X_test)
    y_prob_knn = knn_model.predict_proba(X_test)[:,1]

    return knn_model, y_pred_knn, y_prob_knn

def support_vector_machine(X_train, y_train, X_test):
    svm_model = SVC(probability=True)
    svm_model.fit(X_train, y_train)
    y_pred_svm = svm_model.predict(X_test)
    y_prob_svm = svm_model.predict_proba(X_test)[:, 1]

    return svm_model, y_pred_svm, y_prob_svm

def decision_tree(X_train, y_train, X_test):
    dt_model = DecisionTreeClassifier()
    dt_model.fit(X_train, y_train)
    y_pred_dt = dt_model.predict(X_test)
    y_prob_dt = dt_model.predict_proba(X_test)[:,1]

    return dt_model, y_pred_dt, y_prob_dt

def random_forest(X_train, y_train, X_test):
    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)
    y_prob_rf = rf_model.predict_proba(X_test)[:, 1]

    return rf_model, y_pred_rf, y_prob_rf

def gradient_boosting(X_train, y_train, X_test):
    gb_model = GradientBoostingClassifier()
    gb_model.fit(X_train, y_train)
    y_pred_gb = gb_model.predict(X_test)
    y_prob_gb = gb_model.predict_proba(X_test)[:, 1]

    return gb_model, y_pred_gb, y_prob_gb

def naive_bayes(X_train, y_train, X_test):
    nb_model = GaussianNB()
    nb_model.fit(X_train, y_train)
    y_pred_nb = nb_model.predict(X_test)
    y_prob_nb = nb_model.predict_proba(X_test)[:,1]

    return nb_model, y_pred_nb, y_prob_nb

def neural_network(X_train, y_train, X_test):
    nn_model = MLPClassifier(max_iter=1000)
    nn_model.fit(X_train, y_train)
    y_pred_nn = nn_model.predict(X_test)
    y_prob_nn = nn_model.predict_proba(X_test)[:, 1]

    return nn_model, y_pred_nn, y_prob_nn

def ada_boost(X_train, y_train, X_test):
    ab_model = AdaBoostClassifier()
    ab_model.fit(X_train, y_train)
    y_pred_ab = ab_model.predict(X_test)
    y_prob_ab = ab_model.predict_proba(X_test)[:, 1]

    return ab_model, y_pred_ab, y_prob_ab

def xg_boost(X_train, y_train, X_test):
    xg_model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    xg_model.fit(X_train, y_train)
    y_pred_xg = xg_model.predict(X_test)
    y_prob_xg = xg_model.predict_proba(X_test)[:, 1]

    return xg_model, y_pred_xg, y_prob_xg