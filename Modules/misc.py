def convert_pos(pos:list) -> list:
    """takes a human position and converts to inhuman position"""
    alpharange = "abcdefgh"
    alpha_dict = {}
    for i in range(len(alpharange)):
        alpha_dict[alpharange[i]] = i
    
    if pos[0] in alpha_dict and pos[1] >= 1 and pos[1] < 8:
        return [alpha_dict[pos[0]],8-pos[1]]

    else:
        return pos