import os
import re
from insert_to_excel import Excel
from datetime import datetime
from hurry.filesize import size


# get path from user and cd to it
path = input("Enter Desired Path:")
os.chdir(path)

#path = "D:\projects\ardom-1"

class File:
    pass

class Totals:
    pass

def get_modified_year(file_name):
  modified_date = str(datetime.fromtimestamp(os.stat(file_name).st_mtime))
  modified_year = modified_date.split("-")
  return modified_year[0]

# TODO - complete function
def get_file_size_in_mg(file_name):
    return size(os.stat(file_name).st_size)
    # return (os.stat(file_name).st_size)

def get_file_size(file_name):
    return os.stat(file_name).st_size

def get_file_type(file_name):
    filename, file_extension = os.path.splitext(file_name)
    if not file_extension:
        return "FOLDER"
    else: 
        return file_extension



def process_list(file_list, year_list, file_type_list):
    totals_list = []
   
    for year in year_list:
        for file_type in file_type_list:

            count, total_size = get_info_by_year_and_file_type(file_list, lambda file: file.year == year and file.file_type == file_type)

            if count > 0:
                totals = Totals()
                totals.year = year
                totals.file_type = file_type
                totals.total_size = total_size
                totals.total_size_str = size(total_size)
                totals.count = count
                totals_list.append(totals)
    return totals_list


def count_by_year_and_file_type(file_list, filter):
    result = 0
    for file in file_list:
        if filter(file): 
            result += 1
    return result


def get_info_by_year_and_file_type(file_list, filter):
    count = 0
    size = 0
    for file in file_list:
        if filter(file): 
            count += 1
            size += file.file_size
    return count, size

# nesting_level is 2 because we want to see 2 \'s and then we know its first level dirs from path
def filter_by_nesting_level(file_list, nesting_level=2):
    result = []
    for file in file_list:
        if file.path.count("\\") >= nesting_level:
            result.append(file)          
    return result

def filter_by_nesting_level_2(file_list, nesting_level=2):
    result = {}
    for file in file_list:
        split_str = file.root.split("\\")
        # for i in split_str:
        #     print(i)

        if len(split_str) > 1:
            key = split_str[1]
            if key not in result.keys():
                result[key] = []

            if file.path.count("\\") >= nesting_level:
                result[key].append(file)

    return result


def populate_list():
    file_list = []
    year_list = []
    file_type_list = []

    for root, dirs, files in os.walk(".", topdown=False):
        #print ("root: " + root)

        # for dir_name in dirs:
        #     #  for root, dirs, files in os.walk(".", topdown=False):
        #     print(dir_name)    


        for file_name in files:

            file = File()

            file.root = root
            file.path = os.path.join(root, file_name)
            file.year = get_modified_year(file.path)
            file.file_type = get_file_type(file.path)
            # file.file_size = get_file_size_in_mg(file.path)
            file.file_size = get_file_size(file.path)

            file_list.append(file)

            #print("---" + file.path)

            if file.year not in year_list:
                year_list.append(file.year)

            if file.file_type not in file_type_list:
                file_type_list.append(file.file_type)

    return file_list, year_list, file_type_list

def print_files(file_list):
    for file in file_list:
        # print(file.year + ", " + file.path)
        print(file.root + ", " + file.path)




file_list, year_list, file_type_list= populate_list()

totals_list = process_list(file_list, year_list, file_type_list)

#totals_list_filtered = process_list(filter_by_nesting_level(file_list), year_list, file_type_list)

def print_totals(totals_list):
    for totals in totals_list:
        print (totals.year + " " + totals.file_type + " count: " + str(totals.count) + " size in bytes: " + str(totals.total_size) + " size: " + totals.total_size_str)
#    print (totals.year)
#    print(totals.file_type)
#    print(totals.count)

excel = Excel()

excel.insert_to_root(totals_list, path)
#insert_to_excel.insert_to_excel_subroot(totals_list_filtered, path)

#print_files(file_list)

# for totals in totals_list_filtered:
#         print(totals.year + ", " + str(totals.total_size))

d = filter_by_nesting_level_2(file_list)

for sub_path in d.keys():
    file_list = d[sub_path]
    totals_list = process_list(file_list, year_list, file_type_list)
    # print_totals(totals_list)
    print("")
    print (sub_path)
    print ("------------------------------------------------------")
    print_totals(totals_list) 
    excel.insert_to_subroot(totals_list, sub_path) 

excel.close()

