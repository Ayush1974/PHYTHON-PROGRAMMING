str1="hello there  i am using whatapp!"
i=0
count=0
while i<len (str1) :
        if str1[i]==' ' and str1[i+1]==' ':
            count+=1
            i=i+1
        else:
            count+=0
            i=i+1 

print("The double spaces are:",count)