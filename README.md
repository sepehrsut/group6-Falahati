# group6 - اسقف Project

## Group Member
  1. [MohammadHosein Falahati](#mohammadHosein-falahati) : Header/coder
  2. [Sepehr Harirchian](#sepehr-harirchian) : coder
  3. [Amirhosein GhaziMoradi](#amirhosein-ghazimoradi) : coder 
  4. [AhmadReza AliHoseini](#ahmadreza-alihoseini) : coder
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
  5. [Conculusion](#conculusion)
  
## Introduction
In order to adjust the building expenses, each building manager must calculate all the minor expenses and figure out how to divide each of them, and also report to the occupants at the end. All of this is time consuming for one person and organizing the whole paper and work invoice is very difficult to handle. Therefore, in the age of technology, various programs and softwares have been written to facilitate the work and organize these costs, one of which is our project (اسقف team), which helps the building manager to eliminate all additional building costs.Our program consists of three parts: 1.Input(append func) 2.div(division func) 3.report func
In the input section(append func), the building manager only needs to give the total costs of the building and in the other two sections, the costs of each unit in the ways specified by the manager, such as the aggregate cost chart, financial balance and invoices of the units,and etc. is demonstrated.

## **Append Function**

The append function is the part where the building manager must give the information such as total cost, related unit and etc. to the console. the given information, is recorded in a dictionary.The dictionary "d" keys contain our columns and its values are the building manager data recorded in the console

    def append(root_out: str):
      """ This function accepts inputs from the user. """
    
      import pandas as pd
      import datetime as dt
      d = {'amount': [], 'time':[], 'category': [] , 'subcategory': [],
     'responsible unit': [], 'related unit': [[]],
     'div': [], 'description': []}
     
These dictionary keys include the amount or the same cost, the time of the transaction, the category and subcategory of this cost, the head of the department who is usually the building manager, the unit related to that cost and how to divide it and describe it.
   
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
