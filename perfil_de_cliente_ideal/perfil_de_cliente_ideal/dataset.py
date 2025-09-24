from pathlib import Path
import pandas as pd

# Classe responsável por operações de I/O com DataFrames (carregar e salvar).
class DataRepository:
    def __init__(self):
        pass

    # Carrega um arquivo CSV em um DataFrame a partir de um caminho e separador.
    def load_dataframe(self, raw_dir, sep):
        df = pd.read_csv(raw_dir, sep=sep)
        return df

    # Salva um DataFrame em CSV em um diretório especificado com nome definido.
    def save_dataframe(self, dataframe : pd.DataFrame, name , path,  index=False):
        path_name = path / name
        dataframe.to_csv(path_name, index=index)
        return
