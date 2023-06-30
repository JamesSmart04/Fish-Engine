


def convert_pos(pos:list) -> list:
    """takes a human position and converts to inhuman position"""
    alpharange = "abcdefgh"
    alpha_dict = {}
    for i in range(len(alpharange)):
        alpha_dict[alpharange[i]] = i
    
    if pos[0] in alpha_dict:
        return [alpha_dict[pos[0]],pos[1]-1]

    else:
        print("please provide a valid poosition")
        return False