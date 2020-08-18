import os
import re
from datetime import datetime
from hurry.filesize import size

# get path from user and cd to it
path = input("Enter Desired Path:")
# path = "\projects\tests"
os.chdir(path)

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



def populate_list():
    file_list = []
    year_list = []
    file_type_list = []
    file_counter = 0

    for root, dirs, files in os.walk(".", topdown=False):
        for file_name in files:
            file_counter += 1

            file = File()
            file.path = os.path.join(root, file_name)
            file.year = get_modified_year(file.path)
            file.file_type = get_file_type(file.path)
            # file.file_size = get_file_size_in_mg(file.path)
            file.file_size = get_file_size(file.path)

            file_list.append(file)

            if file.year not in year_list:
                year_list.append(file.year)

            if file.file_type not in file_type_list:
                file_type_list.append(file.file_type)

    return file_list, year_list, file_type_list


file_list, year_list, file_type_list= populate_list()

# for file in file_list:
#     print(file.year + ", " + file.file_type)

#print(file_list)
# print(year_list)
# print(file_type_list)

totals_list = process_list(file_list, year_list, file_type_list)

for totals in totals_list:
    print (totals.year + " " + totals.file_type + " count: " + str(totals.count) + " size: " + str(totals.total_size) + " size str: " + totals.total_size_str)
#    print (totals.year)
#    print(totals.file_type)
#    print(totals.count)
