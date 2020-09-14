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

    
    # Extract file type from sub-root that are bigger then 1GB
    # groupby sub-root, file type, filter(if >1vgb)
    # https://stackoverflow.com/questions/41523270/pandas-groupby-and-filter
    def bigger_then_one_gb(self):
        # print(print(df[(df['V'] == 0).groupby(df['YEAR']))
        # bigger_then_one_gb_tab = self.df_file_list[self.df_file_list['File Size GB'].groupby(self.df_file_list['Sub-Root', 'File Type'])]
        bigger_then_one_gb_tab = self.df_file_list[(self.df_file_list['File Size GB']  > 0.0100)]
        bigger_then_one_gb_tab1 = bigger_then_one_gb_tab.groupby(self.df_file_list['Sub-Root'])
        # df[df.V == 0]
        # bigger_then_one_gb_tab = self.df_file_list[self.df_file_list.File Size GB]
        print(bigger_then_one_gb_tab)



