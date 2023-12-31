

def convert_pos(pos:list) -> list:
    """takes a human position and converts to inhuman position"""
    alpharange = "abcdefgh"
    alpha_dict = {}
    for i in range(len(alpharange)):
        alpha_dict[alpharange[i]] = i
    row = int(pos[1])
    column = pos[0]
    if column in alpha_dict and row >= 1 and row <= 8:
        return [alpha_dict[column],8-row]

    else:
        return pos

def convert_pos_to_string(pos:list) -> str:
    if not pos:
        return ""
    alpharange = "abcdefgh"
    num_dict = {}
    row = pos[1]
    column = pos[0]
    for i in range(len(alpharange)):
        num_dict[i] = alpharange[i]

    if len(pos) == 2:
        return num_dict[column]+str(8-row)
    elif len(pos) == 3:
        promo_list = ['q','n','b','r'] if pos[1] == 7 else ['Q','N','B','R']
        return num_dict[column]+str(8-row)+promo_list[pos[2]]
    