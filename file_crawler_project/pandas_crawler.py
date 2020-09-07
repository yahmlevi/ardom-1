import pandas as pd



class Panda(object):

    def __init__(self, file_list):

        self.df_file_list = pd.DataFrame.from_records([file.to_dict() for file in file_list])

    
    def pd_root(self, path):
        
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
       

    def pd_root_by_file_type(self, path):
    
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
    


    def pd_restricted(self):
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


        
    # https://medium.com/escaletechblog/writing-custom-aggregation-functions-with-pandas-96f5268a8596
    #def test_sum(series):
     #   return reduce(lambda x, y: x + y, series)

