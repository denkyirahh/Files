# Author - Michael Asomani        Date - 9/30/21
# Purpose - Take the years from the program to see if its a leap year or not

import sys

# function to convert string to year

def convert_num(test_str):
    test_int = int(0)
    count_int = int(0)
    smallest_num = int(50)
    largest_num = int(0)

    if(test_str.isalpha() == True):
        pass
    elif(test_str.isspace() == True):
        pass
    elif(test_str.isdecimal() == True):
        test_int = int(test_str)
        test_leap_year(test_int)
    elif(test_str.isprintable() == True):
        for x in range(len(test_str)):
            if test_str[x].isdigit() == True:
                if x + 1 == len(test_str):
                    if x < smallest_num:
                        smallest_num = x
                    elif x > largest_num:
                        largest_num = x
                        test_int = int(test_str[smallest_num:largest_num+1])   
                
                elif test_str[x+1].isdigit() == False:
                    if count_int == 3:
                        if x < smallest_num:
                            smallest_num = x
                        elif x > largest_num:
                            largest_num = x
                            test_int = int(test_str[smallest_num:largest_num+1])  
                    else:
                        break
                elif x < smallest_num:
                    smallest_num = x
                elif x > largest_num:
                    largest_num = x
                    test_int = int(test_str[smallest_num:largest_num+1])      

                
                count_int += 1
                test_leap_year(test_int)
                
            else:
                pass

# function to test if year is a leap year

def test_leap_year(leap_int):
    
       test_year = int(leap_int)
       
       if test_year >= 1583 and test_year < 10000:
           if test_year % 4 == 0 and test_year % 100 != 0:
               print_year(test_year)
           elif test_year % 400 == 0:
               print_year(test_year)
           else:
               pass
       else:
           pass
        
# prints out leap years        

def print_year(year_int):

    lpyr_str = ""
    lpyr_int = int(year_int)
    lpyr_str = lpyr_int

    print(lpyr_str)

# try and catch for the text files

try:
    input_file = open("all_years.txt", "r")
    
    for line_str in input_file:
        line_str = line_str.strip()
        convert_num(line_str)
   
    input_file.close()
except LineError:
    SystemExit(0)
except FileNotFoundError:
    print("File not found.")
    sys.exit(0)
    




