import sqlite3
import xlsxwriter
import xlrd
import pandas as pd
import re
import subprocess
import sys

# TODO
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
    #user_selected_queries = "query 1,query 2,query 3,net time"
    user_selected_queries = input("what queries would you like to execute? (query_name1,query_name2,...query_nameN, query_nameN+1\n") 
    user_selected_query_names = user_selected_queries.split(",")
    
    return workbook, df, user_selected_query_names


def execute_query_on_server(query, query_type, hostname):
    import subprocess

    if query_type == "shell":
        q = '{}' .format(query)
        
    elif query_type == "powershell":
        q = 'powershell -command {}' .format(query)

    p = subprocess.Popen(q, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    flag = False
    try:
        answer, error = p.communicate(timeout=0.5)
        answer = answer.decode('ascii')
        error = error.decode('ascii')
    except:
        answer = "TIMED OUT - PLEASE MAKE TIMEOUT BIGGER"
        flag = True

    if p.returncode != 0:
        if not flag:
            answer = error
        answer = str(answer)
        return (answer, 'ERROR')
        
    answer = str(answer)
    
    if answer:
        return (answer, "")
    
    else:
        return ("EMPTY","")
    

def get_queries_to_execute(df, user_selected_query_names, server_os_version):
    
    row = df[df["OS VERSION"] == server_os_version]
    query_dict = row.to_dict()

    # queries to execute (dictionary query_name/query)
    results = {}
    for query_name in query_dict:
        if query_name in user_selected_query_names:
            temp = query_dict[query_name]
            query = str(temp).split("'")[1]
            
            # key is the query name 
            results[query_name] = query
    
    return results


def extract_hostname_os_version_dict():
    hostname_os_version_dict = {}

    #---------------------------------------------
    # query = "Import-module activedirectory; Get-ADComputer -Filter 'Name -like \"*\"' -searchbase \"cn=computers, dc=ardomnet, dc=co, dc=il\" -Properties OperatingSystem, IPv4Address | sort-object name"
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


def write_to_worksheet(workbook, worksheet_name, row_index, hostname, query_type, query, query_result):
    
    # Shell or PowerShell 
    if query_type == "shell":
        query_type = "CMD" 

    worksheet = workbook.get_worksheet_by_name(worksheet_name)
    
    worksheet.write(row_index, 0, "{}" .format(hostname))
    #worksheet.write(row_index, 1, "{}" .format(query_type)) 
    worksheet.write(row_index, 1, "{}" .format(query))
    worksheet.write(row_index, 2, query_result)


def add_column_headers_to_worksheet(worksheet):
    worksheet.write(0, 0, "SERVER NAME")
    #worksheet.write(0, 1, "QUERY TYPE") 
    worksheet.write(0, 1, "QUERY")
    worksheet.write(0, 2, "RESULT")

def clean_query(dirty_query):
    temp = dirty_query.split("-")
    
    if temp[0].strip() == "cmd":
        query_type = "shell"
    elif temp[0].strip() == "powershell":
        query_type = "powershell"
    elif temp[0].strip() == "NONE":
        query_type = "NONE"
    else:
        print ("Invalid query type " + temp[0].strip())
    
    if query_type == "NONE":
        query = "NONE"
    else:
        query = temp[1].strip()
        query = query.replace("{{dns}}", hostname)
        query = query.replace("\\\\", "\\")

    return query, query_type


def execute_query(hostname, query_name, full_query):
    query, query_type = clean_query(full_query)

    # create worksheet if needed
    if query_name not in worksheets:
        new_worksheet = workbook.add_worksheet(query_name)
        new_worksheet.set_column(0, 10, 50)

        add_column_headers_to_worksheet(new_worksheet)

        # add new worksheet to worksheets dictionary
        worksheets[query_name] = FIRST_ROW_INDEX

    query_result = execute_query_on_server(query, query_type, hostname)
    
    if query_result[1] == "ERROR":
        print("ERROR - could not execute on ", hostname)

        worksheet_name = "ERROR"
    else:
        print("executed successfully on ", hostname)

        worksheet_name = query_name

    row_index = worksheets[worksheet_name]

    write_to_worksheet(workbook, worksheet_name, row_index, hostname, query_type, query, query_result[0])

    # increment the row index by 1
    worksheets[worksheet_name] = row_index + 1

            
workbook, df, user_selected_query_names = init()

try:
    hostname_os_version_dict = extract_hostname_os_version_dict()
    print("extracted data from Process.txt file")

except:
    print("FATEL ERROR - failed to extract data from Process.txt")
    sys.exit()


# keep track of the worksheet next blank row index
FIRST_ROW_INDEX = 1
worksheets = {}

error_worksheet = workbook.add_worksheet("ERROR")
error_worksheet.set_column(0, 10, 50)

add_column_headers_to_worksheet(error_worksheet)

# add the error worksheet to the worksheets dictionary
worksheets["ERROR"] = FIRST_ROW_INDEX

# get answers for selected queries each server at a time
for hostname in hostname_os_version_dict:

    if not hostname:
        continue

    server_os_version = hostname_os_version_dict[hostname]
    
    # -----
    try:
        # Getting the list of queries to execute (by OS version)
        queries_to_execute = get_queries_to_execute(df, user_selected_query_names, server_os_version)
        print("Got list of queries to execute")
    except:
        print("Could not find queries to execute for hostname {}, please add queries to Excel" .format(hostname)) 
        continue

    # loop through the keys of queries_to_execute dictionary
    for query_name in queries_to_execute:
        full_query = queries_to_execute[query_name]
        if full_query != "NONE":
            execute_query(hostname, query_name, full_query)
    # -----
    try:
        # Getting the list of univeral queries to execute
        queries_to_execute = get_queries_to_execute(df, user_selected_query_names, "ALL")
        print("Got list of univeral queries to execute")
    except:
        print("Could not find queries to execute for {}, please add queries to Excel" .format(hostname)) 
        continue
    
    for query_name in queries_to_execute:
        full_query = queries_to_execute[query_name]
        if full_query != "NONE":
            execute_query(hostname, query_name, full_query)
    # -----
      
worksheet = workbook.add_worksheet("SERVER'S OS VERSION")
worksheet.set_column(0, 100, 50)
worksheet.write(0, 0, "SERVER NAME")
worksheet.write(0, 1, "OS VERSION")
i = 1
for hostname in hostname_os_version_dict:
    worksheet.write(i, 0, "{}" .format(hostname))
    worksheet.write(i, 1, "{}" .format(hostname_os_version_dict[hostname]))
    i += 1

# close workbook   
workbook.close()
print("FINISH - please look at query_answers.xlsx")