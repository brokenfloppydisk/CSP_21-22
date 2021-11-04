list_to_sort = []

completed = False
while (not completed):
    user_input = input("Please enter a number or type END to end the list to be sorted.")
    if (user_input == "END"):
        completed = True
    else:
        list_to_sort.append(int(user_input))

for i in range(len(list_to_sort),1,-1):
    for j in range(0,i-1):
        if list_to_sort[j] > list_to_sort[j+1]:
            temp = list_to_sort[j+1]
            list_to_sort[j+1] = list_to_sort[j]
            list_to_sort[j] = temp

print(list_to_sort)