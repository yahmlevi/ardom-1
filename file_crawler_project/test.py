class File:
    pass

class Totals:
    pass


def populate_list():
    file_list = []
   
    for i in range(5):
        file = File()
        file.year = "2020"
        file.file_type = "txt"
        file.path = ""
        file_list.append(file)
       
    for i in range(5):
        file = File()
        file.year = "2019"
        file.file_type = "txt"
        file.path = ""
        file_list.append(file)
       
    return file_list

def count_by_year_and_file_type(file_list, filter):
    result = 0
    for file in file_list:
        if filter(file):
            result+=1
    return result
   
def get_year_list(file_list):
    year_list = []
   
    return year_list
   
def process_list(file_list):
    totals_list = []
   
    year_list = get_year_list(file_list)
    file_type_list = ["txt", "py", "doc"]
   
    for year in year_list:
        for file_type in file_type_list:
            totals = Totals()
           
            totals.year = year
            totals.file_type = file_type
            totals.count = count_by_year_and_file_type(file_list, lambda file: file.year == year and file.file_type == file_type)
            totals_list.append(totals)
    return totals_list
           
           
file_list = populate_list()
print(file_list)
for file in file_list:
    print(file.year + ", " + file.file_type)

totals_list = process_list(file_list)
for totals in totals_list:
    print (totals.year + "-" + totals.file_type + ": " + str(totals.count))
