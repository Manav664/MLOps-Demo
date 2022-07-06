from ast import arg
import yaml
import pandas as pd
import argparse
from src.utils.all_utils import *

if __name__ == '__main__' :

    args = argparse.ArgumentParser()
    
    default_config_path = os.path.join(os.path.join(os.getcwd(),"config"),"config.yaml")

    args.add_argument("--config","-c",default=default_config_path)

    parsed_args = args.parse_args()

    read_save_data(parsed_args.config)