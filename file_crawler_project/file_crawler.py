import os
import re
import sys   
from insert_to_excel import Excel
from datetime import datetime
from hurry.filesize import size
import win32api
import win32con
from pandas_crawler import Panda
import ctypes
from ctypes import wintypes


#from functools import reduce



class File:
    
    def get_sizes(self, clusterSize):
            # FILE SIZE ON DISK 
        #file_name.replace("\\", "\\\\")
        #path = u'D:\\projects\\ardom-1\\file_crawler_project\\insert_to_excel.py'
        
        winlib = ctypes.CDLL('C:\Windows\System32\kernel32.dll')
        hosize = wintypes.DWORD()
        losize = winlib.GetCompressedFileSizeW(self.path, ctypes.byref(hosize))
        size = hosize.value << 32 | losize

        # FILE LOGICAL SIZE
        # return os.stat(file_path).st_size
        
        self.file_size = size

        # FILE SIZE ON DISK
        size_on_disk = int(((size + clusterSize - 1) / clusterSize)) * clusterSize

        self.file_size_on_disk = size_on_disk
        
        return size, size_on_disk

    def to_dict(self):
        # if os.path.isdir(self.path):
        #if "." not in self.path.split("\\")[1]:
        #    sub_root = self.path.split("\\")[1]
        #else:
        #    sub_root = ''
        # and len(self.path.split("\\")) < 0
        if len(self.path.split("\\")) > 2:
            sub_root = self.path.split("\\")[1]
        else:
            sub_root = ''
        
        if len(self.path.split("\\")) >= 4:
            sub_sub_root = self.path.split("\\")[2]
        else:
            sub_sub_root = ''
        

        return {
            'File Path': self.path,
            'File Root': self.root,
            'Year': self.year,
            'File Type': self.file_type,
            'File Size': self.file_size,
            'File Size On Disk': self.file_size_on_disk,
            'Logical Size GB': float(self.logical_gb),
            'File Size GB': float(self.file_size_in_gb),
            'Restricted': self.restricted,
            'Sub-Root': sub_root,
            'Sub-Sub-Root': sub_sub_root
            
        }


class Totals:
    def to_dict(self):
        return {
            'Count': self.count,
            'Year': self.year,
            'File Type': self.file_type       
        }


class Dir:
    def to_dict(self):
        return {
            'Count': self.count,
            'Year': self.year,
            'File Type': self.file_type       
        }


def get_modified_year(file_name):
  modified_date = str(datetime.fromtimestamp(os.stat(file_name).st_mtime))
  modified_year = modified_date.split("-")
  return modified_year[0]

def get_file_size_in_gb(size_in_bytes):
    # return size(os.stat(file_name).st_size)
    #return "%.2f" % (size_in_bytes / (1024*1024*1024))
    return "%.4f" % (size_in_bytes / (1024*1024*1024))


def get_cluster_size(directory = None):
    winlib = ctypes.CDLL('C:\Windows\System32\kernel32.dll')
  
    sectorsPerCluster = wintypes.DWORD()
    bytesPerSector = wintypes.DWORD()
    numberOfFreeClusters = wintypes.DWORD()
    TotalNumberOfClusters = wintypes.DWORD()

    bool_return = winlib.GetDiskFreeSpaceW(directory, 
                                ctypes.byref(sectorsPerCluster),
                                ctypes.byref(bytesPerSector), 
                                ctypes.byref(numberOfFreeClusters),
                                ctypes.byref(TotalNumberOfClusters))

    clusterSize = sectorsPerCluster.value * bytesPerSector.value

    return clusterSize


def get_file_size(file_path):
    # FILE SIZE ON DISK 
    #file_name.replace("\\", "\\\\")
    #path = u'D:\\projects\\ardom-1\\file_crawler_project\\insert_to_excel.py'
    path = 'u' + file_path
    winlib = ctypes.CDLL('C:\Windows\System32\kernel32.dll')

    hosize = wintypes.DWORD()
    losize = winlib.GetCompressedFileSizeW(path, ctypes.byref(hosize))
    size = hosize.value << 32 | losize
    
    sectorsPerCluster = wintypes.DWORD()
    bytesPerSector = wintypes.DWORD()
    NumberOfFreeClusters = wintypes.DWORD()
    TotalNumberOfClusters = wintypes.DWORD()

    bool_return = winlib.GetDiskFreeSpaceW(None, 
                                ctypes.byref(sectorsPerCluster),
                                ctypes.byref(bytesPerSector), 
                                ctypes.byref(NumberOfFreeClusters),
                                ctypes.byref(TotalNumberOfClusters))


    clusterSize = sectorsPerCluster.value * bytesPerSector.value

    size_on_disk = int(((size + clusterSize - 1) / clusterSize)) * clusterSize

    # FILE SIZE ON DISK
    return size_on_disk

    # FILE LOGICAL SIZE
    #return os.stat(file_path).st_size

def get_file_size_logical(file_path):
    # FILE LOGICAL SIZE
    return os.stat(file_path).st_size
    

def get_file_type(file_name):
    filename, file_extension = os.path.splitext(file_name)
    if not file_extension:
        return "FOLDER"
    else: 
        return file_extension


def get_totals_by_file_type(file_list, file_type_list):
    totals_list = []

    for file_type in file_type_list:

            count, total_size, total_size_on_disk = get_info_by_filter(file_list, lambda file: file.file_type == file_type and file.restricted == False)

            if count > 0:
                totals = Totals()
                totals.file_type = file_type
                #totals.total_size = total_size
                totals.total_size = get_file_size_in_gb(total_size)
                totals.total_size_str = size(total_size)
                totals.count = count
                totals_list.append(totals)
    return totals_list


def get_totals_by_year_and_file_type(file_list, year_list, file_type_list):
    totals_list = []
   
    for year in year_list:
        for file_type in file_type_list:

            count, total_size, total_size_on_disk = get_info_by_filter(file_list, lambda file: file.year == year and file.file_type == file_type and file.restricted == False)

            if count > 0:
                totals = Totals() 
                totals.year = year
                totals.file_type = file_type
                #totals.total_size = total_size
                
                totals.total_size = get_file_size_in_gb(total_size)
                totals.total_size_str = size(total_size)

                totals.count = count
                totals_list.append(totals)
    return totals_list


def get_totals(file_list):
    totals_list = []
   
    # the filter is always true (we take all files)
    count, total_size, total_size_on_disk = get_info_by_filter(file_list, lambda file: True)

    if count > 0:
        totals = Totals()
        #totals.total_size = total_size
        totals.total_size = get_file_size_in_gb(total_size)
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


def get_info_by_filter(file_list, filter):
    count = 0
    size = 0
    size_on_disk = 0
    for file in file_list:
        if filter(file): 
            count += 1
            size += file.file_size
            size_on_disk += file.file_size_on_disk
    return count, size, size_on_disk

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
        # check nesting level
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


def filter_list(file_list, filter):
    result = []
    for file in file_list:
        if filter:
            result.append(file)          
    return result



def populate_list(path):
    file_list = []
    year_list = []
    file_type_list = []
    restricted_files_list = []
    skip_all_condition = False
    restart = False

    clusterSize = get_cluster_size()
    

    for root, dirs, files in os.walk(".", topdown=False):
        # for dir_name in dirs:
        #     #  for root, dirs, files in os.walk(".", topdown=False):
        #     print(dir_name)    
        # print all first folders in user given root
        try:     
            split_str = root.split("\\")
            folder = split_str[1]
            print(folder)
            # x += 1
            # print(x)
        
        except:
            pass


        for file_name in files:

            file_path = os.path.join(root, file_name)
            file_type =  get_file_type(file_path)
            
            if file_type != "FOLDER":
                file = File()

                file.root = root
                file.path = file_path 
                file.file_type = file_type
            
                if os.access(file.path, os.R_OK):
                    file.restricted = False
                
                    try:    
                        file.year = get_modified_year(file.path) 
                    
                    except:

                        # pop-up message at end of run
                        win32api.MessageBox(None, "Script Found an Invalid date at - {}" .format(file.path), "Date Error", win32con.MB_OK | win32con.MB_ICONWARNING)    

                        if skip_all_condition is True:
                            continue

                        flag = True

                        while flag is True:

                            user_input = input("Choose whether you want to skip the file (input '1'), skip for all (input '2'), or delete the file automatically (input '3'):")
                            
                            if user_input == "1":
                                flag = False
                                restart = True

                            elif user_input == "2":
                                skip_all_condition = True
                                flag = False
                                restart = True
                                
                            elif user_input == "3":
                                os.remove(file.path)
                                flag = False
                                restart = True

                            else:
                                print("Invalid answer. Please answer only with '1','2', or '3'.")
                            
                    if restart is True:
                        continue
                            
                    file.get_sizes(clusterSize)

                    file.file_size = get_file_size_logical(file.path)
                    
                    file.logical_gb = get_file_size_in_gb(file.file_size)

                    file.file_size_in_gb = get_file_size_in_gb(file.file_size_on_disk)


                else:
                    file.restricted = True
                    file.year = None
                    file.file_size = None
                    file.file_size_in_gb = 0.0
                    
                file_list.append(file)

                

                if file.year not in year_list:
                    year_list.append(file.year)

                if file.file_type not in file_type_list:
                    file_type_list.append(file.file_type)
 

    # return file_list, year_list, file_type_list, restricted_files_list
    return file_list, year_list, file_type_list

def print_files(file_list):
    for file in file_list:
        print(file.root + ", " + file.path)


def print_totals(totals_list):
    for totals in totals_list:
        print (totals.year + " " + totals.file_type + " count: " + str(totals.count) + " size in bytes: " + str(totals.total_size) + " size: " + totals.total_size_str)


def main_excel():
    
    # get path from user and cd to it
    path = input("Enter Desired Path:")
    os.chdir(path)

    excel = Excel(path)

    # file_list, year_list, file_type_list, restricted_files_list = populate_list(path)
    file_list, year_list, file_type_list = populate_list(path)

    #
    # 1st tab - Root
    #
    totals_list = get_totals_by_year_and_file_type(file_list, year_list, file_type_list)
    excel.insert_to_root(totals_list, path)
    
    #
    # 2nd tab - Sub Root
    #
    d = filter_by_nesting_level_2(file_list)

    for sub_path in d.keys():
        _file_list = d[sub_path]
        _totals_list = get_totals_by_year_and_file_type(_file_list, year_list, file_type_list)
 
        excel.insert_to_subroot(_totals_list, sub_path, path)

    #
    # 3rd tab - totals 
    # 
    total_tab_totals_list = get_totals(file_list)

    for sub_path in d.keys():
        _file_list = d[sub_path]
        _totals_list = get_totals(_file_list)
        
        excel.insert_to_total(_totals_list, path, sub_path)

    #
    # 4th tab - Log Restricted
    #
    restricted_file_list = filter_list(file_list, lambda file: file.restricted == True)
    #excel.insert_to_restricted(restricted_file_list)


    #
    # 5th tab - Root by File Type
    #
    excel.insert_to_root_by_file_type(get_totals_by_file_type(file_list, file_type_list), path)

    # pop-up message at end of run
    win32api.MessageBox(None, "Excel Saved at: {}" .format(path), "Finished The Job!", win32con.MB_OK | win32con.MB_ICONWARNING)
    
    excel.close()



def root_pandas():
    # -----------------------------------------------------------------------------------------------
    # PANDAS
    
    # get path from user and cd to it
    path = input("Enter Desired Path:")
    os.chdir(path)

    file_list, year_list, file_type_list = populate_list(path)

    panda = Panda(file_list) 
    
    root, header_list = panda.pd_root(path)
    panda.to_csv(root, header_list, 'root')

    root_by_file_type, header_list = panda.pd_root_by_file_type(path)
    panda.to_csv(root_by_file_type, header_list, 'root_by_file_type')
    
    sub, header_list = panda.pd_subroot(path)
    panda.to_csv(sub, header_list, 'sub_root')

    total, header_list = panda.pd_total(path)
    panda.to_csv(total, header_list, 'total')

    restricted, header_list = panda.pd_restricted()
    path_ = panda.to_csv(restricted, header_list, 'restricted')

    bigger_then_one, header_list = panda.bigger_then_one_gb()
    panda.to_csv(bigger_then_one, header_list, 'bigger_then_one_gb')

    #custom_file, header_list = panda.custom_file_type()
    #panda.to_csv(custom_file, header_list, 'custom_file_type')

    #custom_sub_sub, header_list = panda.custom_sub_sub_analsys()
    #panda.to_csv(custom_sub_sub, header_list, 'custom_sub_sub_analsys')


    # pop-up message at end of run
    win32api.MessageBox(None, "Saved CSV's Folder at: {}" .format(path_), "Pandas Finished !!", win32con.MB_OK | win32con.MB_ICONWARNING)

def custom_file_pandas(file_extensions):
    
    path = input("Enter Desired Path:")
    os.chdir(path)

    file_list, year_list, file_type_list = populate_list(path)
    panda = Panda(file_list) 

    custom_file, header_list = panda.custom_file_type(file_extensions)
    path_ = panda.to_csv(custom_file, header_list, 'custom_file_type')

    # pop-up message at end of run
    win32api.MessageBox(None, "Saved CSV's Folder at: {}" .format(path_), "Pandas Finished !!", win32con.MB_OK | win32con.MB_ICONWARNING)


def custom_sub_sub(custom_sub_sub_var):

    path = input("Enter Desired Path:")
    os.chdir(path)

    file_list, year_list, file_type_list = populate_list(path)
    panda = Panda(file_list)

    custom_sub_sub, header_list = panda.custom_sub_sub_analsys(custom_sub_sub_var)
    path_ = panda.to_csv(custom_sub_sub, header_list, 'custom_sub_sub_analsys')

    # pop-up message at end of run
    win32api.MessageBox(None, "Saved CSV's Folder at: {}" .format(path_), "Pandas Finished !!", win32con.MB_OK | win32con.MB_ICONWARNING)





    

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
# Call your FAVORITE 'main' !

if sys.argv[1] == "root":
    root_pandas()
elif sys.argv[1] == "custom file type":
    file_extensions = input("Enter File Type Extensions with comma between (.txt,.mp4,.avi): ")
    custom_file_pandas(file_extensions.lower())
else:
    custom_sub_sub_var = input("Enter Sub-Sub-Root to analyze: ")
    custom_sub_sub(custom_sub_sub_var)

# call pandas crawler
# root_pandas()
# custom_file_pandas()
# custom_sub_sub

# call excel crawler
#main_excel()