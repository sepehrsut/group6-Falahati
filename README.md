# group6-اسقف Project

## Table of Contents
  1. [Introduction](#introduction)
  2. [Append Function](#append-function)
  3. [Division Function](#division-function)
     1. [E: Equal](#equal)
     2. [R: Number](#number)
     3. [A: Area](#area)
     4. [P: Parking](#parking)
     5. [D: Default](#default)
  4. [Report Faunction](#report-function)
  
## Introduction
In order to adjust the building expenses, each building manager must calculate all the small expenses and how to divide each of them, and also report to the building occupants at the end of the bill, charge, financial balance, etc. All of this is time consuming for one person and organizing the whole paper and work invoice and it is very difficult to handle. Therefore, in the age of technology, various programs and software have been written to facilitate the work and organize these costs, one of which is our project (اسقف team), which helps the building manager to eliminate all additional building costs. And give only general expenses to the program.Our program consists of three parts:1.Input(append fanc) 2.div(division func) 3.report func
In the input section(append fanc), the building manager only needs to record the total costs of the building and in the other two sections, the costs of each unit in the ways specified by the manager, such as the aggregate cost chart, financial balance and invoices of the units,and etc. Shows.

## **Append Function**

The append function is the part where the building manager must record the total cost to the console. In this section, it records all the data written by the administrator in the d dictionary.The dictionary d keys contain our columns and its values are the building manager data recorded in the console

    def append(root_out: str):
      """ This function accepts inputs from the user. """
    
      import pandas as pd
      import datetime as dt
      d = {'amount': [], 'time':[], 'category': [] , 'subcategory': [],
     'responsible unit': [], 'related unit': [[]],
     'div': [], 'description': []}
     
These dictionary keys include the amount or the same cost, when this cost is paid, the ctegory and subcategory of this cost, the head of the department who is usually the building manager, the unit related to that cost and how to divide it and describe it.
   
    amount = int(input('amount:'))
    d['amount'].append(amount)
    
    time = input('time( Example: 1399/09/21 ) : ')
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
        
In the div section, which is the most important part of our input function, the building manager, after entering the relevant option, causes the unit function to calculate the costs of each unit.
    
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
    
At the end of the input, after receiving this information from the building manager, we ask the manager if there is still other data that needs to be recorded that if he clicks yes, all these input processes will be repeated until the last question is answered. If it is not negative, it can record the input data in the d dictionary, and after the end of the input process, all the dictionary data will enter the dataframe space.

    i = input('Is there anything left? A)yes B)no [A/B] :')
    if i == 'B':
        pd.DataFrame(d).to_csv(root_out, mode = 'a', header= False, index = False)
        return
    else:
        pd.DataFrame(d).to_csv(root_out, mode = 'a', header = False, index = False)
        append()
**[⬆ back to top](#table-of-contents)**
