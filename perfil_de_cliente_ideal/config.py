from pathlib import Path

# Define o pasta "raiz"
ROOT = Path(__file__).resolve().parents[1]  # volta até a raiz do repo

# Caminho para os dados
NAME_RAWDATASET = "marketing_campaign.csv"
NAME_PROCESSEDDATASET = "clean_dataset.csv"
DATA_DIR = ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw" / NAME_RAWDATASET
PROCESSED_DATA_DIR = DATA_DIR / "processed"
PROCESSED_DATA_DIR_NAME = DATA_DIR / "processed" / NAME_PROCESSEDDATASET

# Caminho para os modelos
NAME_MODEL = "linear_regression.joblib"
MODEL_DIR = ROOT / "models"
MODEL_DIR_NAME = ROOT / "models" / NAME_MODEL

# Caminho para o reports
REPORTS_DIR = ROOT / "reports"

# parâmetros globais para o modelo
RANDOM_SEED = 42
TEST_SIZE = 0.2
TARGET_COL = "AcceptedCmp1"
WEIGHT = {0: 1, 1: 8}
MAX_ITER = 600

# formato dos dados
CSV_SEPARATOR = "\t"
