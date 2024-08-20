import os
import subprocess
import shutil
import zipfile

def download_dataset(dataset_name: str) -> None:
    """
    Download the dataset from Kaggle using the dataset name.

    Parameters:
        dataset_name (str): Name of the dataset in Kaggle.
        target_dir (str): Directory where the ZIP file will be saved.
    """
    subprocess.run(['kaggle', 'datasets', 'download', '-d', dataset_name], check=True)

def move_zip_file(zip_name: str, target_dir: str) -> None:
    """
    Moves the downloaded ZIP file to the destination directory.

    Parameters:
        zip_name (str): Name of the ZIP file.
        source_dir (str): Source directory.
        target_dir (str): Destination directory.
    """
    shutil.move(zip_name, os.path.join(target_dir, zip_name))

def extract_zip(zip_path: str, extract_to: str) -> None:
    """
    Extracts the contents of the ZIP file to the specified directory.

    Parameters:
        zip_path (str): Full path of the ZIP file.
        extract_to (str): Directory where the contents will be extracted.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def rename_extracted_csv(data_dir: str, new_csv_name: str) -> None:
    """
    Renames the extracted CSV file.

    Parameters:
        data_dir (str): Directory where the CSV file is located.
        new_csv_name (str): New name for the CSV file.
    """
    csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    if csv_files:
        old_csv_path = os.path.join(data_dir, csv_files[0])
        new_csv_path = os.path.join(data_dir, new_csv_name)
        os.rename(old_csv_path, new_csv_path)

def cleanup(zip_path: str) -> None:
    """
    Removes the original ZIP file.

    Parameters:
        zip_path (str): Full path of the ZIP file to be removed.
    """
    os.remove(zip_path)

def main():
    data_dir = './data'
    zip_file_name = 'online-retail-ii-uci.zip'
    csv_file_name = 'raw_data.csv'
    dataset_name = 'mashlyn/online-retail-ii-uci'

    # Create the destination directory if it does not exist
    os.makedirs(data_dir, exist_ok=True)

    # Download, Extract and Rename Process
    download_dataset(dataset_name)
    move_zip_file(zip_file_name, data_dir)
    extract_zip(os.path.join(data_dir, zip_file_name), data_dir)
    rename_extracted_csv(data_dir, csv_file_name)

    # Cleaning the ZIP file
    cleanup(os.path.join(data_dir, zip_file_name))

if __name__ == "__main__":
    main()
