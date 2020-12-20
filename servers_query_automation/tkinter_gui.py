from tkinter import *
from gui_functions import GUIFunctions
from query_automation_tkinter import run

class GUI():

    def __init__(self, master):

        self.functions = GUIFunctions()

        master.title("Query Automation App")

        self.servers_checkbox_value = IntVar()
        self.queries_checkbox_value = IntVar()
        self.timeout_selected = StringVar(master)

        self.bottomframe = Frame(master)
        self.bottomframe.pack(side=BOTTOM,expand=TRUE, fill=BOTH)        
        self.topframe = Frame(master)
        self.topframe.pack(side=TOP,expand=TRUE, fill=BOTH)

        self.create_left_panel(master)
        self.create_right_panel(master)

        run_btn = Button(self.bottomframe, text="RUN", command=self.pressed_run_btn)
        run_btn.pack(fill=X)

        self.server_dict_excel = self.functions.extract_manual_servers_dict()
        self.server_dict_activedir = self.functions.extract_activedir_server_dict()
        

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
        
        for hostname in self.server_dict_excel:
            self.hostname_list.insert(END, hostname)

    def left_panel_ad_btn(self):

        self.hostname_list.delete(0,'end')

        for hostname in self.server_dict_activedir:
            self.hostname_list.insert(END, hostname)


    def left_panel_both_btn(self):

        self.hostname_list.delete(0,'end')
        
        for hostname in self.server_dict_excel:
            self.hostname_list.insert(END, hostname)

        for hostname in self.server_dict_activedir:
            self.hostname_list.insert(END, hostname)


    def right_panel_load_queries_btn(self):

        self.query_list.delete(0,'end')
        query_name_list = self.functions.extract_query_name_list()

        for query in query_name_list:
            self.query_list.insert(END, query)

    def pressed_run_btn(self):
        from tkinter import messagebox
        selected_server = [self.hostname_list.get(idx) for idx in self.hostname_list.curselection()]
        selected_query = [self.query_list.get(idx) for idx in self.query_list.curselection()]
        print(selected_server)
        print(selected_query)
        
        try:
            timeout_val = float(self.timeout_selected.get())
            print(timeout_val)
        except:
            self.timeout_entry.delete(0, 'end')
            messagebox.showerror("error", "TIMEOUT value should be a number")
        
        
        # Intersection between list and dict
        temp1 = self.server_dict_excel.keys() & selected_server
        temp2 = self.server_dict_activedir.keys() & selected_server
         
        excel_hostname_to_os_version_dict = {}
        for item in self.server_dict_excel:
            if item in temp1:
                excel_hostname_to_os_version_dict[item] = self.server_dict_excel[item]

        ad_hostname_to_os_version_dict = {}
        for item in self.server_dict_activedir:
            if item in temp2:
                ad_hostname_to_os_version_dict[item] = self.server_dict_activedir[item]

        final_dict = {**ad_hostname_to_os_version_dict, **excel_hostname_to_os_version_dict}
        print(final_dict)
        run(selected_query, final_dict, timeout_val)
        try:
            run(selected_query, final_dict, timeout_val)
            messagebox.showinfo("SUCCESS","Finished executing queries on servers.\nAnswers at .\\query_answers.xlsx")

        except:
            print("ERROR")
        
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
        
        password_label = Label(self.topframe, text="Enter Timeout Size:")
        password_label.pack(side=LEFT)
        
        self.timeout_entry = Entry(self.topframe, width=3, font=10, textvariable=self.timeout_selected)
        self.timeout_entry.pack(side=LEFT) 

        load_queries_btn = Button(self.topframe, text="Load Queries", command=self.right_panel_load_queries_btn)
        load_queries_btn.pack(side=RIGHT, padx=5)
        
        right_select_all_chk = Checkbutton(self.topframe,text="Select All Queries", padx=5, variable=self.queries_checkbox_value, command=self.queries_checkbox_status)
        right_select_all_chk.pack(side=RIGHT)

        scrollbar = Scrollbar(master,orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=BOTH)

        self.query_list = Listbox(root,height=29, width=40, yscrollcommand = scrollbar.set, exportselection=False,selectmode=MULTIPLE)
        self.query_list.pack(side=RIGHT)

        scrollbar.config(command=self.query_list.yview)

    
root = Tk()
root.geometry("750x500")
window = GUI(root)
root.mainloop()


