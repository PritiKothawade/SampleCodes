def anagramCheck(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 == s2:
        print("Yay")
    else:
        print("Nay")


if __name__ == "__main__":
    anagramCheck("brainy", "binary")