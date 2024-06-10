import os 
from Converter.converter import *

# these variable

absolute_path = "./audio/"

def getAllFile(path: str = "./audio/") -> list[str]:
    dir_list = os.listdir(path)
    dir_list = [file for file in dir_list if file.endswith(".wav")]
    return dir_list
dir_list: list[str] = getAllFile()

def convert_all(dir_list: list[str] = dir_list) -> list[dict[str, str]]: 
    ans: list[dict[str, str]] = []
    for file in dir_list: 
        convert = converter(os.path.join(absolute_path, file))
        ans.append({'filename': file, 'text': convert.binary_to_ascii()}) 
    return ans

# for item in convert_all(dir_list): 
#     print(item)






