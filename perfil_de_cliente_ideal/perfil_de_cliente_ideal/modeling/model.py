from pathlib import Path

from perfil_de_cliente_ideal.dataset import DataRepository
from perfil_de_cliente_ideal.features import FeatureEngineer
from perfil_de_cliente_ideal.config import RAW_DATA_DIR, CSV_SEPARATOR
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

"""from loguru import logger
from tqdm import tqdm
import typer

from perfil_de_cliente_ideal.config import MODELS_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    features_path: Path = PROCESSED_DATA_DIR / "features.csv",
    labels_path: Path = PROCESSED_DATA_DIR / "labels.csv",
    model_path: Path = MODELS_DIR / "model.pkl",
    # -----------------------------------------
):
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Training some model...")
    for i in tqdm(range(10), total=10):
        if i == 5:
            logger.info("Something happened for iteration 5.")
    logger.success("Modeling training complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()"""

class Trainer():
    def __init__(self):
        pass

    def separete_XY(self, df : pd.DataFrame, col_target : str):
        X = df.drop(col_target, axis=1)
        y = df[col_target]
        return X, y

    def do_split(self, x : pd.DataFrame, y : pd.DataFrame, random_state : int, test_size : int):
        X_train, X_test, y_train, y_test = train_test_split(
            x, y, test_size=test_size, random_state=random_state, stratify=y
        )
        return X_train, X_test, y_train, y_test

    def do_scale(self, X_train : pd.DataFrame, X_test : pd.DataFrame ,scaler : StandardScaler()):

        num_features = X_train.select_dtypes(include=["int64", "float64"]).columns.tolist()
        cat_features = X_train.select_dtypes(include=["object", "category"]).columns.tolist()

        X_train_num = pd.DataFrame(scaler.fit_transform(X_train[num_features]), columns=num_features)
        X_train_cat = X_train[cat_features].reset_index(drop=True)

        X_test_num = pd.DataFrame(scaler.transform(X_test[num_features]), columns=num_features)
        X_test_cat = X_test[cat_features].reset_index(drop=True)

        X_train_scaled = pd.concat([X_train_num, X_train_cat], axis=1)
        X_test_scaled = pd.concat([X_test_num, X_test_cat], axis=1)

        return X_train_scaled, X_test_scaled

    def train_log_regression(self, X_train : pd.DataFrame, y_train : pd.Series, class_weight : dict, max_iter : int, random_state : int):
        logreg = LogisticRegression(
            class_weight=class_weight,
            max_iter=max_iter,
            random_state=random_state
        )

        logreg.fit(X_train, y_train)
        return logreg

    def predict_log_regression(self, model: LogisticRegression, X_test: pd.DataFrame):
        return model.predict(X_test)

    def predict_proba_log_regression(self, model: LogisticRegression, X_test: pd.DataFrame) -> pd.DataFrame:
        return model.predict_proba(X_test)