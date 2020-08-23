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
        
        self.init_worksheets()

    def init_worksheets(self):
        bold = self.format_bold

        self.worksheets["root"] = self.workbook.add_worksheet("root")
        
        worksheet = self.worksheets["root"]
        
        # create headlines
        worksheet.write("A1", "Root Folder", bold)
        worksheet.write("C1", "Year Modified", bold)
        worksheet.write("E1", "File Type", bold)
        worksheet.write("G1", "Size in bytes", bold)
        worksheet.write("I1", "Size", bold)
        worksheet.write("K1", "count", bold)

        self.new_row_indices["root"] = 1
        
        self.worksheets["subfolders"] = self.workbook.add_worksheet("subroot")

        worksheet = self.worksheets["subfolders"]
    
        # create headlines
        worksheet.write("A1", "Subroot Folder", bold)
        worksheet.write("C1", "Year Modified", bold)
        worksheet.write("E1", "File Type", bold)
        worksheet.write("G1", "Size in bytes", bold)
        worksheet.write("I1", "Size", bold)
        worksheet.write("K1", "count", bold)

        self.new_row_indices["subfolders"] = 1
        
        self.worksheets["restricted"] = self.workbook.add_worksheet("log-restricted")

        worksheet = self.worksheets["restricted"]
    
        # create headlines
        worksheet.write("A1", "restricted file path", bold)

        self.new_row_indices["restricted"] = 1
        

    def insert_to_root(self, totals_list, path):

        worksheet = self.worksheets["root"]

        # Start from the first cell. Rows and columns are zero indexed.
        row =  self.new_row_indices["root"] 

        # write date
        for totals in totals_list:
            if totals.file_type != "FOLDER":
                worksheet.write(row, 0, path)
                worksheet.write(row, 2, totals.year)
                worksheet.write(row, 4, totals.file_type)
                worksheet.write(row, 6, totals.total_size)
                worksheet.write(row, 8, totals.total_size_str)
                worksheet.write(row, 10, totals.count)        
                row += 1

        self.new_row_indices["root"] = row


    def insert_to_subroot(self, totals_list, path):

        worksheet = self.worksheets["subfolders"]
    
        # Start from the first cell. Rows and columns are zero indexed.
        row =  self.new_row_indices["subfolders"]

        # write date
        for totals in totals_list:
            if totals.file_type != "FOLDER":
                worksheet.write(row, 0, path)
                worksheet.write(row, 2, totals.year)
                worksheet.write(row, 4, totals.file_type)
                worksheet.write(row, 6, totals.total_size)
                worksheet.write(row, 8, totals.total_size_str)
                worksheet.write(row, 10, totals.count)        
                row += 1

        self.new_row_indices["subfolders"] = row

    
    def insert_to_restricted(self, restricted_files_list):

        worksheet = self.worksheets["restricted"]

        # Start from the first cell. Rows and columns are zero indexed.
        row =  self.new_row_indices["restricted"] 

        
        for item in restricted_files_list:  
            worksheet.write(row, 0, item)
            row += 1

        self.new_row_indices["root"] = row

    
    
    def close(self):
        self.workbook.close()    
        

