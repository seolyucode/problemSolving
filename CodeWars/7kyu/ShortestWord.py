# Shortest Word

def find_short(s):
    word_lst = s.split()
    return len(min(word_lst, key=len))