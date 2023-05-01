for _ in range(int(input())):
    binary = list(map(int, list(bin(int(input()))[2:])))[::-1]
    answer = [idx for idx, b in enumerate(binary) if b == 1]
    print(*answer)