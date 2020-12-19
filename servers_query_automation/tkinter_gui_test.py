from tkinter import *
from gui_functions import GUIFunctions

class GUI():

    def __init__(self, master):

        self.functions = GUIFunctions()

        master.title("Query Automation App")

        self.servers_checkbox_value = IntVar()
        self.queries_checkbox_value = IntVar()

        self.bottomframe = Frame(master)
        self.bottomframe.pack(side=BOTTOM,expand=TRUE, fill=BOTH)        
        self.topframe = Frame(master)
        self.topframe.pack(side=TOP,expand=TRUE, fill=BOTH)

        self.create_left_panel(master)
        self.create_right_panel(master)

        run_btn = Button(self.bottomframe, text="RUN", command=self.pressed_run_btn)
        run_btn.pack(fill=X)
        

    def servers_checkbox_status(self):

        if self.servers_checkbox_value.get():
            self.hostname_list.select_set(0, END)
        else:
            self.hostname_list.selection_clear(0, END)

    def queries_checkbox_status(self):

        if self.queries_checkbox_value.get():
            self.query_list.select_set(0, END)
        else:
            self.query_list.selection_clear(0, END)

    def left_panel_excel_btn(self):

        self.hostname_list.delete(0,'end')
        server_list_excel = self.functions.extract_manual_servers_list()
        
        for hostname in server_list_excel:
            self.hostname_list.insert(END, hostname)

    def left_panel_ad_btn(self):

        self.hostname_list.delete(0,'end')
        server_list_activedir = self.functions.extract_activedir_server_list()

        for hostname in server_list_activedir:
            self.hostname_list.insert(END, hostname)


    def left_panel_both_btn(self):

        self.hostname_list.delete(0,'end')
        
        server_list_excel = self.functions.extract_manual_servers_list()

        for hostname in server_list_excel:
            self.hostname_list.insert(END, hostname)

        server_list_activedir = self.functions.extract_activedir_server_list()

        for hostname in server_list_activedir:
            self.hostname_list.insert(END, hostname)


    def right_panel_load_queries_btn(self):

        self.query_list.delete(0,'end')
        query_name_list = self.functions.extract_query_name_list()

        for query in query_name_list:
            self.query_list.insert(END, query)

    def pressed_run_btn(self):

        server_values = [self.hostname_list.get(idx) for idx in self.hostname_list.curselection()]
        query_values = [self.query_list.get(idx) for idx in self.query_list.curselection()]
        print(server_values)
        print(query_values)
        # toplevel = Toplevel()
        # toplevel.geometry("200x150")
        # toplevel.title("Result Location")
        # label1 = Label(toplevel, text="test", height=0, width=100)
        # label1.pack()
        
        
    def create_left_panel(self, master):
        
        self.left_select_all_chk = Checkbutton(self.topframe,text="Select All Servers", variable=self.servers_checkbox_value, command=self.servers_checkbox_status)
        self.left_select_all_chk.pack(side=LEFT)

        left_excel_btn = Button(self.topframe, text="Excel", command=self.left_panel_excel_btn)
        left_excel_btn.pack(side=LEFT, fill=X, padx=5)
        left_ad_btn = Button(self.topframe, text="ActiveDirectory", command=self.left_panel_ad_btn)
        left_ad_btn.pack(side=LEFT, fill=X, padx=5)
        left_both_btn = Button(self.topframe, text="Both", command=self.left_panel_both_btn)
        left_both_btn.pack(side=LEFT, fill=X, padx=5)

        scrollbar = Scrollbar(master, orient=VERTICAL)
        scrollbar.pack(side=LEFT, fill=BOTH)

        self.hostname_list = Listbox(root, yscrollcommand=scrollbar.set,selectmode=MULTIPLE, exportselection=False)
        self.hostname_list.pack(side=LEFT, expand = True, fill=BOTH)

        scrollbar.config(command=self.hostname_list.yview)


    def create_right_panel(self, master):
        # TODO
        # fix entry
        timeout_entry = Entry(self.topframe, text="TIMEOUT", width=3, font=10)
        timeout_entry.pack(side=LEFT, padx=30) 

        right_btn = Button(self.topframe, text="Load Queries", command=self.right_panel_load_queries_btn)
        right_btn.pack(side=RIGHT, padx=5)
        
        right_select_all_chk = Checkbutton(self.topframe,text="Select All Queries", padx=5, variable=self.queries_checkbox_value, command=self.queries_checkbox_status)
        right_select_all_chk.pack(side=RIGHT)

        scrollbar = Scrollbar(master,orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=BOTH)

        self.query_list = Listbox(root,height=29, width=40, yscrollcommand = scrollbar.set, exportselection=False)
        self.query_list.pack(side=RIGHT)

        scrollbar.config(command=self.query_list.yview)

    
root = Tk()
root.geometry("750x500")
window = GUI(root)
root.mainloop()


