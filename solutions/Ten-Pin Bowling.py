def bowling_score(frmes):
    tbl = [10 if i=="X" else int(i) if i not in ["/"," "] else "/" for i in [i for x in frmes for i in x] if i!=" "]
    last = [tbl[i] for i in [-x for x in range(1,len(frmes.split(" ")[-1])+1)]]
    c = 10+last[0] if "/" in last else sum(last)
    for i in range(len(tbl)-len(frmes.split(" ")[-1])):
        c += tbl[i+1]+10-tbl[i-1] if tbl[i]=="/" else 20 if tbl[i]==10 and tbl[i+2]=="/" else tbl[i+1]+tbl[i+2]+10 if tbl[i]==10 else tbl[i]
    return c




"""
def bowling_score(frmes):
    tbl = [10 if i=="X" else int(i) if i not in ["/"," "] else "/" for i in [i for x in frmes for i in x] if i!=" "]
    kr = len(frmes.split(" ")[-1])
    last = [tbl[i] for i in [-x for x in range(1,kr+1)]]
    c = 10+last[0] if "/" in last else sum(last)
    for i in range(len(tbl)-kr):
        print(i,tbl[i])
        if tbl[i] == "/":
            c += tbl[i+1]+10-tbl[i-1]
        elif tbl[i] == 10:
            if tbl[i+2] == "/":
                c += 20
            else:
                c += tbl[i+1]+tbl[i+2]+10
        else:
            c += tbl[i]
    return c
"""
