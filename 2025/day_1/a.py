
# Part 1
with open('input.txt', 'r') as file:
    lines = file.readlines()
    cnt = 0
    starts_at = 50
    for line in lines: 
        line = line.strip()
        step = int(line[1:])
        if line[0] == 'L': 
            starts_at = (starts_at - step) % 100
        else: 
            starts_at = (starts_at + step) % 100
        if(starts_at == 0): cnt+= 1

    print(cnt)

# Part 2
with open('input-1.txt', 'r') as file:
    lines = file.readlines()
    cnt = 0
    starts_at = 50
    for line in lines: 
        line = line.strip()
        step = int(line[1:])
        for _ in range(step):
            if line[0] == 'L':
                starts_at = (starts_at - 1) % 100
            else: 
                starts_at = (starts_at + 1) % 100 
            if starts_at == 0: 
                cnt+= 1

    print(cnt)
