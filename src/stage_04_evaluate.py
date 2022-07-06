from ast import arg
from lib2to3.pgen2.grammar import opmap_raw
import yaml
import pandas as pd
import argparse
from src.utils.all_utils import *
import joblib
from sklearn.metrics import mean_squared_error, mean_absolute_error
import json

def evaluate_model(config_path : str):
    content = read_yaml(config_path=config_path)

    artifact_dir_name = content["artifacts"]["artifact_folder"]
    artifact_folder_path = os.path.join(os.getcwd(),artifact_dir_name)

    split_data_folder_name = content["artifacts"]["split_data_dir"]
    test_data_file_name  = content["artifacts"]["test_data_name"]

    split_data_folder_path = os.path.join(artifact_folder_path,split_data_folder_name)
    test_data_file_path = os.path.join(split_data_folder_path,test_data_file_name)

    test_df = pd.read_csv(test_data_file_path)

    
    test_y = test_df["quality"]
    test_x = test_df.drop("quality",axis=1)

    model_folder_name = content["artifacts"]["model_folder_name"]
    model_file_name = content["artifacts"]["model_file_name"]

    model_folder_path = os.path.join(artifact_folder_path,model_folder_name)
    model_file_path = os.path.join(model_folder_path,model_file_name)

    model = joblib.load(model_file_path)

    pred_y = model.predict(test_x)

    print("*"*10,end="")
    print("MSE",end="")
    print("*"*10)
    mse = mean_squared_error(test_y,pred_y)
    print(mse)

    print("*"*10,end="")
    print("MAE",end="")
    print("*"*10)
    mae = mean_absolute_error(test_y,pred_y)
    print(mae)

    eval_dict = dict()
    eval_dict["mse"] = mse
    eval_dict["mae"] = mae

    eval_file_name = content["artifacts"]["eval_file_name"]
    eval_file_path  = os.path.join(artifact_folder_path,eval_file_name)

    with open(eval_file_path,"w") as outfile:
        json.dump(eval_dict,outfile)
    



if __name__ == '__main__' :

    args = argparse.ArgumentParser()
    
    default_config_path = os.path.join(os.path.join(os.getcwd(),"config"),"config.yaml")

    args.add_argument("--config","-c",default=default_config_path)

    parsed_args = args.parse_args()

    evaluate_model(config_path=parsed_args.config)