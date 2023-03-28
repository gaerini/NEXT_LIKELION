# 9093
sentence_list = input().split()

for i in range(len(sentence_list)):
    if len(sentence_list[i]) > 1:
        temp = list(sentence_list[i])

        temp.reverse()
        
        sentence_list[i] = "".join(temp)
    
print(" ".join(sentence_list))