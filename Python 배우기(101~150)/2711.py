for _ in range(int(input())):
    index, string = input().split()
    string = list(string)
    string.pop(int(index)-1)
    string = "".join(string)
    print(string)