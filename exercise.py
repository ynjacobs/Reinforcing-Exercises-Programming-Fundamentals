venues = [
{ 'address': "123 Main Street", 'city': "Toronto", 'wheelchair_accessible': True, 'capacity': 100 },
{ 'address': "567 Centre Street", 'city': "Toronto", 'wheelchair_accessible': False, 'capacity': 400 },
{ 'address': "9B Ontario Street", 'city': "Montreal", 'wheelchair_accessible': True, 'capacity': 1000 },
{ 'address': "56 Road Avenue", 'city': "Ottawa", 'wheelchair_accessible': True, 'capacity': 650 },
{ 'address': "938 Avenue Way East", 'city': "Toronto", 'wheelchair_accessible': False, 'capacity': 90 },
{ 'address': "34 Main Street West", 'city': "London", 'wheelchair_accessible': False, 'capacity': 300 },
{ 'address': "44 Quebec Road", 'city': "Toronto", 'wheelchair_accessible': True, 'capacity': 200 },
{ 'address': "10 Spruce Avenue Ouest", 'city': "Montreal", 'wheelchair_accessible': False, 'capacity': 525 }
]

venue = venues
new_list = []
for item in venues:
 if item['wheelchair_accessible'] and item['capacity'] >= 150 and item['city'] == "Toronto":
     new_list.append(item)
print(new_list)


       

