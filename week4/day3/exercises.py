#1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
new_dict = dict(zip(keys, values))
print (new_dict)
#2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0
for key, value in family.items():
    if value < 3:
        print (key, "your ticket is free")
    else:
        if value < 12:
            print(key, "the price of your ticket is $10")
            total_cost = total_cost + 10
        else:
            print(key, "your ticket is $15")
            total_cost = total_cost + 15
print(total_cost)

#3
brand = {
'name': "Zara", 
'creation_date': 1975, 
'creator_name': ["Amancio", "Ortega", "Gaona"],
'type_of_clothes': ["men", "women", "children", "home"], 
'international_competitors': ["Gap", "H&M", "Benetton"], 
'number_stores': 7000, 
'major_color':{ 
    'France': 'blue', 
   'Spain': 'red', 
    'US': ['pink', 'green']
}
}
brand['number_stores'] = 2
print("zara customers are", " ".join(brand['type_of_clothes']) )
brand[' country_creation'] = "spain"

if 'international_competitors' in brand.keys():
   brand['international_competitors'].append("desigual")

del brand['creation_date']
print(brand['international_competitors'][-1])
print(brand['major_color']['US'])
print(len(brand.items()))
print(brand.keys())

more_on_zara = {
    'creation_date': 1975, 
    'number_stores': 10000
}

brand.update(more_on_zara)
print(brand['number_stores'])

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]