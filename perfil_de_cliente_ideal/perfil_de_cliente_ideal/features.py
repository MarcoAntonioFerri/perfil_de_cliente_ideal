from datetime import date
import pandas as pd


# Classe responsável por transformar e preparar dados (feature engineering).
class FeatureEngineer():
    def __init__(self):
        pass

    # Remove valores ausentes de uma coluna e reseta o índice.
    def remove_missing(self, df : pd.DataFrame, columns : str):
        df_no_missing = df.dropna(subset=[columns])
        df_no_missing.reset_index(drop=True, inplace=True)
        return df_no_missing

    # Cria a coluna 'age' a partir do ano de nascimento.
    def make_feature_age(self, df : pd.DataFrame):
        df["age"] = date.today().year - df["Year_Birth"]
        return df

    # Remove outliers acima ou abaixo de um valor em uma coluna.
    def remove_outliers(self, df : pd.DataFrame, column : str ,threshold : str, value):
        if threshold == "above":
            df = df[df[column] <= value]
            df.reset_index(drop=True, inplace=True)
            return df

        elif threshold == "below":
            df = df[df[column] >= value]
            df.reset_index(drop=True, inplace=True)
            return df

    # Converte a coluna 'Education' em valores ordinais.
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

    # Aplica one-hot encoding em variáveis categóricas.
    def do_one_hot_enconding(self, df : pd.DataFrame):
        df = pd.get_dummies(df, drop_first=True)
        return df

    # Seleciona apenas as colunas especificadas em list_features.
    def select_features(self, df : pd.DataFrame, list_features : list):
        #print("LISTA DE FEATURES", list_features)
        #print(df[[list_features]])
        df = df[list_features]
        return df

