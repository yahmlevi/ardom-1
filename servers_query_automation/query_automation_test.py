import sqlite3
import xlsxwriter
import xlrd
import pandas as pd
import re


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

    #query = query.replace("{{dns}}", hostname)
    query = "dir"
    
    if query_type == "shell":
        subprocess = subprocess.Popen('{}' .format(query), shell=True, stdout=subprocess.PIPE)
        answer = subprocess.stdout.read()

    if query_type == "powershell":
        subprocess.Popen('powershell -command {}' .format(query), shell=True, stdout=subprocess.PIPE)
        answer = subprocess.stdout.read()

    return answer



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
    
    filename = get_data_txt_file()
    hostname_os_version_dict = {}

    with open(filename) as fp:
        temp = fp.read()
        batches = temp.split("DistinguishedName")

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

def get_data_txt_file():
    import subprocess
    # TODO
    path = "./Process.txt"
    # TODO
    #subprocess = subprocess.Popen("Get-adcomputer -Filter 'Name -like '*'' -Properties | OpratingSystem | Out-File -FilePath {}" .format(path), shell=True, stdout=subprocess.PIPE)
    try:
        answer = subprocess.stdout.read()
    except:
        pass

    # POWERSHELL COMMAND
    # Get-adcomputer -Filter 'Name -like "*"' -Properties | OpratingSystem | Out-File -FilePath {}

    return path



# TODO
# TAB to every query NOT to every hostname



if __name__ == "__main__":

    workbook, df, user_selected_queries_list = init()

    try:
        print("extracting data from txt file")
        hostname_os_version_dict = extract_hostname_os_version_dict()
    except:
        print("failed to extract data from txt")

    # get answers for selected queries each server at a time
    for hostname in hostname_os_version_dict:
    
        # TODO
        # every query - NOT every hostname
        worksheet = workbook.add_worksheet(hostname[:30])

        server_os_version = hostname_os_version_dict[hostname]
        
        try:
            # get list of queries to execute
            queries_to_execute_list = get_queries_to_execute(df, user_selected_queries_list, server_os_version)
            print("executing queries")
        except:
            print("had no queries to execute for {}, please add queries to Excel" .format(hostname)) 
            continue
        
        # classify queries to powershell/shell queries
        shell_queries, powershell_queries = classify_queries(queries_to_execute_list)
        
        i = 0
        for query in powershell_queries:
            answer = execute_query_on_server(query, "powershell", hostname)
            worksheet.write(i, 0, "PowerShell - {}" .format(query))
            worksheet.write(i, 1, answer.decode('utf-8'))
            i += 1
        
        for query in shell_queries:
            answer = execute_query_on_server(query, "shell", hostname)
            worksheet.write(i, 0, "CMD - {}" .format(query))
            worksheet.write(i, 1, answer.decode('utf-8'))
            i += 1
        
    workbook.close()
