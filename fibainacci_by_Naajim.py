#fibinacci series
num=int(input('Please Enter the required range in N:'))
y=0
z=1
count=0
if(num==1):
        print(y)
else :
    while count<num:
        print(y)
        nth=y+z
        y=z
        z=nth
        count +=1
   
