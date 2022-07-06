from ast import arg
from statistics import mode
import yaml
import pandas as pd
import argparse
from src.utils.all_utils import *
import joblib

from sklearn.linear_model import ElasticNet

def train_data(config_path : str, params_path : str):
    content = read_yaml(config_path=config_path)
    params = read_yaml(config_path=params_path)

    artifact_dir_name = content["artifacts"]["artifact_folder"]
    artifact_folder_path = os.path.join(os.getcwd(),artifact_dir_name)

    split_data_folder_name = content["artifacts"]["split_data_dir"]
    train_data_file_name  = content["artifacts"]["train_data_name"]

    split_data_folder_path = os.path.join(artifact_folder_path,split_data_folder_name)
    train_data_file_path = os.path.join(split_data_folder_path,train_data_file_name)

    train_df = pd.read_csv(train_data_file_path)

    train_y = train_df["quality"]
    train_x = train_df.drop("quality",axis=1)

    alpha = params["model_params"]["alpha"]
    l1_ratio = params["model_params"]["l1_ratio"]

    model =  ElasticNet(alpha=alpha,l1_ratio=l1_ratio)

    model.fit(train_x,train_y) 

    model_folder_name = content["artifacts"]["model_folder_name"]
    model_file_name = content["artifacts"]["model_file_name"]

    model_folder_path = os.path.join(artifact_folder_path,model_folder_name)

    create_directory([model_folder_path])

    model_file_path = os.path.join(model_folder_path,model_file_name)

    joblib.dump(model,model_file_path)


if __name__ == '__main__' :

    args = argparse.ArgumentParser()
    
    default_config_path = os.path.join(os.path.join(os.getcwd(),"config"),"config.yaml")

    defalt_param_path = os.path.join(os.getcwd(),"params.yaml")

    args.add_argument("--config","-c",default=default_config_path)

    args.add_argument("--params","-p",default=defalt_param_path)

    parsed_args = args.parse_args()

    train_data(config_path=parsed_args.config, params_path=parsed_args.params)