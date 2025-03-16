def sort_by_tuple_sum(lst: list[tuple])->list[tuple]:
    sorted_list = sorted(lst,key=lambda a:a[0]+a[1])
    return sorted_list

l1 = [(3,1),(2,2),(5,-1),(0,0)]
l2 = [(7,3),(1,2),(4,5),(0,1)]
l3 = [(8,-1),(1,1),(2,0),(5,5),(3,2)]
for l in (l1,l2,l3):
    print(sort_by_tuple_sum(l))