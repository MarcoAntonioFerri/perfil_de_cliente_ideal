
from pathlib import Path
#from unittest.mock import inplace

from perfil_de_cliente_ideal.config import RAW_DATA_DIR, CSV_SEPARATOR
import pandas as pd

"""
#from loguru import logger
#from tqdm import tqdm
#import typer

#from perfil_de_cliente_ideal.config import PROCESSED_DATA_DIR, RAW_DATA_DIR
from perfil_de_cliente_ideal.config import RAW_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    #output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Processing dataset...")
    for i in tqdm(range(10), total=10):
        if i == 5:
            logger.info("Something happened for iteration 5.")
    logger.success("Processing dataset complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
"""
class DataRepository:
    def __init__(self):
        pass

    def load_dataframe(self, raw_dir, sep):
        df = pd.read_csv(raw_dir, sep=sep)
        return df

    def save_dataframe(self, dataframe : pd.DataFrame, name : str, path : str= "",  index=False):
        path_name = path + name
        dataframe.to_csv(path_name, index=index)
        return



#datarepository.save_dataframe(heart,name="novo_df.csv", path="../data/processed/")
