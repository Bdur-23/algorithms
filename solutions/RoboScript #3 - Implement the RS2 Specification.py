import re

def execute(code):
    dirs, curd = [(0,1), (-1,0), (0,-1), (1,0)], 0
    
    while '(' in code:
        code = re.sub(r'\(([A-Z0-9]+)\)(\d*)', lambda m: m[1]*int(m[2] if m[2] else '1'), code)
        
    path = re.findall(r'([FLR])(\d*)', code)
    
    movx, movy = [0],[0]
    for dir, dst in path:
        dst = 1 if dst == '' else int(dst)
        if dir == 'L': 
            curd = (curd + dst) % 4
        if dir == 'R': 
            curd = (curd - dst) % 4
        if dir == 'F':         
            movx.append(movx[-1] + dst * dirs[curd][0])
            movy.append(movy[-1] + dst * dirs[curd][1])
            
    mnx, mxx, mny, mxy = min(movx), max(movx), min(movy), max(movy)
            
    table = [[' ' for _ in range(mxy - mny+1)] for _ in range(mxx - mnx+1)]
    table[-mnx][-mny] = '*'
    moves = [*zip([x-mnx for x in movx], [y-mny for y in movy])]
    
    for (sx, sy), (fx, fy) in zip(moves, moves[1:]):
        for x in range(min(sx,fx), max(sx, fx) +1):
            for y in range(min(sy,fy), max(sy, fy) +1):
                table[x][y] = '*'
                
    return '\r\n'.join(''.join(row) for row in table)
