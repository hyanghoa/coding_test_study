people_list = [0]
for _ in range(10):
    out_people, in_people = map(int, input().split())
    people_list.append(people_list[-1] + in_people - out_people)
print(max(people_list))