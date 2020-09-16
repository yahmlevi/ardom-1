import pandas as pd



class Panda(object):

    def __init__(self, file_list):

        self.df_file_list = pd.DataFrame.from_records([file.to_dict() for file in file_list])

    
    def pd_root(self, path):
        header_list = ['Size GB', 'Count', 'Root']

        print("")
        print('------ROOT TAB--------')
        print("")
        root_tab = self.df_file_list.groupby(['Year', 'File Type']).aggregate({
            "File Size GB": ['sum'],
            'File Type': ['count']
        })
        root_tab['Root'] = path
        print(root_tab)
        print("")
        print('------ROOT TAB--------')
        print("")
        return root_tab, header_list
       

    def pd_root_by_file_type(self, path):
        header_list = ['Size GB', 'Count', 'Root']
    
        print("")
        print('------ROOT BY FILE TYPE TAB--------')
        print("")
        root_by_file_tab = self.df_file_list.groupby(['File Type']).aggregate({
            "File Size GB": ['sum'], 
            'File Type': ['count']
        })
        root_by_file_tab['Root'] = path
        print(root_by_file_tab)
        print("")
        print('------ROOT BY FILE TYPE TAB--------')
        print("")
        return root_by_file_tab, header_list
    


    
    def pd_subroot(self, path):
        header_list = ['Size GB', 'Count', 'Root']
        
        print("")
        print('------SUB-ROOT TAB--------')
        print("")
        sub_root_tab = self.df_file_list.groupby(['Sub-Root', 'Year', 'File Type']).aggregate({
            "File Size GB": ['sum'], 
            'File Type': ['count']
        })
        sub_root_tab['Root'] = path
        print(sub_root_tab)
        print("")
        print('------SUB-ROOT TAB--------')
        print("")
        return sub_root_tab, header_list
    

    def pd_total(self, path):
        header_list = ['Size GB', 'Count', 'Root']

        print("")
        print('------TOTAL TAB--------')
        print("")
        total_tab = self.df_file_list.groupby(['Sub-Root']).aggregate({
            "File Size GB": ['sum'], 
            'File Type': ['count']
        })
        total_tab['Root'] = path
        print(total_tab)
        print("")
        print('------TOTAL TAB--------')
        print("")
        return total_tab, header_list
    
        


    def pd_restricted(self):
        header_list = ['Root']

        print("")
        print('------RESTRICTED TAB--------')
        print("")

        # How To Filter Pandas Dataframe By Values of Column?
        # https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
        
        restricted_tab = self.df_file_list[self.df_file_list["Restricted"] == True]['File Path']
        if restricted_tab.empty:
            print('No Restricted Files!')
            print('No Restricted Files!')
            print('No Restricted Files!')
        
        else:
            print(restricted_tab)
        print("")
        print('------RESTRICTED TAB--------')
        print("")
        return restricted_tab, header_list

    def to_csv(self, df, header_list, csv_name):
        import os
        from datetime import date

        today_date = date.today()
        cwd = os.path.dirname(os.path.realpath(__file__))
        path = cwd + '\crawler_csv_folder_{}'.format(today_date)
        if not os.path.exists(path):
            os.makedirs(path)
        df.to_csv(r'{}\{}.csv' .format(path, csv_name), index = True, header = header_list, encoding='utf-8-sig')
        print('Saved at: {}' .format(path))
        return path

    
    def bigger_then_one_gb(self):
        # https://stackoverflow.com/questions/41523270/pandas-groupby-and-filter
        print("")
        print('------BIGGER THEN 1 GB--------')
        print("")
        
        header_list = ['Size GB', 'Count']
        
        df = self.df_file_list[(self.df_file_list['File Size GB']  > 1.0000)]
        bigger_then_one_gb_tab = df.groupby(['Sub-Root', 'File Type']).aggregate({
            "File Size GB": ['sum'],
            'File Type': ['count']
        })


        print("")
        print('------BIGGER THEN 1 GB--------')
        print("")
        print(bigger_then_one_gb_tab)

        return bigger_then_one_gb_tab, header_list


    def custom_file_type(self):
        # https://stackoverflow.com/questions/12096252/use-a-list-of-values-to-select-rows-from-a-pandas-dataframe
        print("")
        print('------CUSTOM FILE TYPE--------')
        print("")

        header_list = ['Size GB', 'Count']
        
        file_extensions = input("Enter File Type Extensions with comma between (.txt,.mp4,.avi): ")
        file_extensions_list = file_extensions.split(',')

        df = self.df_file_list[(self.df_file_list['File Type'].isin(file_extensions_list))]

        custom_file_type_tab = df.groupby(['Sub-Root']).aggregate({
            "File Size GB": ['sum'],
            'File Type': ['count']
        })

        print("")
        print('------CUSTOM FILE TYPE--------')
        print("")
        print(custom_file_type_tab)

        return custom_file_type_tab, header_list

        
    # User input sub-sub-root and root --> return return regular analysis for all sub-sub-roots in root
    def custom_sub_sub_analsys(self):
        print("")
        print('------CUSTOM SUB SUB ROOT--------')
        print("")

        header_list = ['Size GB', 'Count']

        custom_sub_sub = input("Enter Sub-Sub-Root to analyze: ")

        df = self.df_file_list[(self.df_file_list['Sub-Sub-Root'] == custom_sub_sub)]

        custom_sub_sub_tab = df.groupby(['Sub-Sub-Root']).aggregate({
        "File Size GB": ['sum'], 
        "File Type": ['count']
        })

        print(custom_sub_sub_tab)
        print("")
        print('------CUSTOM SUB SUB ROOT--------')
        print("")

        return custom_sub_sub_tab, header_list
        


