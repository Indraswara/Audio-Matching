from crawler import * 
from Algorithm.BM import *
from Algorithm.KMP import *
from Algorithm.listBM import *
from Algorithm.listKMP import *
from Converter.converter import *

def main(): 
    while(True): 
        print("Pilih algoritma")
        print("1. Boyer Moore")
        print("2. KMP")
        print("3. Exit")
        algo = choose_algo(1, 3, "> ")
        user_input = str(input("Masukkan path audio yang akan dicari: "))
        if algo == 3: 
            break
        else:
            data: list[dict[str, str]] = convert_all()
            user_data = converter(user_input)
            # for item in data: 
            #     print(item)
            user_data_dict: dict[str, str] = {'filename': user_input, 'text': user_data.binary_to_ascii()}
            if(algo == 1): #BM
                ans = listBM(data, user_data.binary_to_ascii())
                result: dict[str, str] = ans.result()
                print(user_data_dict)
                print(result)
                pass
            elif(algo == 2): #KMP
                ans = listKMP(data, user_data.binary_to_ascii())
                result: dict[str, str] = ans.result()
                print(result)
                pass
            # print(data)

def choose_algo(start: int, end: int, msg: str) -> int:
    ans: int = int(input(msg))
    while(ans < start or ans > end):
        print("input tidak valid")
        print("Masukkan antara " + str(start) + "-" + str(end))
        ans = int(input(msg))
    return ans
        
main()