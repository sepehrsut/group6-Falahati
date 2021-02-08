def equal(root_in: str, root_out: str):
   
    """ This function divides expenses evenly between units. """
   
    import pandas as pd
    
    user_input_df = pd.read_excel(root_in, names=['amount','time','category','subcategory','related unit','div'],index_col =False)
    user_input_df = user_input_df[user_input_df['div'] == 'equal'][['amount','time','category','subcategory','related unit']]
           
    # A series of operations for changing the related unit's class frm object to a list. Useful when executing the explode method
    user_input_df['related unit'] = user_input_df['related unit'].str.replace('[','')
    user_input_df['related unit'] = user_input_df['related unit'].str.replace(']','')
    user_input_df['related unit'] = list(user_input_df['related unit'].str.split(','))
    
    user_input_df['cost for each unit'] = user_input_df['amount'] // len(user_input_df['related unit'][0])
    user_input_df = user_input_df.explode('related unit')
    user_input_df['related unit'] = user_input_df['related unit'].str.strip()
    
    user_input_df['%share from the whole amount'] = (user_input_df['cost for each unit'] // user_input_df['amount']) * 100
    
    user_input_df.to_csv(root_out, mode = 'a', header = False, index = False)
    
    return


def number(root_in: str, root_out: str):
    
    """ This function divides expenses according to the number of residents living in each apartment. """
    
    import pandas as pd
   
    user_input_df = pd.read_excel(root_in, names=['amount','time','category','subcategory','related unit','div'],index_col=False)
    resident_info = pd.read_excel(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژ''ه\data1.xlsx')
    
    user_input_df = user_input_df[user_input_df['div'] == 'number'][['amount','time','category','subcategory','related unit']]
    
    # A series of operations for changing the related unit's class frm object to a list. Useful when executing the explode method
    user_input_df['related unit'] = user_input_df['related unit'].str.replace('[','')
    user_input_df['related unit'] = user_input_df['related unit'].str.replace(']','')
    user_input_df['related unit'] = list(user_input_df['related unit'].str.split(','))
    
    user_input_df = user_input_df.explode('related unit',ignore_index = True)
    user_input_df['related unit'] = user_input_df['related unit'].str.strip()
    user_input_df['related unit'] = user_input_df['related unit'].astype(int)
    
    user_input_df['residents'] = resident_info[resident_info['number'].isin(user_input_df['related unit'])]['residents']
    user_input_df['cost for each unit'] = (user_input_df['amount'] * user_input_df['residents']) // user_input_df['residents'].sum()     
    user_input_df['%share from the whole amount'] = (user_input_df['cost for each unit'] // user_input_df['amount']) * 100
    
    user_input_df.to_csv(root_out, mode = 'a', header = False, index = False)   
    
    return 


def area(root_in: str, root_out: str):
    
    """ This function divides expenses according to the area of each apartment. """
    
    import pandas as pd

    user_input_df = pd.read_excel(root_in, names=['amount','time','category','subcategory','related unit','div'],index_col=False)
    resident_info = pd.read_excel(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژ''ه\data1.xlsx')
    
    user_input_df = user_input_df[user_input_df['div'] == 'area'][['amount','time','category','subcategory','related unit']]
    
    # A series of operations for changing the related unit's class frm object to a list. Useful when executing the explode method
    user_input_df['related unit'] = user_input_df['related unit'].str.replace('[','')
    user_input_df['related unit'] = user_input_df['related unit'].str.replace(']','')
    user_input_df['related unit'] = list(user_input_df['related unit'].str.split(','))
    
    user_input_df = user_input_df.explode('related unit',ignore_index = True)
    user_input_df['related unit'] = user_input_df['related unit'].str.strip()
    user_input_df['related unit'] = user_input_df['related unit'].astype(int)
    
    user_input_df['area'] = resident_info[resident_info['number'].isin(user_input_df['related unit'])]['area']
    user_input_df['cost for each unit'] = (user_input_df['amount'] * user_input_df['area']) // user_input_df['area'].sum()     
    user_input_df['%share from the whole amount'] = (user_input_df['cost for each unit'] // user_input_df['amount']) * 100
    
    user_input_df.to_csv(root_out, mode = 'a', header = False, index = False)   
    
    return


def parking(root_in: str, root_out: str):
    
    """ This function divides expenses according to parkings owned by each apartment. """
    
    import pandas as pd
    
    user_input_df = pd.read_excel(root_in, names=['amount','time','category','subcategory','related unit','div'])
    resident_info = pd.read_excel(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژ''ه\data1.xlsx')
    
    user_input_df = user_input_df[user_input_df['div'] == 'parking'][['amount','time','category','subcategory','related unit']]
    
    # A series of operations for changing the related unit's class frm object to a list. Useful when executing the explode method
    user_input_df['related unit'] = user_input_df['related unit'].str.replace('[','')
    user_input_df['related unit'] = user_input_df['related unit'].str.replace(']','')
    user_input_df['related unit'] = list(user_input_df['related unit'].str.split(','))    
    
    user_input_df = user_input_df.explode('related unit',ignore_index = True)
    user_input_df['related unit'] = user_input_df['related unit'].str.strip()
    user_input_df['related unit'] = user_input_df['related unit'].astype(int)
    
    user_input_df['parkings'] = resident_info[resident_info['number'].isin(user_input_df['related unit'])]['parkings']
    user_input_df['cost for each unit'] = (user_input_df['amount'] * user_input_df['parkings']) // user_input_df['parkings'].sum()     
    user_input_df['%share from the whole amount'] = (user_input_df['cost for each unit'] // user_input_df['amount']) * 100 
    
    user_input_df.to_csv(root_out, mode = 'a', header = False, index = False)   
    
    return


def default(root_in: str, root_out: str):
    
    import pandas as pd
    
    user_input_df = pd.read_csv(root_in, names=['amount','time','category','subcategory','related unit','div'],index_col=False)
    resident_info = pd.read_excel(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژ''ه\data1.xlsx')
    
    user_input_df = user_input_df[user_input_df['div'] == 'default'][['amount','time','category','subcategory','related unit']]
    
    # A series of operations for changing the related unit's class frm object to a list. Useful when executing the explode method
    user_input_df['related unit'] = user_input_df['related unit'].str.replace('[','')
    user_input_df['related unit'] = user_input_df['related unit'].str.replace(']','')
    user_input_df['related unit'] = list(user_input_df['related unit'].str.split(','))
    
    user_input_df = user_input_df.explode('related unit',ignore_index = True)
    user_input_df['related unit'] = user_input_df['related unit'].str.strip()
    user_input_df['related unit'] = user_input_df['related unit'].astype(int)
    
    user_input_df['area'] = resident_info[resident_info['number'].isin(user_input_df['related unit'])]['area']
    user_input_df['cost for each unit'] = user_input_df['amount']
    
    user_input_df.to_csv(root_out, mode = 'a', header = False, index = False)   
    
    return