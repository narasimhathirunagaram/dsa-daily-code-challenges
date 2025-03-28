cities = [ 
    { 'name': 'Mumbai', 'areas': { 'Andheri': [32, 33, 31, 30, 29, 34, 35], 'Bandra': [31, 32, 30, 30, 31, 33, 34], } }, 
    { 'name': 'Delhi', 'areas': { 'Rohini': [28, 29, 27, 30, 31, 32, 29], 'Saket': [33, 35, 36, 34, 33, 32, 31], } }, 
    { 'name': 'Chennai', 'areas': { 'T Nagar': [34, 35, 36, 37, 34, 35, 33], 'Velachery': [32, 31, 33, 34, 32, 30, 31] } } 
    ]

# for city in cities:
#     flag = False
#     for i in city['areas'].values():
#         avg = sum(i)/len(i)
#         # print("Average", avg)
#         if avg>30:
#             flag = True
#         else:
#             flag = False
#             break
#     if flag:
#         print(city['name'])
    # print('City name:', city)

for city in cities:
    if all(sum(i)/len(i) > 30 for i in city['areas'].values()):
        print(city['name'])
