# Part 1
with open('input.txt', 'r') as file:
    lines = file.read()
    el = lines.split(',')
    dup_sum, dup_sum_2 = 0, 0
    for i in range(len(el)):
        first,second = str(el[i]).split('-')
        if first[0] == '0': continue
        for j in range(int(first), int(second) + 1):
            word = list(str(j))
            mid = len(word) //2
            word_half = word[:mid]
            word_other = word[mid:]
            if word_half == word_other: 
                dup_sum += int(str(j))
                dup_sum_2 += int(str(j))
            else: 
                repeat = 1
                while repeat * 2 < len(word):
                    repeat_part = str(j)[:repeat]
                    repated_str = repeat_part * (len(word)// repeat)
                    if repated_str == str(j):
                        dup_sum_2+= j
                    repeat += 1
            
    print(dup_sum)
    print(dup_sum_2)
            


                
