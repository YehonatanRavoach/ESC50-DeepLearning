import os
from pathlib import Path

CONFIG_PATH = Path(os.path.abspath(__file__))
# Move one level up to project root
ROOT_DIR = CONFIG_PATH.parent

# Define directories
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
AUDIO_FILES_PATH = RAW_DATA_DIR / "audio"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
AUGMENTED_DATA_DIR = PROCESSED_DATA_DIR / "augmented_data"
MODEL_DIR = ROOT_DIR / "models"

META_DIR = RAW_DATA_DIR / "meta"
CSV_FILE_PATH = META_DIR / "esc50.csv"

for path in [DATA_DIR, RAW_DATA_DIR, AUDIO_FILES_PATH, PROCESSED_DATA_DIR,
             AUGMENTED_DATA_DIR, MODEL_DIR, META_DIR]:
    os.makedirs(path, exist_ok=True)

