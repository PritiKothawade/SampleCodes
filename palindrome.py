def palPythonic(str):
    if str == str[::-1]:
        print("Yay")
    else:
        print("Nay")

if __name__ == "__main__":
    palPythonic(list("radar"))
