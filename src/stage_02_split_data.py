from ast import arg
import yaml
import pandas as pd
import argparse
from src.utils.all_utils import *

if __name__ == '__main__' :

    args = argparse.ArgumentParser()
    
    default_config_path = os.path.join(os.path.join(os.getcwd(),"config"),"config.yaml")

    defalt_param_path = os.path.join(os.getcwd(),"params.yaml")

    args.add_argument("--config","-c",default=default_config_path)

    args.add_argument("--params","-p",default=defalt_param_path)

    parsed_args = args.parse_args()

    split_data(config_path=parsed_args.config, params_path=parsed_args.params)