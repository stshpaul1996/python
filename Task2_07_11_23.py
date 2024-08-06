l = "apple,orange,apple,mango,grapes,apple,grapes,apple,banana"
list_l = l.split(",")
length = list_l[::]
count = list_l.count('apple')
c = 0
res = []
for item in list_l:
    if item == 'apple':
        c += 1
        if c > count-2:
            res.append(item.upper())
        else:
            res.append(item)
    else:
        res.append(item)


for i in res:
    if i == 'apple':
        res.remove('apple')
print(res)        
                           





     




     

 


    

     
