def get_count(sentence):
    vowels = ["a", "e" , "i" , "o","u"]
    count = 0
    for letter in sentence:
        if letter in vowels:
            count += 1
    return count  