# https://www.blog.pythonlibrary.org/2013/02/27/wxpython-adding-checkboxes-to-objectlistview/

import wx
from ObjectListView import ObjectListView, ColumnDefn
import pandas as pd

class Book(object):
    """
    Model of the Book object
    Contains the following attributes:
    'ISBN', 'Author', 'Manufacturer', 'Title'
    """
    #----------------------------------------------------------------------
    def __init__(self, title, author, isbn, mfg, test, second_test):
        self.isbn = isbn
        self.author = author
        self.mfg = mfg
        self.title = title
        self.test = test
        self.second_test = second_test

class Panel(wx.Panel):

    def __init__(self, parent):
    
        wx.Panel.__init__(self, parent=parent)
        
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.list_view = ObjectListView(self, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        
        self.set_data()
        
        checkBtn = wx.Button(self, label="Check All")
        checkBtn.Bind(wx.EVT_BUTTON, self.onCheck)
        btnSizer.Add(checkBtn, 0, wx.ALL, 5)
        
        uncheckBtn = wx.Button(self, label="Submit")
        uncheckBtn.Bind(wx.EVT_BUTTON, self.call_query_automation_script)
        btnSizer.Add(uncheckBtn, 0, wx.ALL, 5)
        
        mainSizer.Add(self.list_view, 1, wx.EXPAND|wx.ALL, 5)
        mainSizer.Add(btnSizer, 0, wx.CENTER|wx.ALL, 5)
        self.SetSizer(mainSizer)
    
    def onCheck(self, event):
        
        objects = self.list_view.GetObjects()
        
        for obj in objects:
            self.list_view.SetCheckState(obj, True)
        self.list_view.RefreshObjects(objects)
        
    def call_query_automation_script(self, event):
        # TODO 
        # call script 
        # objects = self.list_view.GetObjects()
                
        # for obj in objects:
        #     self.list_view.SetCheckState(obj, False)
        # self.list_view.RefreshObjects(objects)        
        pass

    def get_queries_data():
            # create handle to read Excel
            xl_query_to_os_path = "D:\\projects\\ardom-1\\servers_query_automation\\queries.xlsx"
            df = pd.read_excel(xl_query_to_os_path)

            query_dict = df.to_dict()

            return query_dict

    
    
    def set_data(self):
        
        query_dict = Panel.get_queries_data()

        i = 0
        column_list = []
        data_list = []
        test_list = []
        for column_name in query_dict:
            i += 1
            column_list.append(ColumnDefn(column_name, "left", 100, "header"))
            #print(query_dict[query].values())
            data_list.append(query_dict[column_name].values())

            test_list.append(Book("title", "author", "isbn", "mfg", "test5", "hhy"))
            
            
        #TODO
        # DATA CAN NOT BE SET IN WXPYTHON UI (TABLE)
        # solve it
        #print(list(data_list))
        print(column_list)
        self.list_view.SetColumns(column_list)

        self.list_view.CreateCheckStateColumn()
        #self.list_view.SetObjects(data_list)
        print(test_list)
        self.list_view.SetObjects(test_list)



class Frame(wx.Frame):


    def __init__(self):
        
        title = "Query Automation"
        wx.Frame.__init__(self, parent=None, title=title, size=(1024, 768))
        panel = Panel(self)
        
    
if __name__ == "__main__":
    app = wx.App(False)
    frame = Frame()
    frame.Show()
    app.MainLoop()


        


