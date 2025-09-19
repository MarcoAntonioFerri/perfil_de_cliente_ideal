from pathlib import Path
from perfil_de_cliente_ideal.dataset import DataRepository

from datetime import date
from perfil_de_cliente_ideal.config import RAW_DATA_DIR, CSV_SEPARATOR
import pandas as pd

"""

from loguru import logger
from tqdm import tqdm
import typer

from perfil_de_cliente_ideal.config import PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "features.csv",
    # -----------------------------------------
):
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Generating features from dataset...")
    for i in tqdm(range(10), total=10):
        if i == 5:
            logger.info("Something happened for iteration 5.")
    logger.success("Features generation complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
    
"""

class FeatureEngineer():
    def __init__(self):
        pass

    def remove_missing(self, df : pd.DataFrame, columns : str):
        df_no_missing = df.dropna(subset=[columns])
        df_no_missing.reset_index(drop=True, inplace=True)
        return df_no_missing

    def make_feature_age(self, df : pd.DataFrame):
        df["age"] = date.today().year - df["Year_Birth"]
        return df

    def remove_outliers(self, df : pd.DataFrame, column : str ,threshold : str, value):
        if threshold == "above":
            df = df[df[column] <= value]
            df.reset_index(drop=True, inplace=True)
            return df

        elif threshold == "below":
            df = df[df[column] >= value]
            df.reset_index(drop=True, inplace=True)
            return df

    def ordinal_education(self, df : pd.DataFrame):
        replace_education = {
            'Basic': 0,
            'Graduation': 1,
            '2n Cycle': 2,
            'Master': 3,
            'PhD': 4
        }
        df['Education'] = df['Education'].replace(replace_education)
        return df

    def do_one_hot_enconding(self, df : pd.DataFrame):
        df = pd.get_dummies(df, drop_first=True)
        return df

    def select_features(self, df : pd.DataFrame, list_features : list):
        df = df[[list_features]]
        return df

"""datarepository = DataRepository()
heart = datarepository.load_dataframe(RAW_DATA_DIR, CSV_SEPARATOR)
heart.drop(columns=["ID"], inplace=True)
print("Primeiro SHAPE:", heart.shape)

engineer = FeatureEngineer()
#heart = engineer.remove_missing(heart, columns="Income")
heart = engineer.make_feature_age(heart)
#heart = engineer.remove_outliers(heart, column="Income", threshold="above", value=600000)
#heart = engineer.remove_outliers(heart, column="age", threshold="above", value=100)
print(heart.info())
print(heart.isnull().sum())
print("Segundo SHAPE:", heart.shape)

print(heart[heart["age"] >= 100])"""