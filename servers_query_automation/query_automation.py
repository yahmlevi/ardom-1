import sqlite3
import xlsxwriter
import xlrd
import pandas as pd
import re


def init():

    # create handle to write to Excel
    # xl_answers_path = "D:\\projects\\ardom-1\\servers_query_automation\\query_answers.xlsx"
    # TODO
    xl_answers_path = "ENTER PATH TO SAVE ANSWERS HERE"
    workbook = xlsxwriter.Workbook(xl_answers_path)

    # create handle to read Excel
    # TODO
    xl_query_to_os_path = "ENTER PATH TO QUERIES EXCEL"
    df = pd.read_excel(xl_query_to_os_path)

    # get desired queries from user and put into list
    user_selected_queries = input("what queries would you like to execute? (query_name1,query_name2,...query_nameN, query_nameN+1\n") 
    user_selected_queries_list = user_selected_queries.split(",")

    # TODO
    hostname_list = ["ENTER HOSTNAME LIST (ardom-as7"]

    return workbook, df, user_selected_queries_list, hostname_list


def get_os_version(hostname):
    import subprocess
    server_os_version_binary = subprocess.check_output('systeminfo | findstr /B /C:"OS Name" \\ {}' .format(hostname), stderr=subprocess.STDOUT, shell=True)
    # server_os_version_binary = subprocess.check_output('systeminfo | findstr /B /C:"OS Name"', stderr=subprocess.STDOUT, shell=True)
    server_os_version_str = server_os_version_binary.decode('ascii')
    server_os_version = server_os_version_str[27:]
    
    return server_os_version


def classify_queries(selected_queries):
    # TODO
    # implement true classify function (depends on queries)
    shell_query_list = []
    powershell_query_list = []

    # classifies to shell queries only
    for query in selected_queries:
        if query.islower:
            shell_query_list.append(query)
        else:
            powershell_query_list.append(query) 
        
    return shell_query_list, powershell_query_list


def execute_query_on_server(query, query_type, hostname):
    import subprocess

    if query_type == "shell":
        subprocess = subprocess.Popen('{} \\ {}' .format(qeury, hostname), shell=True, stdout=subprocess.PIPE)
        # subprocess = subprocess.Popen('{}' .format(query), shell=True, stdout=subprocess.PIPE)
        answer = subprocess.stdout.read()

    if query_type == "powershell":
        subprocess.Popen('powershell -command {} \\ {}' .format(qeury, hostname), shell=True, stdout=subprocess.PIPE)
        # subprocess.Popen('powershell -command {}' .format(qeury), shell=True, stdout=subprocess.PIPE)
        answer = subprocess.stdout.read()

    return answer



def get_queries_to_execute(df, user_selected_queries_list):
        row = df[df["OS VERSION"] == server_os_version]
        # row = df[df["OS VERSION"] == "os version 6"]
        query_dict = row.to_dict()
        os_specific_query_key_list = list(query_dict.keys())
        selected_queries_key_list = list(set(os_specific_query_key_list).intersection(user_selected_queries_list))
        queries_to_execute_list = []
        for key in query_dict:
            for item in selected_queries_key_list:
                if key == item:
                    temp = query_dict[key]
                    queries_to_execute_list.append(str(temp).split("'")[1])
        
        return queries_to_execute_list






if __name__ == "__main__":
    

    workbook, df, user_selected_queries_list, hostname_list = init()

    # get answers for selected queries each server at a time
    for hostname in hostname_list:
        
        worksheet = workbook.add_worksheet(hostname)

        try:
            server_os_version = get_os_version(hostname)
            # server_os_version = get_os_version()
            print("get_os_version returned - {}" .format(server_os_version))

        except:
            print("could not get server's OS version")
            break

        # get list of queries to execute
        queries_to_execute_list = get_queries_to_execute(df, user_selected_queries_list)

        # classify queries to powershell/shell queries
        shell_queries, powershell_queries = classify_queries(queries_to_execute_list)
        
        i = 0
        for qeury in powershell_queries:
            answer = execute_query_on_server(qeury, "powershell", hostname)
            # answer = execute_query_on_server(qeury, "powershell")
            worksheet.write(i, 0, "PowerShell - {}" .format(query))
            worksheet.write(i, 1, answer.decode('utf-8'))
            i += 1
        
        for query in shell_queries:
            answer = execute_query_on_server(qeury, "shell", hostname)
            # answer = execute_query_on_server(query, "shell")
            worksheet.write(i, 0, "Shell - {}" .format(query))
            worksheet.write(i, 1, answer.decode('utf-8'))
            i += 1
        
    workbook.close()
