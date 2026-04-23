# secret code Language 
import random
import string
st=input("Enter your message:")
words=st.split(" ")
coding=input("1 for coding or 0 for decoding")
coding= True if (coding == "1") else False
if coding:
    nwords=[]
    for word in words:
        if len(word)>=3:
            length=3
            characters = string.ascii_letters + string.digits
            r1=''.join(random.choices(characters, k=length))
            r2=''.join(random.choices(characters, k=length))
            stnew= r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords=[]
    for word in words:
        if len(word)>=3:
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))