def rev(str):
    for i in range(0,len(str)//2):
        str[i],str[len(str)-i-1] = str[len(str)-i-1], str[i]
    print(''.join(str))

def revPythonic(str):
    print(''.join(str[::-1]))

if __name__ == "__main__":
    rev(list("12345"))
    revPythonic("12345")
