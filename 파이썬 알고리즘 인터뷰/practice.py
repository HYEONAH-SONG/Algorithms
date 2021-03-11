sentence = "aaabbbcccffcdd"

l=""
count =[]
score = 0
for alpha in sentence:

    #print(count,score)
    if count and count[-1]!=alpha:
        l+=count[-1]
        l+=str(score)
        count=[]
        score=0
        count.append(alpha)
        score+=1
    else:
        count.append(alpha)
        score += 1
if count :
    l+=count[-1]
    l+=str(score)
print(l)