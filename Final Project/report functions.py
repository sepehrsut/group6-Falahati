# for acquiring a balance for specific units and specified time period please type balance() in python console
# for obtaining a csv file including a transaction history between a specific time period transaction_history() in python console
# for acquiring a percent share from total expenses that categories or subcategories have, please type shares_by_category() or shares_by_category() in python console
# for acquiring a percent share from total expenses that units have, please type shares_by_unit() in python console
chdir(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژه')
def balance():
    
    """ This function calculates the balance for each unit within a specific time period. """
    
    import pandas as pd
    
    user_input_df = pd.read_excel('data3.xlsx')
    
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

def transaction_histoy():
    
    """ This function returns transactions within a specific time period in the form of csv. """
    
    import pandas as pd
    
    transactions = pd.read_excel('data3.xlsx')
    
    # the user enters a time period
    time_period = input('please enter your selected time period as the form yyyy-mm-dd separated by commas with the earlier date typed first. If you want to receive a balance report up to now you must enter the first and the last date that a transaction has been made:').split(',')
    
    # filtering based on time period
    final_df = transactions[(transactions['date'] >= time_period[0]) & (transactions['date'] <= time_period[1])]
    
    final_df.to_csv(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژه\balance.csv', mode= 'w')
    
    return 'A csv file with the name of balance has been created. Please check it.'

def shares_by_category():
    
    """ This function reports the amount share that each category has from the total expenses. """
    
    import pandas as pd
    import matplotlib.pyplot as plt

    user_input_df = pd.read_excel('data2.xlsx') 
    
    shares = user_input_df.groupby('category').aggregate({'amount': 'sum'}).reset_index()
    
    # the % share column demonstrates that what fraction of total expenses belongs to each category
    shares['% share'] = (shares['amount'] / shares['amount'].sum()) * 100
    
    # plotting for better understanding
    plt.pie(shares['amount'], labels = shares['category'], shadow = False, autopct ='%1.f%%')
    plt.title('shares by subcategory')
    plt.show()

    return shares,'A plot has been drawn in the plots pane.Please check it'


def shares_by_subcategory():
    
    """ This function reports the amount share that each subcategory has from the total expenses costed by bills. """
    
    import pandas as pd
    import matplotlib.pyplot as plt

    user_input_df = pd.read_excel('data2.xlsx')
    
    user_input_df = user_input_df[user_input_df['category'] == 'bill']
    shares = user_input_df.groupby('subcategory').aggregate({'amount': 'sum'}).reset_index()
    shares['% share'] = (shares['amount'] / shares['amount'].sum()) * 100

    # plotting for better understanding
    plt.pie(shares['amount'], labels = shares['subcategory'], shadow = True, autopct = '%1.f%%')
    plt.title('shares by subcategory')
    plt.show()
    
    return shares,'A plot has been drawn in the plots pane.Please check it'

def shares_by_unit():
    
    """ This function reports the amount share that each unit has from the total expenses. """
    
    import pandas as pd
    import matplotlib.pyplot as plt
    
    transactions = pd.read_excel('data3.xlsx')
    
    shares = transactions.groupby('unit').aggregate({'cost for each unit': 'sum'}).reset_index()
    shares['% share'] = (shares['cost for each unit'] / shares['cost for each unit'].sum())
    
    # plotting for better understanding
    plt.pie(shares['cost for each unit'], labels = shares['unit'], shadow = True, autopct = '%1.f%%')
    plt.title('shares by unit')
    plt.show()
    
    return shares,'A plot has been drawn in the plots pane. Please chack it.'

def cumulative_sum_for_units():
    
    """ This function returns a cumulative sum for the expenses of each unit based on specified units within a specific time period. """
    
    import pandas as pd
    import matplotlib.pyplot as plt
    
    transactions = pd.read_excel('data3.xlsx')
    
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
    
def cumulative_sum_for_subcategories():
    
    """ This function returns a cumulative sum for the expenses of each subcategory within a specific time period."""
    
    import pandas as pd
    import matplotlib.pyplot as plt

    transactions = pd.read_excel('data3.xlsx')
    
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
    
        
    
    
