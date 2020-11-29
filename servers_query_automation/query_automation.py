import subprocess
import sqlite3
import xlsxwriter
import xlrd
import pandas as pd
import re


# GET INPUT FROM XL FILE

def init():

    # Create an new Excel file and add a worksheet
    xl_answers_path = "D:\\projects\\ardom-1\\servers_query_automation\\servers_query_answers.xlsx"
    workbook = xlsxwriter.Workbook(xl_answers_path)

    # create handle for reading Excel
    xl_query_to_os_path = "D:\\projects\\ardom-1\\servers_query_automation\\queries.xlsx"
    df = pd.read_excel(xl_query_to_os_path)

    # get desired queries from user and put into list
    user_selected_queries = input("what queries would you like to execute? (query_name1,query_name2,...query_nameN, query_nameN+1\n") 
    user_selected_queries_list = user_selected_queries.split(",")

    # hostname_list = ['ardom-as8', 'ardom-adr9', 'ardom-at3']
    hostname_list = ['ardom-as8', 'ardom-adr9', 'ardom-adr10']

    return workbook, df, user_selected_queries_list, hostname_list


def get_os_version(hostname=None):
    #server_os_version_binary = subprocess.check_output('systeminfo | findstr /B /C:"OS Name" \\ {}' .format(hostname), stderr=subprocess.STDOUT, shell=True)
    server_os_version_binary = subprocess.check_output('systeminfo | findstr /B /C:"OS Name"', stderr=subprocess.STDOUT, shell=True)
    server_os_version_str = server_os_version_binary.decode('ascii')
    server_os_version = server_os_version_str[27:]
    
    return server_os_version

def classify_queries(selected_queries):
    pass


if __name__ == "__main__":
    

    workbook, df, user_selected_queries_list, hostname_list = init()

    # get answers for selected queries each server at a time
    for hostname in hostname_list:
        
        worksheet = workbook.add_worksheet(hostname)

        try:
            # server_os_version = get_os_version(hostname)
            server_os_version = get_os_version()
            print("get_os_version returned - {}" .format(server_os_version))

        except:
            print("could not get server's OS version")
            break

        # get list of queries of secific OS version
        # all_querys = df[df["OS VERSION"] == server_os_version]
        row = df[df["OS VERSION"] == "os version 6"]
        query_dict = row.to_dict()
        os_specific_query_key_list = list(query_dict.keys())
        selected_queries_key_list = list(set(os_specific_query_key_list).intersection(user_selected_queries_list))
        queries_to_execute_list = []
        for key in query_dict:
            for item in selected_queries_key_list:
                if key == item:
                    temp = query_dict[key]
                    # TODO 
                    # extract query from temp str
                    # print(temp)
                    queries_to_execute_list.append(temp)
        print(queries_to_execute_list)
            #print(query_dict)

        #print("test - {}" .format(temp))
        #os_specific_query_list = temp[1:]
        #print("list of queries specific to OS version - {}" .format(os_specific_query_list))
        
        
    #     # classify queries to powershell/cmd queries
    #     powershell_queries, shell_queries = classify_queries(selected_queries)
        
    #     i = 0
    #     for qeury in powershell_queries:
    #         # answer = subprocess.check_output('powershell -command {} \\ {}' .format(qeury, hostname), stderr=subprocess.STDOUT, shell=True)
    #         # TODO
    #         # PUT answers in CSV
    #         worksheet.write(i, 0, query)
    #         worksheet.write(i, 1, answer)
    #         i += 1
    #         print(qeury)

    #     for qeury in shell_queries:
    #         # answer = subprocess.check_output('{} \\ {}' .format(qeury, hostname), stderr=subprocess.STDOUT, shell=True)
    #         # TODO
    #         # PUT answers in CSV
    #         worksheet.write(i, 0, query)
    #         worksheet.write(i, 1, answer)
    #         i += 1
    #         print(qeury) 

    workbook.close()
