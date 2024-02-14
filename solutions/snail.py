def snail(nmap):
    final = []
    def right():
        for i in nmap[0]: final.append(i)
        del nmap[0]   
    def left():
        for i in nmap[-1][::-1]: final.append(i)
        del nmap[-1]
    def down():
        for i in range(len(nmap)):final.append(nmap[i][-1]);nmap[i].pop(-1)   
    def up():
        for i in range(len(nmap)-1,-1,-1):final.append(nmap[i][0]);nmap[i].pop(0)       
    directions = [right,down,left,up] 
    for i in range(2*(len(nmap))-1):
        directions[i%4]()     
    return final





def snail3(array):
    ret = []
    if array and array[0]:
        size = len(array)
        for n in xrange((size + 1) // 2):
            for x in xrange(n, size - n):
                ret.append(array[n][x])
            for y in xrange(1 + n, size - n):
                ret.append(array[y][-1 - n])
            for x in xrange(2 + n, size - n + 1):
                ret.append(array[-1 - n][-x])
            for y in xrange(2 + n, size - n):
                ret.append(array[-y][n])
    return ret






def snail4(array):
  if array:
    # force to list because zip returns a list of tuples
    top_row = list(array[0])
    # rotate the array by switching remaining rows & columns with zip
    # the * expands the remaining rows so they can be matched by column
    rotated_array = zip(*array[1:])
    # then reverse rows to make the formerly last column the next top row
    rotated_array = rotated_array[::-1]
    return top_row + snail(rotated_array)
  else:
    return []





def snail5(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out






def snail6(array):
    next_dir = {"right": "down", "down":"left", "left":"up", "up":"right"}
    dir = "right"
    snail = []
    while array:
        if dir == "right":
            snail.extend(array.pop(0))
        elif dir == "down":
            snail.extend([x.pop(-1) for x in array])
        elif dir == "left":
            snail.extend(list(reversed(array.pop(-1))))
        elif dir == "up":
            snail.extend([x.pop(0) for x in reversed(array)])    
        dir = next_dir[dir]
    return snail 








def snail7(array):
    res = []
    while len(array) > 1:
        res = res + array.pop(0)
        res = res + [row.pop(-1) for row in array]
        res = res + list(reversed(array.pop(-1)))
        res = res + [row.pop(0) for row in array[::-1]]
    return res if not array else res + array[0]





snail = lambda a: list(a[0]) + snail([*zip(*a[1:])][::-1]) if a else []





def snail8(array):
  return array[0] + snail(list(map(list, [*zip(*array[1::])][::-1]))) if array else []





def trans(array):
    #Do an inverse transpose (i.e. rotate left by 90 degrees
    return [[row[-i-1] for row in array] for i in range(len(array[0]))] if len(array)>0 else array

def snail9(array):
    output=[]
    
    while len(array)>0:

        #Add the 1st row of the array
        output+=array[0]
        #Chop off the 1st row and transpose
        array=trans(array[1:])
        
    return output






def _snail(array):
    n = len(array)
    for a in range(0, (n + 1) // 2):
        b = n - 1 - a
        for j in range(a, b + 1):
            yield array[a][j]
        for i in range(a + 1, b + 1):
            yield array[i][b]
        for j in range(b - 1, a - 1, -1):
            yield array[b][j]
        for i in range(b - 1, a, -1):
            yield array[i][a]

def snail10(array):
    return list(_snail(array)) if array and array[0] else []






def snail11(array):
    #base case for recursion with n odd
    if len(array)==1: return array[0]
    #base case for recursion with n even
    if len(array)==2: return array[0]+array[1][::-1]
    res=[] #accumulator variable for my result
    #I go on "shaving" the array and taking what I need as a result
    #getting the first row
    res+=array.pop(0)
    #getting the last element of every remaining row but the last
    for i in range(len(array)-1):
        res.append(array[i].pop(-1))
    #getting the last one - reversed
    res+=array.pop(-1)[::-1]
    #and getting the first element of the remaining rows in reverse order
    for i in range(-1,-len(array),-1):
        res.append(array[i].pop(0))
    #calling recursively the function with a smaller array
    return res+snail(array)
    #usually I avoid recursive solutions, but I decided to try my hand
    #in a while with them. I hope you enjoyed reading my code :)




def snail12(snail_map):
    if snail_map:
        top_row = list(snail_map.pop(0))
        rotated_map = list(zip(*[row[::-1] for row in snail_map]))
        return top_row + snail(rotated_map)
    else:
        return []














