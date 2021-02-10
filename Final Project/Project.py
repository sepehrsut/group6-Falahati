# for adding data(bills,elevator,etc.) as input please type append(root_out) in python console which root_out is the path including the name of the csv file that your inputs will be saved in there
# for dividing expenses please type execute_all_division_funcs(root_in, root_out, root_info) in python console
# for acquiring a balance for specific units and specified time period please type balance(root_in) in python console
# for obtaining a csv file including a transaction history between a specific time period transaction_history(root_in) in python console
# for acquiring a percent share from total expenses that categories or subcategories have, please type portion_by_category(root_in) or portion_by_subcategory(root_in) in python console
# for acquiring a percent share from total expenses that units have, please type portion_by_unit(root_in) in python console
# for acquiring a cumulative sum based on units type cumulative_sum_for_units(root_in) and for acquiring a cumulative sum based on subcategories type cumulative_sum_for_subcategories(root_in) in console python
# for observing a status of the buildings total balance please type negative_balance_error(root_in) in python console

def append(root_out: str):
    
    """ This function accepts inputs from the user. The root_out variable is
    the path and the name of the csv file that you want to save your inputs into. """
    
    import pandas as pd
    import datetime as dt
    
    d = {'amount': [], 'time':[], 'category': [] , 'subcategory': [],
     'responsible unit': [], 'related unit': [[]],
     'div': [], 'description': []}
    
    amount = int(input('amount:'))
    d['amount'].append(amount)
    
    time = input('time( Example: 1399/09/21 ) : ')
    d['time'].append(dt.date(int(time[0:4]),int(time[5:7]), int(time[8:])))
    
    category = input("category: 1) bill 2) cleaning 3) elevator 4) parking 5) repairs 6) charge 7) other [1/2/3/4/5/6/7] :")
    if category == '1':
        d['category'].append('bill')
    elif category == '2':
        d['category'].append('cleaning')
    elif category == '3':
        d['category'].append('elevator')
    elif category == '4':
        d['category'].append('parking')
    elif category == '5':
        d['category'].append('repairs')
    elif category == '6':
        d['category'].append('charge')
    elif category == '7':
        d['category'].append('other')
        
    if category == '1':
        subcategory = input('subcategory: 1) water 2) gas 3) electricity 4) tax [1/2/3/4] :')
        if subcategory == '1':
            subcategory = 'water'
        elif subcategory == '2':
            subcategory = 'gas'
        elif subcategory == '3':
            subcategory = 'electricity'
        elif subcategory == '4':
            subcategory = 'tax'
    else:
        subcategory = 'undefind'
    d['subcategory'].append(subcategory)
    
    responsible_unit = input('responsible unit:')
    d['responsible unit'].append(responsible_unit)
    
    related_unit = input('related unit:(please enter the related units as the form first unit number, second unit number,....Note that if you want to include all units you should enter the number of all units)').split(',')
    for e in related_unit:
        d['related unit'][0].append(eval(e))
    
    div = input('div: 1) -e 2) -r 3) -d 4) -a 5) -p [1/2/3/4/5] :(Note that if you have selected charge as a category, -d must be chosen as the division type.)')
    if div == '1':
        div = 'equal'
        d['div'].append(div)
    elif div == '2':
        div = 'number'
        d['div'].append(div)
    elif div == '3':
        div = 'default'
        d['div'].append(div)
    elif div == '4':
        div = 'area'
        d['div'].append(div)
    elif div == '5':
        div = 'parking'
        d['div'].append(div)
    
    description = input('description:')
    d['description'].append(description)
    
    i = input('Is there anything left? A)yes B)no [A/B] :')
    if i == 'B':
        pd.DataFrame(d).to_csv(root_out, mode = 'a', header= False, index = False)
        return
    else:
        pd.DataFrame(d).to_csv(root_out, mode = 'a', header = False, index = False)
        append(root_out)

############# expense division functions        


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


############# report functions


def balance(root_in: str):
    
    """ This function calculates the balance for each unit within a specific
    time period. The root_in variable is the path and the name of the excel file
    containing transactions. """
    
    import pandas as pd
    
    user_input_df = pd.read_excel(root_in)
    
    # the user enters the specified units and the time period
    selected_units = input('Please enter your selected units separated by commas. You can type all if you want to include all units:').split(',')
    time_period = input('please enter your selected time period as the form yyyy-mm-dd separated by commas with the earlier date typed first. If you want to receive a balance report up to now you must enter the first and the last date that a transaction has been made:').split(',')
    
    # changing the class of selected units from str to int
    for i in range(len(selected_units)):
        selected_units[i] = eval(selected_units[i])
          
    if selected_units == 'all':
        
        final_balance = user_input_df[(user_input_df['date'] >= time_period[0]) & (user_input_df['date'] <= time_period[1])].groupby('unit').aggregate({'cost for each unit': 'sum'}).reset_index()
        return final_balance
   
    else:
        
        final_balance = user_input_df[(user_input_df['date'] >= time_period[0]) & (user_input_df['date'] <= time_period[1]) & (user_input_df['unit'].isin(selected_units))][['unit', 'cost for each unit']].groupby('unit').aggregate({'cost for each unit': 'sum'}).reset_index()
        return final_balance

def transaction_histoy(root_in: str, root_out: str):
    
    """ This function returns transactions within a specific time period in the
        form of csv. The root_in variable is the path and the name of the excel
        file containing transactions. The root_out variable is the path and the
        name of the csv file that you want the reports to be saved. """
    
    import pandas as pd
    
    transactions = pd.read_excel(root_in)
    
    # the user enters a time period
    time_period = input('please enter your selected time period as the form yyyy-mm-dd separated by commas with the earlier date typed first. If you want to receive a balance report up to now you must enter the first and the last date that a transaction has been made:').split(',')
    
    # filtering based on time period
    final_df = transactions[(transactions['date'] >= time_period[0]) & (transactions['date'] <= time_period[1])]
    
    final_df.to_csv(root_out, mode= 'w')
    
    return 'A csv file with the name of balance has been created. Please check it.'

def portion_by_category(root_in: str):
    
    """ This function reports the amount share that each category has from the
        total expenses. The root_in variable is the path and the name of the excel
        file containing transactions."""
    
    import pandas as pd
    import matplotlib.pyplot as plt

    user_input_df = pd.read_excel(root_in) 
    
    shares = user_input_df.groupby('category').aggregate({'amount': 'sum'}).reset_index()
    
    # the % share column demonstrates that what fraction of total expenses belongs to each category
    shares['% share'] = (shares['amount'] / shares['amount'].sum()) * 100
    
    # plotting for better understanding
    plt.pie(shares['amount'], labels = shares['category'], shadow = False, autopct ='%1.f%%')
    plt.title('shares by subcategory')
    plt.show()

    return shares,'A plot has been drawn in the plots pane.Please check it'


def portion_by_subcategory(root_in: str):
    
    """ This function reports the amount share that each subcategory has from
        the total expenses costed by bills. The root_in variable is the path 
        and the name of the excel file containing transactions."""
    
    import pandas as pd
    import matplotlib.pyplot as plt

    user_input_df = pd.read_excel(root_in)
    
    user_input_df = user_input_df[user_input_df['category'] == 'bill']
    shares = user_input_df.groupby('subcategory').aggregate({'amount': 'sum'}).reset_index()
    shares['% share'] = (shares['amount'] / shares['amount'].sum()) * 100

    # plotting for better understanding
    plt.pie(shares['amount'], labels = shares['subcategory'], shadow = True, autopct = '%1.f%%')
    plt.title('shares by subcategory')
    plt.show()
    
    return shares,'A plot has been drawn in the plots pane.Please check it'

def portion_by_unit(root_in: str):
    
    """ This function reports the amount share that each unit has from 
        total expenses. The root_in variable is the path and the name of the excel
        file containing transactions."""
    
    import pandas as pd
    import matplotlib.pyplot as plt
    
    transactions = pd.read_excel(root_in)
    
    shares = transactions.groupby('unit').aggregate({'cost for each unit': 'sum'}).reset_index()
    shares['% share'] = (shares['cost for each unit'] / shares['cost for each unit'].sum())
    
    # plotting for better understanding
    plt.pie(shares['cost for each unit'], labels = shares['unit'], shadow = True, autopct = '%1.f%%')
    plt.title('shares by unit')
    plt.show()
    
    return shares,'A plot has been drawn in the plots pane. Please chack it.'

def negative_balance_error(root_in: str):  
    
    """ This function returns a warning if the buildings total balance is negative.
        The root_in variable is the path and the name of the excel file
        containing transactions. """

    import pandas as pd
    
    transactions = pd.read_excel(root_in)

    income = transactions[transactions['category'] == 'charge']['cost for each unit'].sum()
    expenses = transactions[transactions['category'] != 'charge']['cost for each unit'].sum()
    total_balance = income - expenses
    
    if total_balance >= 0:
        return ('Your total balance is' + str(total_balance)+ ', All expenses have been paid.')
    else:
        return ('Warning! You have negative total balance. You need at least' + str(abs(total_balance)))

def cumulative_sum_for_units(root_in: str):
    
    """ This function returns a cumulative sum for the expenses of each unit
        based on specified units within a specific time period. The root_in
        variable is the path and the name of the excel file containing transactions. """
    
    import pandas as pd
    import matplotlib.pyplot as plt
    
    transactions = pd.read_excel(root_in)
    
    # the user enters the specified units and subcategories and time period
    selected_subcategories = input('Please enter your specified subcategories separated by commas. You can type all if you want to include all subcategories: ')
    selected_units = input('Please enter your specified units separated by commas and all lower case. You can type all if you want to include all units: ')
    time_period = input('please enter your selected time period as the form yyyy-mm-dd separated by commas with the earlier date typed first. If you want to receive a balance report up to now you must enter the first and the last date that a transaction has been made: ').split(',')
    
    if (selected_subcategories == 'all') and (selected_units == 'all'):
        
        # filtering by time period
        transactions = transactions[(transactions['date'] >= time_period[0]) & (transactions['date'] <= time_period[1])].groupby('unit').aggregate({'cost for each unit': 'sum'}).reset_index()
        
        units = transactions['unit']
        del transactions['unit']
        
        cumulative_sum = transactions.cumsum()
        
        # plotting
        plt.bar(units, cumulative_sum['cost for each unit'])
        plt.xlabel('unit')
        plt.ylabel('cumulative sum')
        plt.title('cumulative sum for units')
        plt.show()
        
        return 'A plot has been drawn in the plots pane. Please check it.'
    
    elif (selected_subcategories == 'all') and (selected_units != 'all'):
        
        selected_units = selected_units.split(',')
        
        # changing the class of selected units from str to int
        for i in range(len(selected_units)):
            selected_units[i] = int(selected_units[i])
        
        # filtering by selected units and time period
        transactions = transactions[(transactions['date'] >= time_period[0]) & (transactions['date'] <= time_period[1]) & (transactions['unit'].isin(selected_units))].groupby('unit').aggregate({'cost for each unit': 'sum'}).reset_index()
        
        units = transactions['unit']
        del transactions['unit']
        
        cumulative_sum = transactions.cumsum()
        
        # plotting
        plt.bar(units, cumulative_sum['cost for each unit'])
        plt.xlabel('unit')
        plt.ylabel('cumulative sum')
        plt.title('cumulative sum for units')
        plt.show()
        
        return 'A plot has been drawn in the plots pane. Please check it.'
    
    elif (selected_subcategories != 'all') and (selected_units == 'all'):
                
        selected_subcategories = selected_subcategories.split(',')
        
        # if specific subcategories are included then the category column must be a bill
        transactions = transactions[(transactions['date'] >= time_period[0]) & (transactions['date'] <= time_period[1]) & (transactions['category'] == 'bill') & (transactions['subcategory'].isin(selected_subcategories))].groupby('unit').aggregate({'cost for each unit': 'sum'}).reset_index()
        
        units = transactions['unit']
        del transactions['unit']
        
        cumulative_sum = transactions.cumsum()
        
        # plotting
        plt.bar(units, cumulative_sum['cost for each unit'])
        plt.xlabel('unit')
        plt.ylabel('cumulative sum')
        plt.title('cumulative sum for units')
        plt.show()
        
        return 'A plot has been drawn in the plots pane. Please check it.'
    
    elif (selected_subcategories != 'all') and (selected_units != 'all'):
        
        selected_units = selected_units.split(',')
        selected_subcategories = selected_subcategories.split(',')
        
        # changing the class of selected units from str to int
        for i in range(len(selected_units)):
            selected_units[i] = int(selected_units[i])
            
        # filtering by specified units and subcategories and time period          
        transactions = transactions[(transactions['date'] >= time_period[0]) & (transactions['date'] <= time_period[1]) & (transactions['unit'].isin(selected_units)) & (transactions['category'] == 'bill') & (transactions['subcategory'].isin(selected_subcategories))].groupby('unit').aggregate({'cost for each unit': 'sum'}).reset_index()
        
        units = transactions['unit']
        del transactions['unit']
        
        cumulative_sum = transactions.cumsum()
        
        # plotting
        plt.bar(units, cumulative_sum['cost for each unit'])
        plt.xlabel('unit')
        plt.ylabel('cumulative sum')
        plt.title('cumulative sum for units')
        plt.show()
        
        return 'A plot has been drawn in the plots pane. Please check it.'
    
def cumulative_sum_for_subcategories(root_in: str):
    
    """ This function returns a cumulative sum for the expenses of each
        subcategory within a specific time period. The root_in variable is the
        path and the name of the excel file containing transactions."""
    
    import pandas as pd
    import matplotlib.pyplot as plt

    transactions = pd.read_excel(root_in)
    
    # if specific subcategories are included then the category column must be a bill
    transactions = transactions[transactions['category'] == 'bill']
    
    # the user enters the specified subcategories and time period
    selected_subcategories = input('Please enter your specified subcategories separated by commas. You can type all if you want to include all subcategories: ')
    time_period = input('please enter your selected time period as the form yyyy-mm-dd separated by commas with the earlier date typed first. If you want to receive a balance report up to now you must enter the first and the last date that a transaction has been made: ').split(',')
    
    if selected_subcategories == 'all':
        
        # filtering by time period
        transactions = transactions[(transactions['date'] >= time_period[0]) & (transactions['date'] <= time_period[1])].groupby('subcategory').aggregate({'cost for each unit': 'sum'}).reset_index()
        
        subcategories = transactions['subcategory']
        del transactions['subcategory']
        
        cumulative_sum = transactions.cumsum()
        
        # plotting
        plt.bar(subcategories, cumulative_sum['cost for each unit'])
        plt.xlabel('subcategory')
        plt.ylabel('cumulative sum')
        plt.title('cumulative sum for subcategories')
        plt.show()
        
        return 'A plot has been drawn in the plots pane. Please check it.'
    
    else:
        
        selected_subcategories = selected_subcategories.split(',')
        
        # filtering by specified subcategories and time period
        transactions = transactions[(transactions['date'] >= time_period[0]) & (transactions['date'] <= time_period[1]) & (transactions['subcategories'].isin(selected_subcategories))].groupby('subcategory').aggregate({'cost for each unit': 'sum'}).reset_index()
        
        subcategories = transactions['subcategory']
        del transactions['subcategory']
        
        cumulative_sum = transactions.cumsum()
        
        # plotting
        plt.bar(subcategories, cumulative_sum['cost for each unit'])
        plt.xlabel('subcategory')
        plt.ylabel('cumulative sum')
        plt.title('cumulative sum for subcategories')
        plt.show()
        
        return 'A plot has been drawn in the plots pane. Please check it.'
    
def next_year_expenditure_estimation(root_in: str, root_info: str):
    
    """ This function estimates the amount of expenses that each unit should pay
        in the next year. The root_in variable is the path and the name of the
        excel file containing transactions. """
    
    import pandas as pd
    
    user_input_df = pd.read_excel(root_in)
    resident_info = pd.read_excel(root_info)
    inflation_rate = 1.1
    
    user_input_df = user_input_df[user_input_df['category'] != 'charge']
    last_year_total_costs = user_input_df[(user_input_df['time'] >= (user_input_df['time'].iloc[-1][0:5] + '01-01')) & (user_input_df['time'] <= user_input_df['time'].iloc[-1])]['amount'].sum()
    next_year_expenditure_projection = last_year_total_costs * inflation_rate
    unit_next_year_monthly_payment = next_year_expenditure_projection // (12 * len(resident_info['number']))
    
    return unit_next_year_monthly_payment 

def execute_all_division_funcs(root_in: str, root_out: str, root_info: str):
    
    equal(root_in, root_out)
    number(root_in, root_out, root_info)
    area(root_in, root_out, root_info)
    parking(root_in, root_out, root_info)
    
    return













