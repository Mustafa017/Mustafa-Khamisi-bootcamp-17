def find_missing(list_1,list_2):
    if len(list_1) == len(list_2):
        return 0
    else:
        if len(list_1) > len(list_2):
            for x in list_1:
                if x in list_2:
                    continue
                else:
                    return x
        else:
            for y in list_2:
                if y in list_1:
                    continue
                else:
                    return y

