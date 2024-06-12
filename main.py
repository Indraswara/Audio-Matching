from crawler import * 
from Algorithm.BM import *
from Algorithm.KMP import *
from Algorithm.listBM import *
from Algorithm.listKMP import *
from Algorithm.listBruteforce import *
from Converter.converter import *
import time 

number_of_times = 1000

def main(): 
    while(True): 
        print("Pilih algoritma")
        print("1. Boyer Moore")
        print("2. KMP")
        print("3. Bruteforce")
        print("4. Exit")
        algo = choose_algo(1, 3, "> ")
        user_input = str(input("Masukkan path audio yang akan dicari: "))
        if algo == 4: 
            break
        else:
            time_taken = 0
            data: list[dict[str, str]] = convert_all()
            user_data = converter(user_input)
            user_data_ascii = user_data.binary_to_ascii()
            user_data_dict: dict[str, str] = {'filename': user_input, 'text': user_data_ascii}
            if(algo == 1): #BM
                ans = listBM(data, user_data_ascii)
                start_time = time.time()
                result: dict[str, str] = ans.result()
                end_time  = time.time()
                print(user_data_dict)
                print(result)
                time_taken = end_time - start_time
            elif(algo == 2): #KMP
                ans = listKMP(data, user_data_ascii)
                start_time = time.time()
                result: dict[str, str] = ans.result()
                end_time = time.time()
                print(user_data_dict)
                print(result)
                time_taken = end_time - start_time
            elif(algo == 3): #Bruteforce 
                ans = listBruteforce(data, user_data_ascii)
                start_time = time.time()
                result: dict[str, str] = ans.result() 
                end_time = time.time()
                print(user_data_dict) 
                print(result)
                time_taken = end_time - start_time
            # print(data)
            if(time_taken < 0.001): 
                print("Time: < 0.001 Seconds" ) 
            else: 
                print("Time: " + str(time_taken))
        

def choose_algo(start: int, end: int, msg: str) -> int:
    ans: int = int(input(msg))
    while(ans < start or ans > end):
        print("input tidak valid")
        print("Masukkan antara " + str(start) + "-" + str(end))
        ans = int(input(msg))
    return ans
        
main()