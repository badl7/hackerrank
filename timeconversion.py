def timeconversion(s):
    a = s[0:2]
    if s[8:] == "PM":
        if int(a) != 12:
            news = int(a) + 12
            print(str(news) + s[2:8])
        else:
            print(s[:8])
    elif s[8:] == "AM":
        if int(a) == 12:
            print('00' + s[2:8])
        else:
            print(s[:8])
    


s = "12:01:00AM"
print(s[8:])
timeconversion(s)
