import argparse
from datetime import date
from pathlib import Path

from joblib import dump, load
from loguru import logger
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

from perfil_de_cliente_ideal.config import (
    CSV_SEPARATOR,
    MAX_ITER,
    MODEL_DIR_NAME,
    NAME_PROCESSEDDATASET,
    PROCESSED_DATA_DIR,
    PROCESSED_DATA_DIR_NAME,
    RANDOM_SEED,
    REPORTS_DIR,
    RAW_DATA_DIR,
    TARGET_COL,
    TEST_SIZE,
    WEIGHT,
)
from perfil_de_cliente_ideal.dataset import DataRepository
from perfil_de_cliente_ideal.features import FeatureEngineer
from perfil_de_cliente_ideal.modeling.model import Trainer

def cmd_train(args: argparse.Namespace):

    #Instância as classes
    datarepository = DataRepository()
    engineer = FeatureEngineer()
    trainer = Trainer()

    #Carregando Dataset
    logger.info("Carregando dataset bruto de {}", RAW_DATA_DIR)
    heart = datarepository.load_dataframe(RAW_DATA_DIR, CSV_SEPARATOR)

    # Selecionando features que serão usadas na modelagem
    heart = engineer.select_features(heart, ["Income", "Education", "Marital_Status", "Kidhome", "Teenhome", "Year_Birth", "AcceptedCmp1"])
    logger.info("As features para modelagem foram selecionadas.")

    #Removendo missing da feature Income
    logger.info("Removendo valores ausentes de 'Income'")
    heart = engineer.remove_missing(heart, "Income")


    #Criando variável Age
    logger.info("Criando variável 'age' a partir do ano de nascimento")
    heart = engineer.make_feature_age(heart)

    #Removendo Outliers da variável age e Income
    logger.info("Removendo outliers de 'age' > 100 e 'Income' > 600000")
    heart = engineer.remove_outliers(heart, "age", "above", 100)
    heart = engineer.remove_outliers(heart, "Income", "above", 600000)

    #Salvando o DataFrame com dados limpos
    datarepository.save_dataframe(heart, NAME_PROCESSEDDATASET, PROCESSED_DATA_DIR)
    logger.info("Dataset devidamente tratado, salvo no caminho: {}", PROCESSED_DATA_DIR)

    #Load do Dataset tratado
    logger.info("Carregando dataset processado para modelagem")
    processed_heart = datarepository.load_dataframe(PROCESSED_DATA_DIR_NAME, ",")

    X = processed_heart.drop(TARGET_COL, axis=1)
    y = processed_heart[TARGET_COL]

    #Aplicando OrdinalEncoding e One-hot-Encoding
    logger.info("Aplicando ordinal encoding e one-hot encoding")
    X = engineer.ordinal_education(X)
    X = engineer.do_one_hot_enconding(X)

    #Separando em treino e teste
    logger.info("Separando dataset em treino e teste")
    X_train, X_test, y_train, y_test = trainer.do_split(X, y, random_state=RANDOM_SEED, test_size=TEST_SIZE)

    #Realizando escalonamento
    logger.info("Aplicando escalonamento nas variáveis numéricas")
    scaler = StandardScaler()
    X_train_scaled = trainer.do_scale(X_train, scaler)
    X_test_scaled = trainer.do_scale(X_test, scaler)

    #Necessário resetar o índice do y_train, pois, ao fazer o Scaled ele já resetou automaticamente o índica deo X_train_scaled
    y_train.reset_index(drop=True, inplace=True)

    #Treinando modelo
    model = trainer.train_log_regression(X_train_scaled, y_train, class_weight=WEIGHT, max_iter=MAX_ITER, random_state=RANDOM_SEED)
    model.fit(X_train, y_train)
    logger.info("Modelo de Regressão Logística treinado com sucesso")

    y_pred = model.predict(X_test)
    dump(model, MODEL_DIR_NAME)
    logger.info("Salvando modelo treinado em {}", MODEL_DIR_NAME)

    logger.success("Treinamento concluído com sucesso!")
    return 0

def cmd_predict(args: argparse.Namespace):

    #Instância as classes
    datarepository = DataRepository()
    engineer = FeatureEngineer()
    trainer = Trainer()

    # Verifica se o caminho de entrada passado via CLI realmente existe
    in_path = Path(args.path_to_input)
    if not in_path.exists():
        logger.error("Arquivo ou caminho inserido inexistente.")
        return 2

    # Carrega o dataset do arquivo informado
    heart = datarepository.load_dataframe(in_path, args.sep)
    logger.info("Arquivo de inputação carregado com sucesso.")

    # Carrega o modelo previamente treinado (Já salvo)
    model = load(MODEL_DIR_NAME)
    logger.info("Modelo de Regressão Logística carregado com sucesso.")

    # Aplica Ordinal_Encoding e One-Hot-Encoding
    heart_encoded = engineer.ordinal_education(heart)
    heart_encoded = engineer.do_one_hot_enconding(heart_encoded)
    logger.info("Encoding aplicado com sucesso.")

    # Escala as variáveis numéricas usando StandardScaler
    scaler = StandardScaler()
    heart_encoded_scaled = trainer.do_scale(heart_encoded, scaler)
    logger.info("Escalonamento aplicado com sucesso.")

    # Remove a coluna target ("AcceptedCmp1") caso ainda esteja presente
    if "AcceptedCmp1" in heart_encoded_scaled.columns:
        heart_encoded_scaled.drop(columns="AcceptedCmp1", inplace=True)

    # Gera as predições com o modelo carregado
    logger.info("Gerando as predições")
    preds = model.predict(heart_encoded_scaled)


    if args.output != REPORTS_DIR:
        out = Path(args.output)
        datarepository.save_dataframe(pd.DataFrame(preds), name=out.name ,path=out.parent)
        logger.info("Predições salvas em {}", out)
        logger.success("Todas as predições foram feitas com sucesso!")
        return 0

    datarepository.save_dataframe(pd.DataFrame(preds), name="predicao_" + str(date.today()) + ".csv" , path=REPORTS_DIR)

    logger.info("Predições salvas na pasta 'reports'")
    logger.success("Todas as predições foram feitas com sucesso!")
    return 0