"""
Encode:
    step1 reverse string
    step2 add original string in even indexes
    step3 convert the odd parts to unicode and even to binary
    step3 return the final string

Decodde
"""
import sys
def accept():
    inn=input("Pls choose:\n1.Encode(E)\n2.Decode(D)\n\nYour choice:")
    opt=inn.lower()
    if opt=='e':
        s=input("Enter a String:")
    elif opt=='d':
        s=(input("Enter the cipher string:"))
    else:
        print("Invalid choice")
        sys.exit(0)
    return s,opt

def encode(s):
        rst=list(s[::-1])  #[n,i,v,a,g]
        st=list(s)  #[g,a,v,i,n]
        ns=[]
        for i in range(0,len(rst)): #[G,a,v,i,n] ---#[n,g,i,a,v,v,a,i,g,n]
            if i%2!=0:
                ns.append(str(ord(rst[i])))
            else:
                ns.append(format(ord(st[i]),'08b'))
        fw="".join(ns)
        return fw

def decode(s):
    l=s.strip().split()   #[110, 103, 105, 97, 118, 118, 97, 105, 103, 110]
    ns=[chr(int(x)) for x in l]
    rst=[]
    st=[]
    for i in range(0,len(ns)-1,2):
        rst.append(ns[i])
        st.append(ns[i+1])
    fw="".join(st)
    return fw

def choose(b):
    if b=='e':
        print(encode(a))
    if b=="d":
        print(decode(a))
a,b=accept()
choose(b)
