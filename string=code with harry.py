#2
letter=('''Dear<|Name|>,
you are selected!
<|date|> ''')
name=input("enter your name")
date=input("rnter date")
letter=letter.replace("<|Name|>",name) 
letter=letter.replace("<|date|>",date)     
print(letter)
#3
n="navya is a good girl"
doubleSpace=n.find(" ")
print(doubleSpace)
#4
letter="dear harry,\nthis python course is nice.\n thanks!"
print(letter)