import yaml
import os
import pandas as pd
from sklearn.model_selection import train_test_split

def read_yaml(config_path: str) -> dict:
    with open(config_path) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content

def create_directory(dir_paths: list):

    for dir_path in dir_paths:
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)


def read_save_data(config_path: str):
    content = read_yaml(config_path=config_path)

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


def split_data(config_path : str,params_path : str):
    content = read_yaml(config_path=config_path)
    params = read_yaml(config_path=params_path)

    artifact_dir_name = content["artifacts"]["artifact_folder"]
    raw_data_folder_name = content["artifacts"]["raw_data_folder"]
    raw_data_file_name  = content["artifacts"]["raw_data_name"]
    
    artifact_folder_path = os.path.join(os.getcwd(),artifact_dir_name)
    raw_data_folder_path = os.path.join(artifact_folder_path,raw_data_folder_name)
    raw_data_file_path = os.path.join(raw_data_folder_path,raw_data_file_name) 

    df = pd.read_csv(raw_data_file_path)

    test_size = params["base"]["test_size"]
    random_state = params["base"]["random_state"]

    train_df,test_df = train_test_split(df,test_size=test_size,random_state=random_state)

    split_data_folder_name = content["artifacts"]["split_data_dir"]
    train_data_file_name  = content["artifacts"]["train_data_name"]
    test_data_file_name  = content["artifacts"]["test_data_name"]

    split_data_folder_path = os.path.join(artifact_folder_path,split_data_folder_name)

    create_directory([split_data_folder_path])

    train_data_file_path = os.path.join(split_data_folder_path,train_data_file_name)
    test_data_file_path = os.path.join(split_data_folder_path,test_data_file_name)

    train_df.to_csv(train_data_file_path)
    test_df.to_csv(test_data_file_path)

