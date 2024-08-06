#Task-1 07/11/2023
def details_manadatory(params, manadatory, user_input):
    if sorted(manadatory) == sorted(user_input) :
        
        return 'Manadatory items were given'
    else:

        s1 = list((set(manadatory) - set(user_input)))
        s2 = " ".join(s1)
        diff = []
        for item in user_input:
            if item not in manadatory:
                diff.append(item)
        
        extra = []
        for each in diff:
            if each not in params:
                extra.append(each)

        dif = " ".join(extra)
        if len(extra) == 0:
            return f'{s2} manadatory'
        else:
            return f'{dif} extra given \n{s2} manadatory'

params = ["name", "age", "aadhar", "phone"]
manadatory = ["name", "age"]
user_input = input("Enter user input separtated by space:- ").split()
#print(user_input)
get = details_manadatory(params, manadatory, user_input)
print(get)