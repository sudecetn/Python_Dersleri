import pandas as pd

seri_1 = pd.Series([1,2,3,4,5])
print(seri_1)

print("-"*50)

print(seri_1.index)

seri_2 = pd.Series([175,160,180,182,168],index=['Ahmet','Ali','Ayşe',"Mehmet","Fatma",])

print(seri_2)

seri_2.index = ["Sıra_1","Sıra_2","Sıra_3","Sıra_4","Sıra,_5",]
print(seri_2)




