from tkinter import *
from gui_functions import GUIFunctions

class GUI():

    def __init__(self, master):
        functions = GUIFunctions()

        master.title("Query Automation App")

        self.bottomframe = Frame(master)
        self.bottomframe.pack(side=BOTTOM)
        
        self.topframe = Frame(master)
        self.topframe.pack(side=TOP)

        self.create_left_panel(master, functions)
        self.create_right_panel(master, functions)



    def create_left_panel(self, master, functions):

        hostname_to_os_version_dict = functions.extract_hostname_os_version_dict()

        left_excel_btn = Button(self.topframe, text="Excel")
        left_excel_btn.pack(side=LEFT)
        left_ad_btn = Button(self.topframe, text="ActiveDirectory")
        left_ad_btn.pack(side=LEFT)
        left_both_btn = Button(self.topframe, text="Both")
        left_both_btn.pack(side=LEFT)

        left_select_all_chk = Checkbutton(self.topframe,text="select all")
        left_select_all_chk.pack(side=LEFT)

        scrollbar = Scrollbar(master, orient=VERTICAL) # orient=VERTICAL
        scrollbar.pack(side=LEFT, fill=BOTH)

        hostname_list = Listbox(root, yscrollcommand = scrollbar.set) #,height=29, width=40 # , yscrollcommand = scrollbar.set
        for hostname in hostname_to_os_version_dict:
            hostname_list.insert(END, hostname)

        hostname_list.pack(side=LEFT, expand = True, fill=BOTH)
        scrollbar.config(command=hostname_list.yview)


    def create_right_panel(self, master, functions):

        hostname_to_os_version_dict = functions.extract_hostname_os_version_dict()

        right_btn = Button(master, text="Excel")
        right_btn.pack(side=RIGHT)
        right_btn = Button(master, text="ActiveDirectory")
        right_btn.pack(side=RIGHT)
        right_btn = Button(master, text="Both")
        right_btn.pack(side=RIGHT)

        right_select_all_chk = Checkbutton(master,text="select all")
        right_select_all_chk.pack(side=RIGHT)

        scrollbar = Scrollbar(master) # orient=VERTICAL
        scrollbar.pack(side=RIGHT)

        hostname_list = Listbox(root,height=29, width=40, bg="red") # , yscrollcommand = scrollbar.set
        for hostname in hostname_to_os_version_dict:
            hostname_list.insert(END, hostname)

        hostname_list.pack(side=RIGHT)
        scrollbar.config(command=hostname_list.yview)




root = Tk()
root.geometry("750x500")
window = GUI(root)
root.mainloop()


