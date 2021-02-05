import pandas as pd
import datetime as dt
# Data input
d = {'amount': [], 'time':[], 'category': [] , 'subcategory': [],
     'responsible unit': [], 'related unit': [],
     'div': [], 'description': []}

while True:
    amount = int(input('amount:'))
    d['amount'].append(amount)
    
    time = input('time( Example: 1399/09/21 ) : ')
    d['time'].append(dt.date(int(time[0:4]),int(time[5:7]), int(time[8:])))
    
    category = input("category: 1) receipt 2) cleaning 3) elevator 4) parking 5) repairs 6) charge 7) other [1/2/3/4/5/6/7] :")
    if category == '1':
        d['category'].append('receipt')
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
        subcategory = 'Undefind'
    d['subcategory'].append(subcategory)
    
    responsible_unit = input('responsible unit:')
    d['responsible unit'].append(responsible_unit)
    
    
    div = input('div: 1) -e 2) -r 3) -d 4) -a 5) -p [1/2/3/4/5] :')
    if div == '1':
        div = 'equal'
        d['div'].append(div)
        related_unit = 'All'
        d['related unit'].append(related_unit)
    elif div == '2':
        div = 'number'
        d['div'].append(div)
        related_unit = 'All'
        d['related unit'].append(related_unit)
    elif div == '3':
        div = 'default'
        d['div'].append(div)
        related_unit = 'All'
        d['related unit'].append(related_unit)
    elif div == '4':
        div = 'area'
        d['div'].append(div)
        related_unit = 'All'
        d['related unit'].append(related_unit)
    elif div == '5':
        div = 'parking'
        d['div'].append(div)
        related_unit = input('related Unit[All or write numbers]:')
        d['related unit'].append(related_unit)
        
    
    description = input('description:')
    d['description'].append(description)
    

    i = input('Is there anything left? A)yes B)no [A/B] :')
    if i == 'B':
        break
    
df = pd.DataFrame(d)

df.to_csv('D:/MH.Falahati/شریف/ترم اول/پایتون/جزوات کلاس/20. Final Project/Data.csv' , mode = 'a')

a = pd.read_csv('D:/MH.Falahati/شریف/ترم اول/پایتون/جزوات کلاس/20. Final Project/Data.csv')
a = a[a['amount'] != 'amount'].drop('Unnamed: 0' , axis = 1)
a.to_csv('D:/MH.Falahati/شریف/ترم اول/پایتون/جزوات کلاس/20. Final Project/Data.csv')


# function div

b = pd.read_csv('D:/MH.Falahati/شریف/ترم اول/پایتون/جزوات کلاس/20. Final Project/My CSV.csv')



def equal():
    global a
    equal = a[(a['div'] == 'equal')]['amount']
    total = equal.sum()
    b = pd.read_csv('D:/MH.Falahati/شریف/ترم اول/پایتون/جزوات کلاس/20. Final Project/My CSV.csv')
    output_equal = round((total/len(b['Vahed'])) , 2)
    b['output_equal'] = output_equal
    return(b['output_equal'])


def number():
    global a
    number = a[a['div'] == 'number']['amount']
    total = number.sum()
    b = pd.read_csv('D:/MH.Falahati/شریف/ترم اول/پایتون/جزوات کلاس/20. Final Project/My CSV.csv')
    num_number = b['People Quantity']
    output_number = total*(num_number/sum(b['People Quantity']))         
    return (output_number)


def area():
    global a
    area = a[a['div'] == 'area']['amount']
    total = area.sum()
    b = pd.read_csv('D:/MH.Falahati/شریف/ترم اول/پایتون/جزوات کلاس/20. Final Project/My CSV.csv')
    area_number = b['Metrag']
    output_area = round(total*(area_number/sum(b['Metrag'])) , 2)
    return(output_area)


def parking():
    global a
    parking = a[a['div'] == 'parking']['amount']
    total = parking.sum()
    b = pd.read_csv('D:/MH.Falahati/شریف/ترم اول/پایتون/جزوات کلاس/20. Final Project/My CSV.csv')
    parking_number = b['Parking']
    output_parking = round(total*(parking_number/sum(b['Parking'])) , 2)
    return(output_parking)




dict1 = {'related unit': [] , 'price': [] ,'time': [] , 'category':[] , 'subcategory':[] , 'BedehKar' : [] , 'BestanKar' : []}

dict1['price'].append(equal())

c = pd.read_csv('D:/MH.Falahati/شریف/ترم اول/پایتون/جزوات کلاس/20. Final Project/Sotoon.csv')
c['vahed'] = b['Vahed']
c['equal'] = equal()
c['area'] = area()
c['parking'] = parking()
c['number'] = number()


#b.to_csv('D:/MH.Falahati/شریف/ترم اول/پایتون/جزوات کلاس/20. Final Project/My CSV.csv')