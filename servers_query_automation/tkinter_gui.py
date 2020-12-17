from tkinter import *
from gui_functions import GUIFunctions

class GUI():

    def __init__(self, master):
        functions = GUIFunctions()

        master.title("Query Automation App")

        self.create_left_panel(master, functions)
        self.create_right_panel(master, functions)
        

    def create_left_panel(self, master, functions):

        hostname_to_os_version_dict = functions.extract_hostname_os_version_dict()

        excel_btn = Button(master, text="Excel")
        excel_btn.grid(row=0, column=1,columnspan=3)
        ad_btn = Button(master, text="ActiveDirectory")
        ad_btn.grid(row=0, column=2)
        both_btn = Button(master, text="Both")
        both_btn.grid(row=0, column=3)

        select_all_chk = Checkbutton(master,text="select all")
        select_all_chk.grid(row=0, column=0)

        scrollbar = Scrollbar(master, orient=VERTICAL) # orient=VERTICAL
        scrollbar.grid(row=1,column=0, sticky="W")

        hostname_list = Listbox(root,height=29, width=40) # , yscrollcommand = scrollbar.set
        for hostname in hostname_to_os_version_dict:
            hostname_list.insert(END, hostname)

        hostname_list.grid(row=1,column=1,columnspan=3,sticky='W') #,sticky='nsew'
        scrollbar.config(command=hostname_list.yview)


    def create_right_panel(self, master, functions):

        hostname_to_os_version_dict = functions.extract_hostname_os_version_dict()

        btn = Button(master, text="Excel")
        btn.grid(row=0, column=4)
        btn = Button(master, text="ActiveDirectory")
        btn.grid(row=0, column=5)
        btn = Button(master, text="Both")
        btn.grid(row=0, column=6)

        chk = Checkbutton(master,text="select all")
        chk.grid(row=0, column=6)

        scrollbar = Scrollbar(master) # orient=VERTICAL
        scrollbar.grid(row=1,column=7,rowspan=3)

        hostname_list = Listbox(root,height=29, width=40, bg="red") # , yscrollcommand = scrollbar.set
        for hostname in hostname_to_os_version_dict:
            hostname_list.insert(END, hostname)

        hostname_list.grid(row=1,column=7,columnspan=3,sticky='E') #,sticky='nsew'
        scrollbar.config(command=hostname_list.yview)




root = Tk()
root.geometry("750x500")
for i in range(0,50):
    root.grid_rowconfigure(i, weight=1) # this needed to be added
    root.grid_columnconfigure(i, weight=1)
window = GUI(root)
root.mainloop()


