def words(n):
    result = {}
    if isinstance(n,dict):
        for key,value in result.items():
            return key, value
    else:
        for x in n.split():
            if x not in result:
                result[x] = 1
            else:
                result[x] += 1
        return result




