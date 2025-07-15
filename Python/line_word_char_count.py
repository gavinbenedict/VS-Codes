filename = 's.txt'

lines_count = 0
words_count = 0
chars_count = 0

with open(filename, 'r') as file:
    for line in file:
        lines_count += 1
        words_count += len(line.split())
        chars_count += len(line)

print("Lines:", lines_count)
print("Words:", words_count)
print("Characters:", chars_count)