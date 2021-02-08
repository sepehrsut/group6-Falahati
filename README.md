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
In the input section(append fanc), the building manager only needs to record the total costs of the building and in the other two sections, the costs of each unit in the ways specified by the manager, such as the aggregate cost chart, financial balance and invoices of the units, etc. Shows.

## Append Function
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
