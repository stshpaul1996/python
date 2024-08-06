#With neccessay or without need of decorator when we wants
def outer(f):
    def inner(ip):
        if ip:
            a = f()
            a.sort()
            return a
        else:
            return f()
    return inner

@outer
def main(op=0):
    return [3,8,9,1,2]

print(main([1,2]))
print(main(0))


#Print large value with try and except
a,b,c = 10,20,5

#print flat list
l = [3,[1,2],[10,20,[30,40,50,[70,80],90],60],100]
res = []
def flat(l):
    for i in l:
        if isinstance(i,int):
            res.append(i)
        else:
            flat(i)
flat(l)
print(res)


#Coding question
dic = {"name": "vinay","age":25,"salary":250000}
dic2 = {"name": "vinay","age":30,"salary":250000,"ph":8545845153}

output = {"name": "vinay","age":25,"salary":250000,"ph":8545845153}
for i,j in dic2.items():
    if i in dic:
        pass
    else:
        dic[i] = j

print(dic)

# one drive multiple folders, each folder- multiple files only print .pdf files only
import os
import glob

def print_pdf_files(folder): 
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".py"):
                print(os.path.join(root, file))

folder_path = "C:/Users/stshp/OneDrive/Desktop/Python"

print_pdf_files(folder_path)



#Coding question
dic = {"name": "vinay","age":25,"salary":250000}
dic2 = {"name": "vinay","age":30,"salary":250000,"ph":8545845153}

output = {"name": "ajay","age":25,"salary":100000,"ph":8545845153}
for i,j in dic2.items():
    if i in dic:
        if dic2[i] > dic[i]:
            dic[i] = j
        else:
            dic[i] = dic2[i]

    else:
        dic[i] = j

print(dic)


#Find all possible palindromes
s = "ghffhffadabbbbadahgt"
for i in range(len(s)):
    for j in range(i,len(s)+1):
        if s[i:j] == s[i:j][::-1]:
            print(s[i:j], end=" ")
   
        
