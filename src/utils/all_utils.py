import yaml
import os
import pandas as pd

def read_config(config_path: str) -> dict:
    with open(config_path) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content

def create_directory(dir_paths: list):

    for dir_path in dir_paths:
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)


def read_save_data(config_path: str):
    content = read_config(config_path=config_path)

    data_path = content["data_source"]
    df = pd.read_csv(data_path,sep=";")

    artifact_dir_name = content["artifacts"]["artifact_folder"]
    raw_data_folder_name = content["artifacts"]["raw_data_folder"]
    raw_data_file_name  = content["artifacts"]["raw_data_name"]
    
    artifact_folder_path = os.path.join(os.getcwd(),artifact_dir_name)
    raw_data_folder_path = os.path.join(artifact_folder_path,raw_data_folder_name)
    raw_data_file_path = os.path.join(raw_data_folder_path,raw_data_file_name)

    create_directory(dir_paths=[artifact_folder_path,raw_data_folder_path])

    df.to_csv(raw_data_file_path,index=False)