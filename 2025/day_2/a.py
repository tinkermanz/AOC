# Part 1
with open('input-1.txt', 'r') as file:
    lines = file.read()
    el = lines.split(',')
    dup_sum = 0
    for i in range(len(el)):
        first,second = str(el[i]).split('-')
        if first[0] == '0': continue
        for j in range(int(first), int(second) + 1):
            word = list(str(j))
            print(word)
            mid = len(word) //2
            word_half = word[:mid]
            word_other = word[mid:]
            if word_half == word_other: 
                dup_sum += int(str(j))
    
    print(dup_sum)
            
# Part 2


                
