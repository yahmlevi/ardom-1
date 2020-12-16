from tkinter import *
from gui_functions import GUIFunctions

class GUI():

    def __init__(self, master):
        functions = GUIFunctions()

        master.title("Query Automation App")

        # LEFT PANEL
        self.create_left_panel(master, functions)
        

    def create_left_panel(self, master, functions):

        hostname_to_os_version_dict = functions.extract_hostname_os_version_dict()

        master.columnconfigure(0,weight=1)    #confiugures column 0 to stretch with a scaler of 1.
        master.rowconfigure(0,weight=1)       #confiugures row 0 to stretch with a scaler of 1.
        master.columnconfigure(1,weight=1)    #confiugures column 0 to stretch with a scaler of 1.
        # master.rowconfigure(1,weight=1)       #confiugures row 0 to stretch with a scaler of 1.


        # btn = Button(master, text="Click Me")
        # btn.pack(side=TOP, side=LEFT)
    
        scrollbar = Scrollbar(master, orient=VERTICAL)
        #scrollbar.pack(side=LEFT, fill=Y)
        scrollbar.grid(row=0,column=0) 
        mylist = Listbox(root, yscrollcommand = scrollbar.set)

        for hostname in hostname_to_os_version_dict:
            mylist.insert(END, hostname)

        #mylist.pack(side=LEFT, fill=BOTH, expand=True)
        mylist.grid(row=0,column=1,sticky='nsew')
        scrollbar.config(command=mylist.yview)

root = Tk()
window = GUI(root)
root.mainloop()


