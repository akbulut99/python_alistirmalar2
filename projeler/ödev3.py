bas_harf = ""
with open("test.txt","r",encoding="utf-8") as file:
   

  for i in file:
    bas_harf += i[0]

print(bas_harf)