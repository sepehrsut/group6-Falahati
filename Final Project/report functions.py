# for acquiring a balance for specific units and specified time period please type balance(root_in) in python console
# for obtaining a csv file including a transaction history between a specific time period transaction_history(root_in, root_out) in python console
# for acquiring a percent share from total expenses that categories or subcategories have, please type portion_by_category(root_in) or portion_by_subcategory(root_in) in python console
# for acquiring a percent share from total expenses that units have, please type portion_by_unit(root_in) in python console
# for acquiring a cumulative sum based on units type cumulative_sum_for_units(root_in) and for acquiring a cumulative sum based on subcategories type cumulative_sum_for_subcategories(root_in) in python console
# for observing a status of the buildings total balance please type negative_balance_error(root_in) in python console
# for acquiring an estimation of next year's monthly expenses for each unit please type next_year_expenditure_estimation(root_in, root_info) in python console

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
        file containing transactions.  """
    
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
        and the name of the excel file containing transactions. """
    
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
        file containing transactions. """
    
    import pandas as pd
    import matplotlib.pyplot as plt
    
    transactions = pd.read_excel(root_in)
    
    shares = transactions.groupby('unit').aggregate({'cost for each unit': 'sum'}).reset_index()
    shares['% share'] = (shares['cost for each unit'] / shares['cost for each unit'].sum()) * 100
    
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
    
    
