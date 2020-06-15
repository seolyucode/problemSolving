# Mexican Wave

def wave(str):
    waved = []
    for i, char in enumerate(str):
        waved.append(str[:i] + str[i].upper() + str[i+1:])
        for j in waved:
            if j.islower() == True:
                waved.remove(j)
    return waved