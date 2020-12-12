import sqlite3
import xlsxwriter
import xlrd
import pandas as pd
import re
import subprocess, sys


# class QueryDetailes(object):
#     self.query = query 
#     self.query_name = query_name


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
    user_selected_queries = "query 1,query 2, query 3"
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
    
    # query = query.replace("{{dns}}", hostname)
    # query = query.replace("\\\\", "\\")

    print("TEST - ", query)

    if query_type == "shell":
        q = '{}' .format(query)
        
    elif query_type == "powershell":
        q = 'powershell -command {}' .format(query)
    
    subprocess = subprocess.Popen(q, shell=True, stdout=subprocess.PIPE)
    
    try:
        answer_temp = subprocess.communicate(timeout=1)
        answer = answer_temp[0].decode("utf-8")
    
    except:
        subprocess.kill()
        answer = "ERROR"
    
    if answer:
        return answer
    
    else:
        return "EMPTY"
    
def get_queries_to_execute(df, user_selected_queries_list, server_os_version):
    row = df[df["OS VERSION"] == server_os_version]
    query_dict = row.to_dict()
    os_specific_query_key_list = list(query_dict.keys())
    
    #TODO
    #selected_queries_key_list = list(set(os_specific_query_key_list).intersection(user_selected_queries_list))
    selected_queries_key_list = os_specific_query_key_list 
    
    queries_to_execute_list = []
    for key in query_dict:
        for item in selected_queries_key_list:
            if key == item:
                temp = query_dict[key]
                queries_to_execute_list.append(str(temp).split("'")[1])
        
    return queries_to_execute_list, query_dict

def extract_hostname_os_version_dict():
    hostname_os_version_dict = {}

    #---------------------------------------------
    # query = "Import-module activedirectory; Get-ADComputer -Filter 'Name -like \"*\"' -Properties OperatingSystem"
    # p = subprocess.Popen(["powershell.exe", '{}'.format(query) ], stdout=subprocess.PIPE)
    # res = p.communicate()
    # batches = res[0].decode("utf-8").split("DistinguishedName")
    with open("Process.txt") as fp:
        temp = fp.read()
        batches = temp.split("DistinguishedName")
    #---------------------------------------------
    
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

def write_to_worksheet(worksheet, hostname, query_type, query, query_result):
    worksheet.write(i, 0, "SERVER NAME - {}" .format(hostname))
    
    # Shell or PowerShell 
    if query_type == "shell":
        query_type = "CMD" 

    worksheet.write(i, 1, "QUERY TYPE - {}" .format(query_type)) 
    worksheet.write(i, 2, "QUERY - {}" .format(query))
    worksheet.write(i, 3, query_result)


# if _name_ == "_main_":

workbook, df, user_selected_queries_list = init()

try:
    hostname_os_version_dict = extract_hostname_os_version_dict()
    print("extracted data from Process.txt file")

except:
    print("failed to extract data from Process.txt")





i = 0
x = 0

worksheets = {}

error_worksheet = workbook.add_worksheet("ERROR")
error_worksheet.set_column(0, 10000, 50)

worksheets["ERROR"] = error_worksheet

# get answers for selected queries each server at a time
for hostname in hostname_os_version_dict:

    server_os_version = hostname_os_version_dict[hostname]
    
    try:
        # get list of queries to execute
        queries_to_execute_list, query_dict = get_queries_to_execute(df, user_selected_queries_list, server_os_version)
        print("got list of queries to execute")
    except:
        print("had no queries to execute for {}, please add queries to Excel" .format(hostname)) 
        continue
    
    # classify queries to powershell/shell queries
    # shell_queries, powershell_queries = classify_queries(queries_to_execute_list)
      
    for full_query in queries_to_execute_list:

        temp = full_query.split("-")

        if temp[0].strip() == "cmd":
            query_type = "shell"
            query = temp[1].strip()
            
        if temp[0].strip() == "powershell":
            query_type = "powershell"
            query = temp[1].strip()

        # user query_name ...

        query = query.replace("{{dns}}", hostname)
        query = query.replace("\\\\", "\\")
            
        # create worksheet if needed
        if query not in worksheets:
            new_worksheet = workbook.add_worksheet(query)
            new_worksheet.set_column(0, 10000, 50)

            worksheets[query] = new_worksheet

        # execute query
        query_result = execute_query_on_server(query, query_type, hostname)
        
        # query = query.replace("{{dns}}", hostname)
        # query = query.replace("\\\\", "\\")

        if query_result == "ERROR":
            print("ERROR - could not execute on ", hostname)
            current_worksheet = worksheets["ERROR"]
        else:
            print("executed successfully on ", hostname)
            current_worksheet = worksheets[query]
            
        write_to_worksheet(worksheet, hostname, query_type, query, query_result)
        i += 1
    
workbook.close()
