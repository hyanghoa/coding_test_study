for _ in range(int(input())):
    total_c = 0
    total_g = 0
    for _ in range(int(input())):
        c, g = map(float, input().split())
        total_c += int(c)
        total_g += c*g
    print(f"{total_c} {total_g/total_c:.1f}")