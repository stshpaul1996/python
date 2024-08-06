from copy import deepcopy,copy

# def mul(p1,p2):
#     return p1*p2


# mul(10,20)
# print(id(mul), type(mul))


# def fun(x,y):
#     print(x+y)
# res = fun
# print(res)
# r1 = res(10,20)
# r2 = fun(20,40)
# print(r1,r2)    



# def inc(y):
#     y += [1]
# a = [5,7] 
# inc(a)
# print(a)


# ls = 45
# b = ls
# ls = 25
# print(b)
# ll = [[1,2,3], 4,5]
# l8 = ll
# l8[2] = 4
# print(ll)

# ds = [1, 4,5]
# v = ds.copy()
# v[0] = 0
# print(ds)
# print(v)

# ds = [1, 4,5]
# v = deepcopy(ds)
# v[0] = 0
# print(ds)
# print(v)


# ss = [[1000,2000,3000], 4000,5000]
# vv = copy(ss)
# print(id(ss[1]))
# print(id(vv[1]))
# ss[1] = 9000
# print(id(ss[1]))
# print(ss[1])
# print(id(vv[1]))
# print(vv[1])
# ss.append(7000)
# print(ss)
# print(vv)



# Python-Task-2
x = [2000, [6000, 7000]]
a = [[[3000,5000,7000], 4000, x], 1000, 2000]
b = a[:]
d = deepcopy(a)
print(id(a[0][0][0]))
print(id(d[0][0][0]))
a[1] = 6000
print(id(a[1]))
print(a[1])
print(d[1])
print()
print(id(d[1]))
a[0][0] = 7000
print(id(a[0][0]))
print(id(d[0][0]))
x[1].append(8000)
print(id(x[1][-1]))
print(id(a[0][2][1][-1]))
print(id(d[0][2][1][-1]))
print((x[1][-1]))
print((a[0][2][1][-1]))
print((d[0][2][1][-1]))
print(id(a[1]))
print(id(b[1]))
print(id(d[1]))



class Emp:
    def __init__(self,name,empid):
        self.name=name
        self.empid=empid
    def get(self):
        return self.name, self.empid
jay = Emp("Jayaram", 1234)
print(type(Emp))
print(type(jay))