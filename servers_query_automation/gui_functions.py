
import pandas as pd

class GUIFunctions(object):

    def __init__(self):
        self.hostname_os_version_dict = {}

        # create handle to read Excel
        xl_queries = ".\queries.xlsx"
        self.queries_df = pd.read_excel(xl_queries)

        xl_manual_servers = ".\manual_servers_list.xlsx"
        self.manual_server_list_df = pd.read_excel(xl_manual_servers)

    def extract_manual_servers_dict(self):
        
        server = self.manual_server_list_df.iloc[:,0]
        os_version = self.manual_server_list_df.iloc[:,1]

        return pd.Series(os_version.values, index=server).to_dict()



    def extract_query_name_list(self):
        header_list = list(self.queries_df)

        return header_list[1:]
        

    def extract_activedir_server_dict(self):
        self.hostname_os_version_dict = {}

        #---------------------------------------------
        import subprocess
        query = "Import-module activedirectory; Get-ADComputer -Filter 'Name -like \"*\"' -searchbase \"cn=computers, dc=ardomnet, dc=co, dc=il\" -Properties OperatingSystem, IPv4Address | sort-object name"
        p = subprocess.Popen(["powershell.exe", '{}'.format(query) ], stdout=subprocess.PIPE)
        res = p.communicate()
        batches = res[0].decode("utf-8").split("DistinguishedName")
        # with open("Process.txt") as fp:
        #     temp = fp.read()
        #     batches = temp.split("DistinguishedName")
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
            self.hostname_os_version_dict[temp1[1].strip()] = temp2[1].strip()
        
        return self.hostname_os_version_dict

