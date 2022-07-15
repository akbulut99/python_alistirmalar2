
with open("mail.txt","r",encoding="utf-8") as file:
    for i in file:
        i = i[:-1]
        if i.endswith(".com") and i.find("@") != -1:
         print(i)