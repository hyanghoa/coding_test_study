a, b = map(int, input().split())
sequence = []
i = 1
while len(sequence) < b:
    sequence.extend([i]*i)
    i += 1
    
print(sum(sequence[a-1:b]))