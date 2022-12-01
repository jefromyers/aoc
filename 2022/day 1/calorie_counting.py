from collections import defaultdict 

if __name__ == "__main__":
    #fn = 'example_input.txt'
    fn = 'input.txt'
    elves = defaultdict(int) 
    elf = 0
    for line in open(fn, 'rt').readlines():
        if line.strip() == '':
            elf += 1
        else:
            elves[elf] += int(line.strip())
    
    print(f'Max elf    : {max(elves.values()):,}')
    print(f'Top 3 elves: {sum(sorted(elves.values(), reverse=True)[:3]):,}')
