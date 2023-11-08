def solution(players, callings):
    order_dict = {player: i for i, player in enumerate(players)}
    for i in callings:
        current_rank = order_dict[i]
        order_dict[i] -= 1
        order_dict[players[current_rank-1]] += 1
        players[current_rank-1], players[current_rank] = i, players[current_rank-1]
    return players