import os
from kaggle.api.kaggle_api_extended import KaggleApi
from config import RAW_DATA_DIR, KAGGLE_DATASET_URL

def download_esc50():
    """Download the ESC-50 dataset from Kaggle."""
    api = KaggleApi()
    api.authenticate()

    download_path = AUDIO_FILES_PATH
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    api.dataset_download_files(KAGGLE_DATASET_URL, path=download_path, unzip=True)
    print("ESC-50 dataset downloaded successfully.")

if __name__ == "__main__":
    download_esc50()
