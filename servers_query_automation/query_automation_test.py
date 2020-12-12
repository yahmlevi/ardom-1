import sqlite3
import xlsxwriter
import xlrd
import pandas as pd
import re
import subprocess, sys

# init powershell
# Import-module activedirectory 
# Get-ADComputer -Filter 'Name -like "*"' -Properties OperatingSystem | Out-File -FilePath ./process.txt

def init():

    # create handle to write to Excel
    xl_answers_path = ".\query_answers.xlsx"
    workbook = xlsxwriter.Workbook(xl_answers_path)

    # create handle to read Excel
    xl_query_to_os_path = ".\queries.xlsx"
    df = pd.read_excel(xl_query_to_os_path)

    # get desired queries from user and put into list
    user_selected_queries = "query 1,query 2"
    #user_selected_queries = input("what queries would you like to execute? (query_name1,query_name2,...query_nameN, query_nameN+1\n") 
    user_selected_queries_list = user_selected_queries.split(",")
    
    return workbook, df, user_selected_queries_list


def classify_queries(selected_queries):
    shell_query_list = []
    powershell_query_list = []
    for query in selected_queries:
        temp = query.split("-")
        if temp[0].strip() == "cmd":
            shell_query_list.append(temp[1].strip())
        elif temp[0].strip() == "powershell":
            powershell_query_list.append(temp[1].strip())
    return shell_query_list, powershell_query_list


def execute_query_on_server(query, query_type, hostname):
    import subprocess
    query = query.replace("{{dns}}", hostname)
    q = '{}' .format(query.replace("\\\\","\\"))
    if query_type == "shell":
        subprocess = subprocess.Popen(q, shell=True, stdout=subprocess.PIPE)
        try:
            answer_temp = subprocess.communicate()
            answer = answer_temp[0].decode("utf-8")
        except:
            answer = "ERROR"
    return answer
        # subprocess = subprocess.Popen(q, shell=True, stdout=subprocess.PIPE)
        # answer = subprocess.stdout.read()
    # if query_type == "powershell":
    #     q = 'powershell -command {}' .format(query)
    #     subprocess = subprocess.Popen(q, shell=True, stdout=subprocess.PIPE)
    #     answer = subprocess.stdout.read()
    # elif answer:
    #     return answer
    # else:
    #     return "ERROR"

def get_queries_to_execute(df, user_selected_queries_list, server_os_version):
    row = df[df["OS VERSION"] == server_os_version]
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

def extract_hostname_os_version_dict():
    hostname_os_version_dict = {}
    query = "Import-module activedirectory; Get-ADComputer -Filter 'Name -like \"*\"' -Properties OperatingSystem"
    p = subprocess.Popen(["powershell.exe", '{}'.format(query) ], stdout=subprocess.PIPE)
    res = p.communicate()
    batches = res[0].decode("utf-8").split("DistinguishedName")
    temp_list = []
    for batch in batches:
        i = 0
        for line in batch.split("\n"):
            if "DNSHostName" in line or "OperatingSystem" in line:
                line.split(":")
                temp_list.append(line)
    it = iter(temp_list)
    for x in it:
        temp = next(it)
        temp1 = x.split(":")
        temp2 = temp.split(":")
        hostname_os_version_dict[temp1[1].strip()] = temp2[1].strip()     
    return hostname_os_version_dict



# TODO
# TAB to every query NOT to every hostname



if _name_ == "_main_":
    workbook, df, user_selected_queries_list = init()
    try:
        hostname_os_version_dict = extract_hostname_os_version_dict()
        print("extracting data from txt file")
    except:
        print("failed to extract data from txt")

    # every query - NOT every hostname
    worksheet = workbook.add_worksheet("SUCCESS")
    error_worksheet = workbook.add_worksheet("ERROR")
    error_worksheet.set_column(0, 10000, 50)
    worksheet.set_column(0, 10000, 50)

    i = 0
    x = 0
        
    # # get answers for selected queries each server at a time
    for hostname in hostname_os_version_dict:
        server_os_version = hostname_os_version_dict[hostname]
        
        try:
            # get list of queries to execute
            queries_to_execute_list = get_queries_to_execute(df, user_selected_queries_list, server_os_version)
            # print("got list of queries to execute")
        except:
            # print("had no queries to execute for {}, please add queries to Excel" .format(hostname)) 
            continue
        
        # classify queries to powershell/shell queries
        shell_queries, powershell_queries = classify_queries(queries_to_execute_list)


        # for query in powershell_queries:
        #     answer = execute_query_on_server(query, "powershell", hostname)
        #     print()
    #         if answer == "ERROR":
    #             print("ERROR - could not execute on ", hostname)
    #             error_worksheet.write(x, 0, "SERVER NAME - {}" .format(hostname))
    #             error_worksheet.write(x, 1, "QUERY TYPE - {}" .format("PowerShell"))
    #             error_worksheet.write(x, 2, "QUERY - {}" .format(query)) 
    #             error_worksheet.write(x, 3, answer)
    #             x += 1
    #         else:
    #             print("executed successfully on ", hostname)
    #             worksheet.write(i, 0, "SERVER NAME - {}" .format(hostname))
    #             worksheet.write(i, 1, "QUERY TYPE - {}" .format("PowerShell"))
    #             worksheet.write(i, 2, "QUERY - {}" .format(query))
    #             worksheet.write(i, 3, answer.decode('utf-8'))
    #             i += 1
        
        for query in shell_queries:
            answer = execute_query_on_server(query, "shell", hostname)
            if answer == "ERROR":
                print("ERROR - could not execute on ", hostname)
                error_worksheet.write(x, 0, "SERVER NAME - {}" .format(hostname))
                error_worksheet.write(x, 1, "QUERY TYPE - {}" .format("CMD"))
                error_worksheet.write(x, 2, "QUERY - {}" .format(query.replace("{{dns}}", hostname))) 
                error_worksheet.write(x, 3, answer)
                x += 1
                print("x-" + str(x))
               
            else:
                print("executed successfully on ", hostname)
                worksheet.write(i, 0, "SERVER NAME - {}" .format(hostname))
                worksheet.write(i, 1, "QUERY TYPE - {}" .format("CMD"))
                worksheet.write(i, 2, "QUERY - {}" .format(query.replace("{{dns}}", hostname)))
                worksheet.write(i, 3, answer)
                i += 1
                print("i-" + str(i))

        if i > 100:
            break
        if x > 100:
            break         
    workbook.close()