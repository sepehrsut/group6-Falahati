# group6 - اسقف Project

## Group Member
  1. [MohammadHosein Falahati](#mohammadHosein-falahati) : Head Of The Group/coder
  2. [Sepehr Harirchian](#sepehr-harirchian) : coder(debuger)
  3. [Amirhosein GhaziMoradi](#amirhosein-ghazimoradi) : coder 
  4. [AhmadReza AliHoseini](#ahmadreza-alihoseini) : coder
## Table of Contents
  1. [Introduction](#introduction)
  2. [Append Function](#append-function)
  3. [Division Function](#division-function)
     1. [equal](#equal)
     2. [number](#number)
     3. [area](#area)
     4. [parking](#parking)
     5. [default](#default)
  4. [Report Function](#report-function)
     1. [balance](#balance)
     2. [transaction histoy](#transaction-histoy)
     3. [portion by category](#portion-by-category)
     4. [portion by subcategory](#portion-by-subcategory)
     5. [portion by unit](#portion-by-unit)
     6. [negative balance error](#negative-balance-error)
     7. [cumulative sum for units](#cumulative-sum-for-units)
     8. [cumulative sum for subcategory](#cumulative-sum-for-subcategory)
     9. [next year expenditure estimation](#next-year-expenditure-estimation)
  5. [Conculusion](#conculusion)
  
## Introduction
In order to adjust the building expenses, each building manager must calculate all the minor expenses and figure out how to divide each of them, and also report to the occupants at the end. All of this is time consuming for one person and organizing the whole paper and work invoice is very difficult to handle. Therefore, in the age of technology, various programs and softwares have been written to facilitate the work and organize these costs, one of which is our project (اسقف team), which helps the building manager to eliminate all additional building costs.Our program consists of three parts: 1.Input(append func) 2.div(division func) 3.report func
In the input section(append func), the building manager only needs to give the total costs of the building and in the other two sections, the costs of each unit in the ways specified by the manager, such as the aggregate cost chart, financial balance and invoices of the units,and etc. is demonstrated.

[*summary*](https://github.com/FAHM7380/group6-Falahati/blob/main/summary.png?raw=true)

## **Append Function**

The append function is the part where the building manager must give the information such as total cost, related unit and etc. to the console. the given information, is recorded in a dictionary.The dictionary "d" keys contain our columns and its values are the building manager data recorded in the console

    def append(root_out: str):
      """ This function accepts inputs from the user. """
    
      import pandas as pd
      import datetime as dt
      d = {'amount': [], 'date':[], 'category': [] , 'subcategory': [],
     'responsible unit': [], 'related unit': [[]],
     'div': [], 'description': []}
     
These dictionary keys include the amount or the same cost, the time of the transaction, the category and subcategory of this cost, the head of the department who is usually the building manager, the unit related to that cost and how to divide it and describe it.
   
    amount = int(input('amount:'))
    d['amount'].append(amount)
    
    time = input('date( Example: 1399/09/21 ) : ')
    d['time'].append(dt.date(int(time[0:4]),int(time[5:7]), int(time[8:])))
    
In the category section and the rest of the input sections, we acted as a few options so that the building manager could easily do the building work and spend less time typing. 
    
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
        
Also, in the subcategory section, which was only related to the building bills section, it only displays for the manager when the building manager writes the number 1 in the category section.
        
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
        
In the div section, which is the most important part of our input function, the building manager, after entering the relevant option, causes the division functions to calculate the costs of each unit.

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
    
At the end of the input, after receiving this information from the building manager, we ask the manager if there is still other data that needs to be recorded. If he clicks yes, all of these input processes will be repeated until the last question is answered. If he clicks no, the process stops and all of the data will enter the dataframe space.also, the dataframe is saved as a csv file for further operations.

    i = input('Is there anything left? A)yes B)no [A/B] :')
    if i == 'B':
        pd.DataFrame(d).to_csv(root_out, mode = 'a', header= False, index = False)
        return
    else:
        pd.DataFrame(d).to_csv(root_out, mode = 'a', header = False, index = False)
        append()
**[⬆ back to top](#table-of-contents)**

## **Division Function**

Division functions are a group of functions that divide the price between units based on the inputs of the building manager in the previous section, as stated in the functions. This group of functions includes 5 ***equal, number, area, parking and default functions***, of which the 3 functions ***number***, ***area***, ***parking*** have almost the same algorithm, except that they are calculated based on the area of the units or the number of parking spaces or the number of people.
The ***equal function*** also divides a cost equally between units, which is the most common method of calculation in buildings.
Finally, the ***default function*** is used to calculate the building charge, which is always a constant value and is evenly divided between the units.

### *equal*

    def equal(root_in: str, root_out: str):
   
      """ This function divides expenses evenly between units. The root_in
          variable is the path and the name of your user input data excel file.
          The root_out variable is the path and the name of the csv file that 
          you want to save your transactions after running the function. """
   
      import pandas as pd
      import numpy as np
    
      user_input_df = pd.read_excel(root_in, names=['amount','time','category','subcategory','related unit','div'],index_col =False)
      user_input_df = user_input_df[user_input_df['div'] == 'equal'][['amount','time','category','subcategory','related unit']].reset_index()
            
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
      
### *number*

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
      
### *area*

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
      
### *parking*

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

### *default*

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

 **[⬆ back to top](#table-of-contents)**
 
## **Report Function**

Report functions return a wide range of building’s financial reports such as cumulative sum graphs, transaction histories etc. About ten functions make it possible for the building manager to get an overview of the residents’ payments and building expenses.

The ***balance function*** provides each unit’s total payments in a desired time period.

A history of transactions in a specified time is also delivered as a csv file to the user by the ***transaction_history function***. 

Functions starting with the word ***portion_by*** illustrate each unit, category or subcategory’s fraction of the total expenses.

Whenever the building’s total balance is negative, the ***negative_balance_error function*** rises a warning otherwise it shows the excess amount of money. 

The ***cumulative_sum functions*** (for unit or subcategory) provide a cumulative sum graph of the building’s costs with the capability of being filtered based on a range of parameters either grouped by units or subcategories. 

The last but not least is the ***next_year_expenditure_estimation function*** which basically projects each unit’s next year monthly expenses (perhaps charge) with considering the inflation rate in the calculations.

### *balance*

    def balance(root_in: str):
    
      """ This function calculates the balance for each unit within a specific
          time period. The root_in variable is the path and the name of the excel file
          containing transactions. """
    
      import pandas as pd
    
      user_input_df = pd.read_excel(root_in)
    
    # the user enters the specified units and the time period
      selected_units = input('Please enter your selected units separated by commas. You can type all if you want to include all units:').split(',')
      time_period = input('please enter your selected time period as the form yyyy-mm-dd separated by commas with the earlier date typed first. If you want to receive a balance  report up to now you must enter the first and the last date that a transaction has been made:').split(',')
    
    # changing the class of selected units from str to int
      for i in range(len(selected_units)):
          selected_units[i] = eval(selected_units[i])
          
      if selected_units == 'all':
        
         final_balance = user_input_df[(user_input_df['date'] >= time_period[0]) & (user_input_df['date'] <= time_period[1])].groupby('unit').aggregate({'cost for each unit':  'sum'}).reset_index()
          return final_balance
   
      else:
        
          final_balance = user_input_df[(user_input_df['date'] >= time_period[0]) & (user_input_df['date'] <= time_period[1]) & (user_input_df['unit'].isin(selected_units))] [['unit', 'cost for each unit']].groupby('unit').aggregate({'cost for each unit': 'sum'}).reset_index()
          return final_balance
 
 ### *transaction histoy*
 
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

 ### *portion by category*
 
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
      plt.title('portion by subcategory')
      plt.show()

      return shares,'A plot has been drawn in the plots pane.Please check it'
 
 
 ### *portion by subcategory*
 
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
      plt.title('portion by subcategory')
      plt.show()
      
      return shares,'A plot has been drawn in the plots pane.Please check it'
 
 ### *portion by unit*
 
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
      plt.title('portion by unit')
      plt.show()
    
      return shares,'A plot has been drawn in the plots pane. Please chack it.'
 
 ### *negative balance error*
 
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
 
 ### *cumulative sum for units*
 
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
          
**[⬆ back to top](#table-of-contents)** 
 
 ### *cumulative sum for subcategory*
 
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
          
 **[⬆ back to top](#table-of-contents)**         

### *next year expenditure estimation*

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
 
 **[⬆ back to top](#table-of-contents)**


## **Conculusion**

### Member performance report:
input functions were written by **[MohammadHossein Falahati](#group-member)** with the help of **[Sepehr Harirchian](#group-member)**.
The report function was written by **[AhmadReza AliHosseini](#group-member)** and **[AmirHossein GhaziMoradi](#group-member)**.
Computational functions and how to divide costs were written by **[AhmadReza AliHosseini](#group-member)** and **[AmirHossein GhaziMoradi](#group-member)** and finally debugged and highly optimized by **[Sepehr Harirchian](#group-member)**.
The report writing and presentation of the project in Git hub was done by **[MohammadHossein Falahati](#group-member)** and **[AmirHossein GhaziMoradi](#group-member)** with translation correction by **[Sepehr Harirchian](#group-member)**.

### The work process and challenges in the project:
At first the group focused on accepting inputs from user and came to the conclusion that the program must accept inputs using while and if loops.
One challenge was in the expense’s division functions. We didn’t have an idea how to divide the expenses between related units, and another problem was that we didn’t know how to put the distributed costs in a new database, which was solved by asking the project guide and searching.
Although the report functions had a lot of syntax, we were able to successfully overcome this challenge due to previous familiarity.
One of our biggest challenges was that at first our functions were performed on all units, but later we realized that some costs may not apply to some units. Unfortunately, we did not find a solution to solve this problem, so the group decided to enter the desired units manually, which of course is mentioned in the points where there is room for improvement.
Some challenges were minor were solved by searching the internet and collaborating with members.

### Creative ideas and extra works:
One issue that may be considered exceptional is making it easy for the user to use the program by entering the least number of characters. For example, we can refer to the division functions instead of entering information each time the function is executed. The user only chooses the type of function so that the program, executes the function and hence divides the costs according to the user input database. Also, as extra work, a function was written that demonstrates the share of each unit in total costs by plotting.

### strong points of the code and points where the program can be improved:
One of the advantages of our say program is that variables are named in such way so that even those with a medium to low level of English literacy can understand the code. Various documentations including function definitions and multiple hashtags make the code more comprehendible.
A Point in the program that can be improved is adding an all option when accepting data in related units instead of writing individual units.

  **[⬆ back to top](#table-of-contents)**
