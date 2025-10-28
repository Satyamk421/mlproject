import sys
import os
import numpy as np
import pandas as pd
from src.execption import CustomException
import dill

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path ,'wb') as obj:
            dill.dump(obj,obj)
    except Exception as e:
        raise CustomException(e,sys)

    