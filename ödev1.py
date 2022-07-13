s =  "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
frekans = dict()
for i in s:
    if i in frekans:
        frekans[i] += 1
    else:
        frekans[i] = 1

for i,j in frekans.items():
    print("i:",i,"j:",j)
    print("------")