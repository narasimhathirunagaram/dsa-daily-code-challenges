students = [ 
        { 'name': 'Amit', 'semesters': [ {'Math': 88, 'Science': 91, 'English': 85}, {'Math': 90, 'Science': 92, 'English': 84} ] }, 
        { 'name': 'Pooja', 'semesters': [ {'Math': 79, 'Science': 95, 'English': 88}, {'Math': 82, 'Science': 81, 'English': 85} ] }, 
        { 'name': 'Ravi', 'semesters': [ {'Math': 87, 'Science': 88, 'English': 89}, {'Math': 91, 'Science': 90, 'English': 93} ] } 
    ]

# l = [(i['name'],i['semesters']) for i in students]
# out_d = {}
# for x in l:
#     # print(x[0],x[1])
#     s = 0
#     less_l = []
#     for y in x[1]:
#         for k,v in y.items():
#             if v>80:
#                 s += v
#             else:
#                 # print(x,' scored less')
#                 less_l.append(x)
#                 break
#     if x not in less_l:
#         out_d[x[0]] = s
# print(out_d)    



# Approach2

out_d = {}

for student in students:
    total_score = 0
    for semester in student['semesters']:
        if any(score <= 80 for score in semester.values()):
            break
        total_score += sum(semester.values())
    else:
        out_d[student['name']] = total_score

print(out_d)

# Approach 3
# out_d = {
#     student["name"]: sum(sum(sem.values()) for sem in student["semesters"])
#     for student in students
#     if all(all(score > 80 for score in sem.values()) for sem in student["semesters"])
# }

# print(out_d)