import xlsxwriter
import os


def insert_to_excel_root(totals_list, path):
    # create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('file_crawler.xlsx')
    worksheet = workbook.add_worksheet()

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # create headlines
    worksheet.write("A1", "Root Folder", bold)
    worksheet.write("C1", "Year Modified", bold)
    worksheet.write("E1", "File Type", bold)
    worksheet.write("G1", "Size in bytes", bold)
    worksheet.write("I1", "Size", bold)
    worksheet.write("K1", "count", bold)
    
    # Start from the first cell. Rows and columns are zero indexed.
    row = 1

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

    workbook.close()

