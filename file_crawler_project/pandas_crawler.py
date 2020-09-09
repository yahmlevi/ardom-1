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
        return root_tab
       

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
        return root_by_file_tab
    


    
    def pd_subroot(self, path):
        
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
        return sub_root_tab
    

    def pd_total(self, path):
        
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
        return total_tab
    
        


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
        return restricted_tab

    def to_csv(self, df):
        df.to_csv(r'D:\projects\ardom-1\pandas_crawler.csv', index = False)
        #print(df)
        

    def concat_df(self, df1, df2, df3, df4, df5):
        #pd.concat([
            #pd.concat([df1, df2], axis=1),
            #pd.concat([df3, df4], axis=1)]).to_csv('D:\projects\ardom-1\file_crawler_project\pandas_crawler.csv', index = False)
        bigdata = pd.concat([df1, df2, df3, df4, df5], ignore_index=True, sort=False)
        return bigdata




        
    # https://medium.com/escaletechblog/writing-custom-aggregation-functions-with-pandas-96f5268a8596
    #def test_sum(series):
     #   return reduce(lambda x, y: x + y, series)

