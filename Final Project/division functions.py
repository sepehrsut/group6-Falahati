# for dividing expenses please type execute_all_division_funcs(root_in, root_out, root_info) in python console

def equal(root_in: str, root_out: str):
   
    """ This function divides expenses evenly between units. The root_in
        variable is the path and the name of your user input data excel file.
        The root_out variable is the path and the name of the csv file that 
        you want to save your transactions after running the function. """
   
    import pandas as pd
    import numpy as np
    
    user_input_df = pd.read_excel(root_in, names=['amount','time','category','subcategory','related unit','div'],index_col =False)
    user_input_df = user_input_df[user_input_df['div'] == 'equal'][['amount','time','category','subcategory','related unit']]
            
    # A series of operations for changing the related unit's class from object to a list. Useful when executing the explode method
    
    user_input_df['related unit'] = user_input_df['related unit'].str.replace('[','')
    user_input_df['related unit'] = user_input_df['related unit'].str.replace(']','')
    user_input_df['related unit'] = user_input_df['related unit'].str.replace(' ','')
    user_input_df['related unit'] = list(user_input_df['related unit'].str.split(','))

    costs_for_each_unit = []
    for i in range(len(user_input_df['related unit'])):
         costs_for_each_unit.append(user_input_df.iloc[i]['amount'] // len(user_input_df.iloc[i]['related unit']))
    user_input_df['cost for each unit'] = np.array(costs_for_each_unit)
    user_input_df = user_input_df.explode('related unit')
        
    user_input_df.to_csv(root_out, mode = 'a', header = False, index = False)
    
    return


def number(root_in: str, root_out: str, root_info: str):
    
    """ This function divides expenses according to the number of 
        living in each apartment. The root_in variable is the path and the name
        of your user input data excel file. The root_out variable is the path
        and the name of the csv file that you want to save your transactions
        after running the function. The root_info variable is the path and the
        name your building residents' information excel file. """
    
    import pandas as pd
    import numpy as np
   
    user_input_df = pd.read_excel(root_in, names=['amount','time','category','subcategory','related unit','div'],index_col=False)
    resident_info = pd.read_excel(root_info)
    
    # Changing the column name and making it the same as the other dataframe. Useful when performing merge
    resident_info = resident_info.rename(columns = {'number': 'related unit'})
    
    user_input_df = user_input_df[user_input_df['div'] == 'number'][['amount','time','category','subcategory','related unit']]
    
    # A series of operations for changing the related unit's class from object to a list. Useful when executing the explode method
    user_input_df['related unit'] = user_input_df['related unit'].str.replace('[','')
    user_input_df['related unit'] = user_input_df['related unit'].str.replace(']','')
    user_input_df['related unit'] = user_input_df['related unit'].str.replace(' ','')
    user_input_df['related unit'] = list(user_input_df['related unit'].str.split(','))

    
    # Calculating the total residents that each row's related units have and adding them as a new column to user_input_df.
    resident_info['related unit'] = resident_info['related unit'].astype(str)
    total_residents = []
    for i in range(len(user_input_df['related unit'])):
        total = resident_info[resident_info['related unit'].isin(user_input_df.iloc[i]['related unit'])]['residents'].sum()
        total_residents.append(total)
    user_input_df['total resident'] = np.array(total_residents)
    
    user_input_df = user_input_df.explode('related unit',ignore_index = True)
    
    # Adding the related residents of each unit after the explosion method
    user_input_df = resident_info[['residents','related unit']].merge(user_input_df, on = 'related unit')
    
    user_input_df['cost for each unit'] = (user_input_df['amount'] * user_input_df['residents']) // user_input_df['total resident']    
    
    del user_input_df['total resident']
    del user_input_df['residents']
    
    user_input_df.to_csv(root_out, mode = 'a', header = False, index = False)   
    
    return 


def area(root_in: str, root_out: str, root_info: str):
    
    """ This function divides expenses according to the area of each apartment.
        The root_in variable is the path and the name of your user input data
        excel file. The root_out variable is the path and the name of the csv
        file that you want to save your transactions after running the function.
        The root_info variable is the path and the name your building residents'
        information excel file. """
    
    import pandas as pd
    import numpy as np

    user_input_df = pd.read_excel(root_in, names=['amount','time','category','subcategory','related unit','div'],index_col=False)
    resident_info = pd.read_excel(root_info)

    # Changing the column name and making it the same as the other dataframe. Useful when performing merge
    resident_info = resident_info.rename(columns = {'number': 'related unit'})
    
    user_input_df = user_input_df[user_input_df['div'] == 'area'][['amount','time','category','subcategory','related unit']]
    
    # A series of operations for changing the related unit's class frm object to a list. Useful when executing the explode method
    user_input_df['related unit'] = user_input_df['related unit'].str.replace('[','')
    user_input_df['related unit'] = user_input_df['related unit'].str.replace(']','')
    user_input_df['related unit'] = user_input_df['related unit'].str.replace(' ','')
    user_input_df['related unit'] = list(user_input_df['related unit'].str.split(','))
    
    # Calculating the total residents that each row's related units have and adding them as a new column to user_input_df.
    resident_info['related unit'] = resident_info['related unit'].astype(str)
    total_areas = []
    for i in range(len(user_input_df['related unit'])):
        total = resident_info[resident_info['related unit'].isin(user_input_df.iloc[i]['related unit'])]['area'].sum()
        total_areas.append(total)
    user_input_df['total area'] = np.array(total_areas)
    
    user_input_df = user_input_df.explode('related unit',ignore_index = True)
    
    # Adding the related residents of each unit after the explosion method
    user_input_df = resident_info[['area','related unit']].merge(user_input_df, on = 'related unit')
    
    user_input_df['cost for each unit'] = (user_input_df['amount'] * user_input_df['area']) // user_input_df['total area']    
    
    del user_input_df['total area']
    del user_input_df['area']
    
    user_input_df.to_csv(root_out, mode = 'a', header = False, index = False)   
    
    return


def parking(root_in: str, root_out: str, root_info: str):
    
    """ This function divides expenses according to parkings owned by each
        apartment. The root_in variable is the path and the name of your user 
        input data excel file. The root_out variable is the path and the name 
        of the csv file that you want to save your transactions after running
        the function. The root_info variable is the path and the name your
        building residents' information excel file. """
    
    import pandas as pd
    import numpy as np
    
    user_input_df = pd.read_excel(root_in, names=['amount','time','category','subcategory','related unit','div'], index_col= False)
    resident_info = pd.read_excel(root_info)
    
    # Changing the column name and making it the same as the other dataframe. Useful when performing merge
    resident_info = resident_info.rename(columns = {'number': 'related unit'})
    
    user_input_df = user_input_df[user_input_df['div'] == 'parking'][['amount','time','category','subcategory','related unit']]
    
    # A series of operations for changing the related unit's class frm object to a list. Useful when executing the explode method
    user_input_df['related unit'] = user_input_df['related unit'].str.replace('[','')
    user_input_df['related unit'] = user_input_df['related unit'].str.replace(']','')
    user_input_df['related unit'] = user_input_df['related unit'].str.replace(' ','')
    user_input_df['related unit'] = list(user_input_df['related unit'].str.split(','))
    
    # Calculating the total residents that each row's related units have and adding them as a new column to user_input_df.
    resident_info['related unit'] = resident_info['related unit'].astype(str)
    total_parkings = []
    for i in range(len(user_input_df['related unit'])):
        total = resident_info[resident_info['related unit'].isin(user_input_df.iloc[i]['related unit'])]['parkings'].sum()
        total_parkings.append(total)
    user_input_df['total parking'] = np.array(total_parkings)
    
    user_input_df = user_input_df.explode('related unit',ignore_index = True)
    
    # Adding the related residents of each unit after the explosion method
    user_input_df = resident_info[['parkings','related unit']].merge(user_input_df, on = 'related unit')
    
    user_input_df['cost for each unit'] = (user_input_df['amount'] * user_input_df['parkings']) // user_input_df['total parking']    
    
    del user_input_df['total parking']
    del user_input_df['parkings']
    
    user_input_df.to_csv(root_out, mode = 'a', header = False, index = False)   
    
    return


def default(root_in: str, root_out: str, root_info: str):
    
    """ This function adds the amount to each units balance. The root_in
        variable is the path and the name of your user input data excel file.
        The root_out variable is the path and the name of the csv file that
        you want to save your transactions after running the function. The
        root_info variable is the path and the name your building residents' 
        information excel file. """
    
    import pandas as pd
    
    user_input_df = pd.read_excel(root_in, names=['amount','time','category','subcategory','related unit','div'],index_col=False)
    
    user_input_df = user_input_df[user_input_df['div'] == 'default'][['amount','time','category','subcategory','related unit']]
    
    # A series of operations for changing the related unit's class frm object to a list. Useful when executing the explode method
    user_input_df['related unit'] = user_input_df['related unit'].str.replace('[','')
    user_input_df['related unit'] = user_input_df['related unit'].str.replace(']','')
    user_input_df['related unit'] = user_input_df['related unit'].str.replace(' ','')
    user_input_df['related unit'] = list(user_input_df['related unit'].str.split(','))
    
    user_input_df = user_input_df.explode('related unit',ignore_index = True)
    
    user_input_df['cost for each unit'] = user_input_df['amount']
    
    user_input_df.to_csv(root_out, mode = 'a', header = False, index = False)   
    
    return

def execute_all_division_funcs(root_in: str, root_out: str, root_info: str):
    
    equal(root_in, root_out)
    number(root_in, root_out, root_info)
    area(root_in, root_out, root_info)
    parking(root_in, root_out, root_info)
    
    return
