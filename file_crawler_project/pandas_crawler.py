import pandas as pd


def set_df(file_list):
    df_file_list = pd.DataFrame.from_records([file.to_dict() for file in file_list])
    return df_file_list
    
    
def pd_root(df_file_list, path):
    # -----------------------------------------------------------------------------------------------
    # ------ROOT TAB DONE--------
    print("")
    print('------ROOT TAB--------')
    print("")
    root_tab = df_file_list.groupby(['Year', 'File Type']).aggregate({
        "File Size GB": ['sum'],
        'File Type': ['count']
    })
    root_tab['Root'] = path
    print(root_tab)
    print("")
    print('------ROOT TAB--------')
    print("")
    # ------ROOT TAB WORKS--------

def pd_root_by_file_type(df_file_list, path):
    #-------ROOT BY FILE TYPE------
    print("")
    print('------ROOT BY FILE TYPE TAB--------')
    print("")
    root_by_file_tab = df_file_list.groupby(['File Type']).aggregate({
        "File Size GB": ['sum'], 
        'File Type': ['count']
    })
    root_by_file_tab['Root'] = path
    print(root_by_file_tab)
    print("")
    print('------ROOT BY FILE TYPE TAB--------')
    print("")
    #-------ROOT BY FILE TYPE------


def pd_restricted(df_file_list):
    print("")
    print('------RESTRICTED TAB--------')
    print("")
    #-------RESTRICTED TAB------

    # How To Filter Pandas Dataframe By Values of Column?
    # https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
    
    restricted_tab = df_file_list[df_file_list["Restricted"] == True]['File Path']
    if restricted_tab.empty:
        print('No Restricted Files!')
        print('No Restricted Files!')
        print('No Restricted Files!')
    
    else:
        print(restricted_tab)
    print("")
    print('------RESTRICTED TAB--------')
    print("")
    #-------RESTRICTED TAB------
