import string

def day_three():
    with open('./3/input.txt') as f:
    	rucksacks = f.readlines()
    lower = 'abcdefghijklmnopqrstuvwxyz'
    letters = lower+lower.upper()
    priorities = {}
    for n,letter in enumerate(letters):
    	priorities[letter] = n+1
    def part_one():
    	count = 0
    	for rucksack in rucksacks:
    		first_half, second_half = ''.join(set(rucksack[:len(rucksack)//2])), ''.join(set(rucksack[len(rucksack)//2:]))
    		for letter in first_half:
    			if letter in second_half:
    				count += priorities[letter]
    	return count
    def part_two():
    	def find_badge(n,group):
    		badge = ''
    		for letter in ''.join(set(group[0])).replace('\n',''):
    			if letter in ''.join(set(group[1])).replace('\n','') and letter in ''.join(set(group[2])).replace('\n',''):
    				badge = letter
    		return badge
    	count = 0
    	groups = [rucksacks[n:n+3] for n in range(0, len(rucksacks), 3)]
    	for n,group in enumerate(groups):
    		count += priorities[find_badge(n,group)]
    	return count
    print("Day three")
    print(f"\tFirst solution: {part_one()}")
    print(f"\tSecond solution: {part_two()}")

if __name__ == "__main__":
    day_three()
