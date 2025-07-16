"""
Encode:
    step1 reverse string
    step2 add original string in even indexes
    step3 convert the final string to unicode
    step3 return the final string

"""
def accept():
    inn=input("Pls choose:\n1.Decode(D)\n2.Encode(E)\n")
    opt=inn.lower()
    if opt=='e':
        s=input("Enter a String:")
    if opt=='d':
        s=(input("Enter a String:"))
    return s,opt

def encode(s):
        rst=list(s[::-1])  #[n,i,v,a,g]
        st=list(s)  #[g,a,v,i,n]
        ns=[]
        for i in range(0,len(rst)): #[G,a,v,i,n] ---#[n,g,i,a,v,v,a,i,g,n]
            ns.append(ord(rst[i]))
            ns.append(ord(st[i]))
        fw=ns
        return fw
                 

def decode(s):
    s = s.replace(',', ' ')  # ✅ replace commas with spaces
    l = s.strip().split()
    decoded_chars = []
    for i in range(1, len(l), 2):  # Only pick odd indices = original string
        decoded_chars.append(chr(int(l[i])))
    return ''.join(decoded_chars)

    

def choose(b):
    if b=='e':
        print(encode(a))
    if b=="d":
        print(decode(a))


a,b=accept()
choose(b)
