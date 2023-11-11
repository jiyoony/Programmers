def move(current,park,direction,distance):
    initial_y, initial_x = current
    y,x = current
    for i in range(distance):
        mov = [a+b for a,b in zip(current, direction)]
        y,x = mov
        try:
            if ((park[y][x] != 'X') and (0 <= x < len(park[0])) and (0<= y <len(park))):
                current = [y,x]
            else:
                return [initial_y, initial_x]
        except IndexError:
            return [initial_y, initial_x]
    return [y,x]
    
def find_start(park):
    for y_index,y in enumerate(park):
        if 'S' in y:
            return [y_index, y.index("S")]

def solution(park, routes):
    parkList = []
    for i in park:
        parkList.append(list(i))
    direction = {"E": [0,1], "W": [0,-1], "S": [1,0], "N": [-1,0]}
    current = find_start(parkList)
    for route in routes:
        mov_dir = direction[route[0]]
        distance = int(route[2])
        current = move(current, park, mov_dir, distance)
    
    return current