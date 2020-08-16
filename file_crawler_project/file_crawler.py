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
            totals = Totals()
            totals.year = year
            totals.file_type = file_type
            type_in_years = count_by_year_and_file_type(file_list, lambda file: file.year == year and file.file_type == file_type)
            totals_list.append(totals)
    return totals_list, type_in_years


def count_by_year_and_file_type(file_list, filter):
    result = 0
    for file in file_list:
        if filter(file): 
            result += 1
    return result


def populate_list():
    file_list = []
    year_list = []
    file_size_list = []
    file_counter = 0
    for root, dirs, files in os.walk(".", topdown=False):
        for file_name in files:
            file_counter += 1
            file = File()
            file.year = get_modified_year(os.path.join(root, file_name))
            file.file_type = get_file_type(os.path.join(root, file_name))
            file.file_size = get_file_size_in_mg(os.path.join(root, file_name))
            file_list.append(file)
            if file.year not in year_list:
                year_list.append(file.year)
            if file.file_size not in file_size_list:
                file_size_list.append(file.file_size)
    return file_list, year_list, file_size_list


file_list, year_list, file_type_list= populate_list()

for file in file_list:
    print(file.year + ", " + file.file_type)
#print(file_list)
print(year_list)
print(file_type_list)

#totals_list, type_in_years = process_list(file_list, year_list, file_type_list)
#print(type_in_years)
#for totals in totals_list:
    #print (totals.year)
    #print(totals.file_type)
    #print(totals.count)
