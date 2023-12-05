def solution(wallpaper):    
    lux,rdx,luy,rdy = len(wallpaper), -1, len(wallpaper[0]), -1
    
    for x, wall in enumerate(wallpaper):
        if '#' in wall: 
            if x <= lux:
                lux = x
            if wall.find('#') <= luy:
                luy = wall.find('#')
            if x >= rdx:
                rdx = x+1
            if wall.rfind('#') >= rdy:
                rdy = wall.rfind('#')+1
    return [lux,luy,rdx,rdy]