def solution(bandage, health, attacks):
    max_health = health
    t,x,y = bandage
    attacks_key = {s:damage for s,damage in attacks}
    last_attack_sec = 0
    for s, damage in attacks:
        time_interval = (s-last_attack_sec-1)
        health += x * time_interval
        if(time_interval >= t):
            health += y * (time_interval // t)
        if health >= max_health:
            health = max_health
        last_attack_sec = s
        health -= damage
        if (health <= 0):
            return -1
        
    return health