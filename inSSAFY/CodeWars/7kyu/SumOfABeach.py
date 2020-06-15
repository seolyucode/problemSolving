# Sum of a Beach

def sum_of_a_beach(beach):
    beach = beach.lower()
    words = ["sand", "water", "fish", "sun"]
    count = 0
    for word in words:
        count += beach.count(word)
    return count