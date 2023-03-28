# 1259
number = input()
number_list = []
ref = []
for i in range(len(number)):
    number_list.append(number[i])
    #1 [1]
    #2 [1, 2]


ref = number_list
number_list.reverse()

if number_list == ref:
    print('Yes')
else:
    print('No')
