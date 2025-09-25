import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# Classe responsável por orquestrar treino, split, escalonamento e predição de modelos.
class Trainer:
    def __init__(self):
        pass

    # Separa features (X) e target (y) a partir do DataFrame.
    def separete_XY(self, df: pd.DataFrame, col_target: str):
        X = df.drop(col_target, axis=1)
        y = df[col_target]
        return X, y

    # Divide os dados em treino e teste, mantendo a proporção do target.
    def do_split(self, x: pd.DataFrame, y: pd.DataFrame, random_state: int, test_size: int):
        X_train, X_test, y_train, y_test = train_test_split(
            x, y, test_size=test_size, random_state=random_state, stratify=y
        )
        return X_train, X_test, y_train, y_test

    # Escalona apenas as variáveis numéricas e mantém as categóricas.
    def do_scale(self, X: pd.DataFrame, scaler: StandardScaler()):
        num_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
        cat_features = X.select_dtypes(include=["object", "category", "bool"]).columns.tolist()

        X_train_num = pd.DataFrame(scaler.fit_transform(X[num_features]), columns=num_features)
        X_train_cat = X[cat_features].reset_index(drop=True)

        X_scaled = pd.concat([X_train_num, X_train_cat], axis=1)

        return X_scaled

    # Treina um modelo de regressão logística com parâmetros definidos.
    def train_log_regression(
        self,
        X_train: pd.DataFrame,
        y_train: pd.Series,
        class_weight: dict,
        max_iter: int,
        random_state: int,
    ):
        logreg = LogisticRegression(
            class_weight=class_weight, max_iter=max_iter, random_state=random_state
        )

        return logreg
