from itertools import product
from functools import reduce

def expand(expr):
    #print(expr)
    main = expr[1:expr.find(")")]
    if expr[-1] in "0":return "1"
    elif expr[-1] in "1":return main
    
    main = main if main[0] in "-" else "+" + main
    main = main if main[1] in "0123456789" else main[0]+"1"+main[1::]
    pl = [c for c,i in enumerate(main) if i in "+-" and c!=0]
    #print(main, pl)

    mn = [i for i in main] 
    for i in pl:
        mn.insert(i," ")
    #tk = ["".join(mn).split(" ") for _ in range(int(expr[-1]))]
    #print(tk)
    
    #pr = list(product([i for i in range(len(pl)+1)],repeat=int(expr[-1])))
    #print(pr)
    
    fin = [sorted(i) for i in [[["".join(mn).split(" ") for _ in range(int(expr[-1]))][i][j] for i,j in enumerate(x)] for x in list(product([i for i in range(len(pl)+1)],repeat=int(expr[-1])))]]
    #print(fin)

    types,count = [],[]
    for c,i in enumerate(fin):
        if i not in types:
            types.append(i)
            count.append(1)
        elif i in types:
            count[types.index(i)] += 1
    #for i in range(len(count)):
        #print(types[i],":",count[i])
    
    ktr = main[2] if main[2] not in "0123456789" else main[3]
    for i in range(len(count)):
        types[i].append(str(count[i]))
        for c,x in enumerate(types[i]):
            if ktr in x:
                types[i][c] = x[0:-1]
            types[i][c] = int(types[i][c])
    #print(types)
    
    answer = ""
    for i in range(len(types)):
        print(types[i])
        kat = reduce(lambda a, b: a * b,types[i])
        print(kat)
        if kat == 1 and i != len(types)-1:
            kat = ""
        elif kat == -1 and i != len(types)-1:
            kat = "-"
        elif kat < 0 or kat > 0 and i == 0:
            kat = str(kat)
        elif kat > 0 and i != 0:
            kat = f"+{kat}"
        
        if i == len(types)-1:
            answer += str(kat)
        elif i == len(types)-2:
            answer += f"{kat}{ktr}"
        else:
            answer += f"{kat}{ktr}^{int(expr[-1])-i}"

    #print(answer)
    return answer
