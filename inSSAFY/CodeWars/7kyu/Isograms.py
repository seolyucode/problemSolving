# Isograms

def is_isogram(string):
    if string:
        if len(string.lower()) == len(set(string.lower())):
            return True
        else:
            return False
    else:
        return True