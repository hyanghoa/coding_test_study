def get_div(n):
    a = 1
    div = []
    while a < n:
        if n % a == 0:
            div.append(a)
        a += 1
    return div
    
while True:
    n = int(input())
    if n == -1:
        break
    div = get_div(n)
    if n == sum(div):
        print(f"{n} = {' + '.join(map(str, div))}")
    else:
        print(f"{n} is NOT perfect.")