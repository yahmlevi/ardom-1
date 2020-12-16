
class GUIFunctions(object):

    def __init__(self):
        self.hostname_os_version_dict = {}


    def extract_hostname_os_version_dict(self):
        self.hostname_os_version_dict = {}

        #---------------------------------------------
        # import subprocess
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
            self.hostname_os_version_dict[temp1[1].strip()] = temp2[1].strip()
        
        return self.hostname_os_version_dict
