import xlsxwriter
import os


class Excel(object):

    def __init__(self):
        
        # create a workbook and add a worksheet.
        self.workbook = xlsxwriter.Workbook('D:\projects\\ardom-1\\file_crawler_project\\file_crawler_results.xlsx')
        self.worksheets = {}
        self.new_row_indices = {}

        # Add a bold format to use to highlight cells.
        self.format_bold = self.workbook.add_format({'bold': True})

        self.worksheet_data = [
            {
                "name": "Root",
                "headers": ["Root Folder", "Year Modified", "File Type", "Size in bytes",  "Size", "count"]
            },
            {
                "name": "Sub-Root",
                "headers": ["Subroot Folder", "Year Modified", "File Type", "Size in bytes", "Size", "Count"]
            },
            {
                "name": "Total", 
                "headers": ["Root Folder", "Subroot Folder", "File Size", "Count"]
            },
            {
                "name": "Log-Restricted",
                "headers": ["Restricted File Path"]
            }
        ]
        
        self.init_worksheets()

    def init_worksheets(self):

        for data in self.worksheet_data:
            name = data["name"]
            self.worksheets[name] = self.workbook.add_worksheet(name)
            worksheet = self.worksheets[name]
            
            self.set_column_headers(worksheet, data["headers"])
            self.new_row_indices[name] = 1        

    def set_column_headers(self, worksheet, headers):
        
        column_index = 0
        for header in headers:
            worksheet.write(0, column_index, header, self.format_bold)
            if column_index == 0:
                column_width = 40
            else:
                column_width = 20
            worksheet.set_column(column_index, column_index, column_width)
            column_index+=1 


    def insert_to_root(self, totals_list, path):

        name = self.worksheet_data[0]["name"]
        worksheet = self.worksheets[name]

        # Start from the first cell. Rows and columns are zero indexed.
        row =  self.new_row_indices[name] 

        # write date
        for totals in totals_list:
            if totals.file_type != "FOLDER":
                worksheet.write(row, 0, path)
                worksheet.write(row, 1, totals.year)
                worksheet.write(row, 2, totals.file_type)
                worksheet.write(row, 3, totals.total_size)
                worksheet.write(row, 4, totals.total_size_str)
                worksheet.write(row, 5, totals.count)        
                row += 1

        self.new_row_indices[name] = row


    def insert_to_subroot(self, totals_list, path):

        name = self.worksheet_data[1]["name"]
        worksheet = self.worksheets[name]
    
        # Start from the first cell. Rows and columns are zero indexed.
        row =  self.new_row_indices[name]

        # write date
        for totals in totals_list:
            if totals.file_type != "FOLDER":
                worksheet.write(row, 0, path)
                worksheet.write(row, 1, totals.year)
                worksheet.write(row, 2, totals.file_type)
                worksheet.write(row, 3, totals.total_size)
                worksheet.write(row, 4, totals.total_size_str)
                worksheet.write(row, 5, totals.count)        
                row += 1

        self.new_row_indices[name] = row


    def insert_to_total(self, totals_list, path, sub_path = ""):

        name = self.worksheet_data[2]["name"]
        worksheet = self.worksheets[name]
    
        # Start from the first cell. Rows and columns are zero indexed.
        row =  self.new_row_indices[name]

        # write date
        for totals in totals_list:
        
            worksheet.write(row, 0, path)
            worksheet.write(row, 1, sub_path)
            worksheet.write(row, 2, totals.total_size_str)
            worksheet.write(row, 3, totals.count)    
            row += 1

        self.new_row_indices[name] = row


    
    def insert_to_restricted(self, restricted_files_list):

        name = self.worksheet_data[3]["name"]
        worksheet = self.worksheets[name]

        # Start from the first cell. Rows and columns are zero indexed.
        row =  self.new_row_indices[name] 

        
        for item in restricted_files_list:  
            worksheet.write(row, 0, item)
            row += 1

        self.new_row_indices[name] = row

    
    
    def close(self):
        self.workbook.close()    
        

