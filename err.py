def make_list(number):
    names=[]
    for item in range(number):
        names.append(input("Enter your name with a capital letter."))
    return names

number=int(input("kaç tane giriş"))
names=make_list(number)
for name in names:
    if name[0]=="A":
        print("Name",name,"start with A")
