
def vowel_count():
    inp = input("Enter the word: ")
    small_inp = inp.lower()
    a = small_inp.count("a")
    e = small_inp.count("e")
    i = small_inp.count("i")
    o = small_inp.count("o")
    u = small_inp.count("u")
    print(f"the word {inp} has {a+e+i+o+u} vowels")
