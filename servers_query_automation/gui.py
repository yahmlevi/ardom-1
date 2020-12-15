# https://www.blog.pythonlibrary.org/2013/02/27/wxpython-adding-checkboxes-to-objectlistview/

import wx
from ObjectListView import ObjectListView, ColumnDefn, OLVEvent
import pandas as pd



# https://stackoverflow.com/questions/1305532/convert-nested-python-dict-to-object?page=1&tab=votes#tab-top
class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

class Panel(wx.Panel):

    def __init__(self, parent):
    
        wx.Panel.__init__(self, parent=parent)
        
        self.desired_query_list = []
        
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.list_view = ObjectListView(self, style=wx.LC_REPORT|wx.SUNKEN_BORDER)

        self.list_view.Bind(OLVEvent.EVT_ITEM_CHECKED, self.on_item_checked)
        
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


    def on_item_checked(self, event):
        temp = self.list_view.GetSelectedObject()
        checked = True if self.list_view.IsChecked(temp) else False
        selected_row = vars(temp)
        print("TEST - ", selected_row)

        if checked:
            self.desired_query_list.append(selected_row)
        elif not checked:
            if selected_row in self.desired_query_list:
                self.desired_query_list.remove(selected_row)
            else:
                pass
            
        return self.desired_query_list

    
    def onCheck(self, event):
        objects = self.list_view.GetObjects()
        
        for obj in objects:
            self.list_view.SetCheckState(obj, True)
        self.list_view.RefreshObjects(objects)
        
    def call_query_automation_script(self, event):
        desired_query_list = self.on_item_checked("")
        print(desired_query_list)


    def get_queries_data():
            xl_query_to_os_path = "D:\\projects\\ardom-1\\servers_query_automation\\queries.xlsx"
            df = pd.read_excel(xl_query_to_os_path)

            query_dict = df.to_dict()

            return query_dict, df

    def set_data(self):
        query_dict, df = Panel.get_queries_data()
        
        i = 0
        column_list = []
        list_of_dict = []

        # convert df to list of dict 
        data_rows = df.T.to_dict().values()

        # get first row of Excel (header row) as a list
        column_name_row = list(df.iloc[0].keys())

        # build column_list
        for column_name in column_name_row:
            column_list.append(ColumnDefn(column_name, "left", 150, column_name))

        # create dict of row
        for row in data_rows:  
            obj = {}          
            for i in range(0, len(row.values())):
                column_name = column_name_row[i]
                obj[column_name] = list(row.values())[i]
            
            # make dict hashable 
            obj = Struct(**obj)
            
            list_of_dict.append(obj)
        
        self.list_view.SetColumns(column_list)
        self.list_view.CreateCheckStateColumn()
        self.list_view.SetObjects(list_of_dict)
        

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


        


