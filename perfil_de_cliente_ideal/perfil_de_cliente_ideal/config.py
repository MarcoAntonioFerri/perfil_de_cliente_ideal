from pathlib import Path
"""
from dotenv import load_dotenv
from loguru import logger

# Load environment variables from .env file if it exists
load_dotenv()

# Paths

PROJ_ROOT = Path(__file__).resolve().parents[1]
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

MODELS_DIR = PROJ_ROOT / "models"

REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# If tqdm is installed, configure loguru with tqdm.write
# https://github.com/Delgan/loguru/issues/135
try:
    from tqdm import tqdm

    logger.remove(0)
    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
except ModuleNotFoundError:
    pass
"""
# caminhos
ROOT = Path(__file__).resolve().parents[1]  # volta até a raiz do repo
NAME_RAWDATASET = "marketing_campaign.csv"
DATA_DIR = ROOT / "data"
MODEL_DIR = ROOT / "models"
RAW_DATA_DIR = DATA_DIR / "raw" / NAME_RAWDATASET

#print(ROOT)
# arquivos (ajuste para o seu caso)
#PROCESSED_CSV = DATA_DIR / "processed" / "dataset.csv" #necessaário comentar pois não existe o dataset.csv
#MODEL_PATH = MODEL_DIR / "clf.joblib"

# parâmetros globais
RANDOM_SEED = 42
TEST_SIZE = 0.2
TARGET_COL = "AcceptedCmp1"

# formato dos dados
CSV_SEPARATOR = "\t"