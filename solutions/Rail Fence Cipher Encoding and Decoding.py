def encode_rail_fence_cipher(string, n):
    tk,main,n = [[] for i in range(n)],[i for i in string],n-1
    for i in range(len(main)):
        tk[i%n if i//n%2==0 else n-i%n].append(main[i])
    return "".join([i for x in tk for i in x])
    
def decode_rail_fence_cipher(string, n):
    tk,main,n = [[] for i in range(n)],[i for i in string],n-1
    for i in range(len(main)):
        tk[i%n if i//n%2==0 else n-i%n].append(i)
    return "".join([k for _,k in sorted(zip([i for x in tk for i in x],main))])
