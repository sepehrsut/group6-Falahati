# for adding data(bills,elevator,etc.) as input please type append() in python console
# l1 = list(a[a['related unit'] != 'All']['related unit'].str.split(','))
# l2 = [eval(i) for i in l1[0]]
#df1 = df.iloc[n:m]
#df.index = np.arange(len(df1))
#& user_input_df['category'] == ......

def append():
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
        pd.DataFrame(d).to_csv(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژه\user input data.csv',mode = 'a', header= False, index = False)
        return
    else:
        pd.DataFrame(d).to_csv(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژه\user input data.csv',mode = 'a', header = False, index = False)
        append()

def equal():
   
    """ This function divides expenses evenly between tenants. """
   
    import pandas as pd
    
    user_input_df = pd.read_csv('C:/Users/ASUS/Desktop/مبانی برنامه سازی/پروژه/user input data.csv', names=['amount','time','category','subcategory','responsible unit','related unit','div'],index_col =False)
    final_df = user_input_df[user_input_df['div'] == 'equal'][['amount','time','category','subcategory','related unit']]
    final_df['related unit count'] = ((len(user_input_df['related unit'][0]) - 2) // 4) + 2
    final_df['cost for each unit'] = final_df['amount'] // final_df['related unit count']    
    final_df['related unit'] = final_df['related unit'].str.replace('[','')
    final_df['related unit'] = final_df['related unit'].str.replace(']','')
    final_df['related unit'] = list(final_df['related unit'].str.split(','))
    final_df = final_df.explode('related unit')
    final_df['related unit'] = final_df['related unit'].str.strip()
    del final_df['amount']
    final_df.to_csv(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژه\Taraz.csv',mode = 'a', header = False, index = False)
    
    return


def number():
    
    """ This function divides expenses according to the number of people living in each apartment. """
    
    import pandas as pd
   
    user_input_df = pd.read_csv(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژه\user input data.csv', names=['amount','time','category','subcategory','responsible unit','related unit','div'],index_col=False)
    resident_info = pd.read_excel(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژ''ه\data1.xlsx')
    final_df = user_input_df[user_input_df['div'] == 'number'][['amount','time','category','subcategory','related unit']]
    final_df['related unit'] = final_df['related unit'].str.replace('[','')
    final_df['related unit'] = final_df['related unit'].str.replace(']','')
    final_df['related unit'] = list(final_df['related unit'].str.split(','))
    final_df = final_df.explode('related unit',ignore_index = True)
    final_df['related unit'] = final_df['related unit'].str.strip()
    final_df['related unit'] = final_df['related unit'].astype(int)
    final_df['residents'] = resident_info[resident_info['number'].isin(final_df['related unit'])]['residents']
    final_df['cost for each unit'] = (final_df['amount'] * final_df['residents']) // final_df['residents'].sum()     
    del final_df['amount']
    final_df.to_csv(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژه\Taraz.csv',mode = 'a', header = False, index = False)   
    
    return 


def area():
    
    """ This function divides expenses according to the area of each apartment. """
    
    import pandas as pd

    user_input_df = pd.read_csv(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژه\user input data.csv', names=['amount','time','category','subcategory','responsible unit','related unit','div'],index_col=False)
    resident_info = pd.read_excel(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژ''ه\data1.xlsx')
    final_df = user_input_df[user_input_df['div'] == 'area'][['amount','time','category','subcategory','related unit']]
    final_df['related unit'] = final_df['related unit'].str.replace('[','')
    final_df['related unit'] = final_df['related unit'].str.replace(']','')
    final_df['related unit'] = list(final_df['related unit'].str.split(','))
    final_df = final_df.explode('related unit',ignore_index = True)
    final_df['related unit'] = final_df['related unit'].str.strip()
    final_df['related unit'] = final_df['related unit'].astype(int)
    final_df['area'] = resident_info[resident_info['number'].isin(final_df['related unit'])]['area']
    final_df['cost for each unit'] = (final_df['amount'] * final_df['area']) // final_df['area'].sum()     
    del final_df['amount']
    final_df.to_csv(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژه\Taraz.csv',mode = 'a', header = False, index = False)   
    
    return


def parking():
    
    """ This function divides expenses according to parkings owned by each apartment. """
    
    import pandas as pd
    
    user_input_df = pd.read_csv(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژه\user input data.csv', names=['amount','time','category','subcategory','responsible unit','related unit','div'])
    resident_info = pd.read_excel(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژ''ه\data1.xlsx')
    final_df = user_input_df[user_input_df['div'] == 'parking'][['amount','time','category','subcategory','related unit']]
    final_df['related unit'] = final_df['related unit'].str.replace('[','')
    final_df['related unit'] = final_df['related unit'].str.replace(']','')
    final_df['related unit'] = list(final_df['related unit'].str.split(','))    
    final_df = final_df.explode('related unit',ignore_index = True)
    final_df['related unit'] = final_df['related unit'].str.strip()
    final_df['related unit'] = final_df['related unit'].astype(int)
    final_df['parkings'] = resident_info[resident_info['number'].isin(final_df['related unit'])]['parkings']
    final_df['cost for each unit'] = (final_df['amount'] * final_df['parkings']) // final_df['parkings'].sum()     
    del final_df['amount']
    final_df.to_csv(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژه\Taraz.csv',mode = 'a', header = False, index = False)   
    
    return


def default():
    
    import pandas as pd
    
    user_input_df = pd.read_csv(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژه\user input data.csv', names=['amount','time','category','subcategory','responsible unit','related unit','div'],index_col=False)
    resident_info = pd.read_excel(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژ''ه\data1.xlsx')
    final_df = user_input_df[user_input_df['div'] == 'default'][['amount','time','category','subcategory','related unit']]
    final_df['related unit'] = final_df['related unit'].str.replace('[','')
    final_df['related unit'] = final_df['related unit'].str.replace(']','')
    final_df['related unit'] = list(final_df['related unit'].str.split(','))
    final_df = final_df.explode('related unit',ignore_index = True)
    final_df['related unit'] = final_df['related unit'].str.strip()
    final_df['related unit'] = final_df['related unit'].astype(int)
    final_df['area'] = resident_info[resident_info['number'].isin(final_df['related unit'])]['area']
    final_df['cost for each unit'] = final_df['amount']
    del final_df['amount']  
    final_df.to_csv(r'C:\Users\ASUS\Desktop\مبانی برنامه سازی\پروژه\Taraz.csv',mode = 'a', header = False, index = False)   
    
    return



















