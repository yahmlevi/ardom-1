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
    user_selected_queries = "query 1,query 2, query 3"
    #user_selected_queries = input("what queries would you like to execute? (query_name1,query_name2,...query_nameN, query_nameN+1\n") 
    user_selected_queries_list = user_selected_queries.split(",")
    
    return workbook, df, user_selected_queries_list


def execute_query_on_server(query, query_type, hostname):
    import subprocess

    if query_type == "shell":
        q = '{}' .format(query)
        
    elif query_type == "powershell":
        q = 'powershell -command {}' .format(query)
    
    subprocess = subprocess.Popen(q, shell=True, stdout=subprocess.PIPE)
    
    try:
        answer_temp = subprocess.communicate(timeout=0.5)
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
    
    # TODO
    # selected_query_keys = list(set(os_specific_query_key_list).intersection(user_selected_queries_list))
    selected_query_keys = os_specific_query_key_list 
    
    # queries to execute (dictionary query_name/query)
    results = {}
    for key in query_dict:
        if key in selected_query_keys:
            temp = query_dict[key]
            query = str(temp).split("'")[1]
            
            # key is the query name 
            results[key] = query
    
    return results


def extract_hostname_os_version_dict():
    hostname_os_version_dict = {}

    #---------------------------------------------
    query = "Import-module activedirectory; Get-ADComputer -Filter 'Name -like \"*\"' -Properties OperatingSystem"
    p = subprocess.Popen(["powershell.exe", '{}'.format(query) ], stdout=subprocess.PIPE)
    res = p.communicate()
    batches = res[0].decode("utf-8").split("DistinguishedName")
    # with open("Process.txt") as fp:
    #     temp = fp.read()
    #     batches = temp.split("DistinguishedName")
    # #---------------------------------------------
    
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

    # i = 0
    # if worksheet_name == "ERROR":
    #     row_index = i


    worksheet = workbook.get_worksheet_by_name(worksheet_name)
    worksheet.write(row_index, 0, "SERVER NAME - {}" .format(hostname))
    worksheet.write(row_index, 1, "QUERY TYPE - {}" .format(query_type)) 
    worksheet.write(row_index, 2, "QUERY - {}" .format(query))
    worksheet.write(row_index, 3, query_result)

    # i += 1


workbook, df, user_selected_queries_list = init()

try:
    hostname_os_version_dict = extract_hostname_os_version_dict()
    print("extracted data from Process.txt file")

except:
    print("FATEL ERROR - failed to extract data from Process.txt")
    sys.exit()


# keep track of the worksheet next blank row index
FIRST_ROW_INDEX = 0
worksheets = {}

error_worksheet = workbook.add_worksheet("ERROR")
error_worksheet.set_column(0, 10, 50)

# add the error worksheet to the worksheets dictionary
worksheets["ERROR"] = FIRST_ROW_INDEX

# get answers for selected queries each server at a time
for hostname in hostname_os_version_dict:

    if not hostname:
        continue

    server_os_version = hostname_os_version_dict[hostname]
    
    try:
        # get list of queries to execute
        queries_to_execute = get_queries_to_execute(df, user_selected_queries_list, server_os_version)
        print("Got list of queries to execute")
    except:
        print("Could not find queries to execute for hostname {}, please add queries to Excel" .format(hostname)) 
        continue

    # loop through the keys of queries_to_execute dictionary
    for query_name in queries_to_execute:
        
        if queries_to_execute[query_name] is queries_to_execute["OS VERSION"]:
            continue

        full_query = queries_to_execute[query_name]
        temp = full_query.split("-")
        
        if temp[0].strip() == "cmd":
            query_type = "shell"
        elif temp[0].strip() == "powershell":
            query_type = "powershell"
        else:
            print ("Invalid query type " + temp[0].strip())
            
        query = temp[1].strip()
        query = query.replace("{{dns}}", hostname)
        query = query.replace("\\\\", "\\")
            
        # create worksheet if needed
        if query_name not in worksheets:
            new_worksheet = workbook.add_worksheet(query_name)
            new_worksheet.set_column(0, 10000, 50)
            
            # add new worksheet to worksheets dictionary
            worksheets[query_name] = FIRST_ROW_INDEX

        query_result = execute_query_on_server(query, query_type, hostname)
        
        if query_result == "ERROR":
            print("ERROR - could not execute on ", hostname)

            worksheet_name = "ERROR"
        else:
            print("executed successfully on ", hostname)

            worksheet_name = query_name


        row_index = worksheets[worksheet_name

        write_to_worksheet(workbook, worksheet_name, row_index, hostname, query_type, query, query_result)

        # increment the row index by 1
        worksheets[worksheet_name] = row_index + 1

worksheet = workbook.add_worksheet("SERVER'S OS VERSION")
worksheet.set_column(0, 100, 50)

i = 0
for hostname in hostname_os_version_dict:
    worksheet.write(i, 0, "SERVER NAME - {}" .format(hostname))
    worksheet.write(i, 1, "OS VERSION - {}" .format(hostname_os_version_dict[hostname]))
    i += 1

# close workbook   
workbook.close()
print("FINISH - please look at query_answers.xlsx")