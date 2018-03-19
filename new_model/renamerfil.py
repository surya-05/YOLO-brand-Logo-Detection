import os

initcoun=0
path='annotation/'
fil=os.listdir(path)
for fils in fil:
    #os.rename(fils,str(initcoun))
    print(fils)
    base=os.path.splitext(fils)[0]
    os.rename(path+""+fils,base+".xml")

fil=[os.listdir(path)]
print (initcoun)
