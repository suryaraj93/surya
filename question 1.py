text=input("enter text:")
x=set()
res=""
for word in text:
    # print(word)
    if word not in x:
        x.add(word)
        #print(x)
        res=res+str(text.count(word))+word
print("The result is: "+res)