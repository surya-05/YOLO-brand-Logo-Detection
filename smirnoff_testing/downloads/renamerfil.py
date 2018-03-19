import os

initcoun=0
path='hp_laptop/'
fil=os.listdir(path)
for fils in fil:
    #os.rename(fils,str(initcoun))
    os.rename(os.path.join(path, fils), os.path.join(path, "hp"+str(initcoun)+'.jpg'))
    initcoun=initcoun+1


fil=[os.listdir(path)]
print (fil)
