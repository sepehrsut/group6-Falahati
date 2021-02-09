# for adding data(bills,elevator,etc.) as input please type append(root_out) in python console which root_out is the path including the name of the csv file that your inputs will be saved in there
# for dividing expenses please run each division function in the python console.
# for acquiring a balance for specific units and specified time period please type balance() in python console
# for obtaining a csv file including a transaction history between a specific time period transaction_history() in python console
# for obtaining a percent share from total expenses categories or subcategories please type share_by_category() or share_by_category() in python console
# l2 = [eval(i) for i in l1[0]]
# df1 = df.iloc[n:m]
# df.index = np.arange(len(df1))
# & user_input_df['category'] == ......

def append(root_out: str):
    """ This function accepts inputs from the user. """
    
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
        append()

############# division functions        
def equal(root_in: str, root_out: str):
   
    """ This function divides expenses evenly between units. """
   
    import pandas as pd
    
    user_input_df = pd.read_csv(root_in, names=['amount','time','category','subcategory','responsible unit','related unit','div'],index_col =False)
    user_input_df = user_input_df[user_input_df['div'] == 'equal'][['amount','time','category','subcategory','related unit']]
            
    # A series of operations for changing the related unit's class frm object to a list. Useful when executing the explode method
    
    user_input_df['related unit'] = user_input_df['related unit'].str.replace('[','')
    user_input_df['related unit'] = user_input_df['related unit'].str.replace(']','')
    user_input_df['related unit'] = list(user_input_df['related unit'].str.split(','))
    
    user_input_df['cost for each unit'] = user_input_df['amount'] // len(user_input_df['related unit'][0])
    user_input_df = user_input_df.explode('related unit')
    user_input_df['related unit'] = user_input_df['related unit'].str.strip()
    
    user_input_df['%share from the whole amount'] = (user_input_df['cost for each unit'] / user_input_df['amount']) * 100
    
    user_input_df.to_csv(root_out, mode = 'a', header = False, index = False)
    
    return


def number(root_in: str, root_out: str):
    
    """ This function divides expenses according to the number of residents living in each apartment. """
    
    import pandas as pd
   
    user_input_df = pd.read_csv(root_in, names=['amount','time','category','subcategory','responsible unit','related unit','div'],index_col=False)
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

    user_input_df = pd.read_csv(root_in, names=['amount','time','category','subcategory','responsible unit','related unit','div'],index_col=False)
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
    
    user_input_df = pd.read_csv(root_in, names=['amount','time','category','subcategory','responsible unit','related unit','div'], index_col= False)
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
    user_input_df['cost for each unit'] = (user_input_df['amount'] * user_input_df['parkings']) // (user_input_df['parkings'].sum())     
    user_input_df['%share from the whole amount'] = (user_input_df['cost for each unit'] // user_input_df['amount']) * 100 
    
    user_input_df.to_csv(root_out, mode = 'a', header = False, index = False)   
    
    return

root_in = r"C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژه\user input data.csv"
root_out = r"C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژه\Taraz.csv"

def default(root_in: str, root_out: str):
    
    import pandas as pd
    
    user_input_df = pd.read_csv(root_in, names=['amount','time','category','subcategory','responsible unit','related unit','div'],index_col=False)
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

def balance():
    
    """ This function calculates the balance for each unit within a specific time period. """
    
    import pandas as pd
    
    user_input_df = pd.read_excel('data3.xlsx')
    selected_units = input('Please enter your selected units separated by commas:').split(',')
    
    # changing the class of selected units
    for i in range(len(selected_units)):
        selected_units[i] = eval(selected_units[i])
        
    time_period = input('please enter your selected time period as the form yyyy-mm-dd separated by commas with the earlier date typed first:').split(',')
    final_balance = user_input_df[(user_input_df['name'].isin(selected_units)) & (user_input_df['date'] >= time_period[0]) & (user_input_df['date'] <= time_period[1])][['name', 'mablagh']]
    final_balance = final_balance.groupby('name').aggregate({'mablagh': 'sum'})
    
    return (final_balance)

def transaction_histoy():
    
    """ This function filters bills within a specific time period. """
    
    import pandas as pd
    
    user_input_df = pd.read_excel('data3.xlsx')
    time_period = input('please enter your selected time period as the form yyyy-mm-dd separated by commas with the earlier date typed first:').split(',')
    final_df = user_input_df[(user_input_df['date'] >= time_period[0]) & (user_input_df['date'] <= time_period[1])]
    final_df.to_csv(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژه\balance.csv', mode= 'w')
    
    return

def share_by_category():
    
    """ This function reports the amount share that each category has from the total expenses. """
    
    import pandas as pd
    import matplotlib.pyplot as plt

    user_input_df = pd.read_excel('data2.xlsx')
    
    shares = user_input_df.groupby('category').aggregate({'amount': 'sum'}).reset_index()
    
    shares['% share'] = (shares['amount'] / shares['amount'].sum()) * 100
    
    # plotting for better understanding
    plt.pie(shares['amount'], labels = shares['category'] , shadow=False, explode=[0.1,0.1,0.1,0.1,0.1,0.1] , autopct='%1.f%%')

    return shares,'A plot has been drawn in the plots pane.Please check it'


def share_by_subcategory():
    
    """ This function reports the amount share that each subcategory has from the total expenses costed by bills. """
    
    import pandas as pd
    import matplotlib.pyplot as plt

    user_input_df = pd.read_excel('data2.xlsx')
    
    user_input_df = user_input_df[user_input_df['category'] == 'bill']
    shares = user_input_df.groupby('subcategory').aggregate({'amount': 'sum'}).reset_index()
    shares['% share'] = (shares['amount'] / shares['amount'].sum()) * 100

    # plotting for better understanding
    plt.pie(shares['amount'], labels = shares['subcategory'] , shadow=True , autopct='%1.f%%')
    
    return shares,'A plot has been drawn in the plots pane.Please check it'



















