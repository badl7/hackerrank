n= int(input("kaç kişi takım"))
players ={}
for i in range(n):
    name= input("name")
    size=input("size")
    players[name]=size
    

name=input("isim gir")
if name in players:
    print(players[name])
else:
    print("yok")
