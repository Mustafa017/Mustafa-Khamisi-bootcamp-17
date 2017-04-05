def find_max_min(n):
    for i in range(len(n)):
        if not isinstance(n,list):
            raise ValueError("Input should be a list")
        else:
            result = []
            smallest = min(n)
            largest = max(n)
            if smallest == largest:
                result.append(n[i])
                return result
            else:
                result.extend([smallest, largest])
                return result