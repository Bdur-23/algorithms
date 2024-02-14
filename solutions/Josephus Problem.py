#by brute force - a number kills the next one
def josephus_solver(n):
    li = [i for i in range(1,n+1)]
    while len(li)>1:
        c = 1
        for i in li:
            if i != li[-1]:
                li.pop(c)
                c += 1
            else:
                c = 0
                li.pop(c)
                c += 1
    return li[0]




#solution with binary converting
#converting a number to binary
def num_bin(s):
    binar = []
    while 1 <= s:
        if s % 2 == 0:
            binar.insert(0,0)
        elif s % 2 == 1:
            binar.insert(0,1)
        s = s//2
    return binar

#converting a binary to a number
def bin_num(l):
     t = []
     c = 1
     for x in l:
          t.append((2**(len(l)-c))*x)
          c += 1
     return sum(t)

#calculating the josephous number
def josephus(n):
        a = num_bin(n)
        for i in a:
            if i==1:
                a.remove(i)
                break
        a.append(1)
        r = bin_num(a)
        return r




#short way with finding the bigest power of 2 inside the number
def joseph(n):
    c,a = 0,n
    while 1<a:
        a //= 2
        c += 1
    return 2*(n-2**c)+1




#checking answers with multiple samples
while True:
     c = int(input("enter:" ))
     #print(num_bin(c))
     #print(bin_num(num_bin(c)),"\n")
     #print(josephus_solver(c))
     #print(josephus(c))
     print(joseph(c),"\n")









