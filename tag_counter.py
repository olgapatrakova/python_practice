tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

### Count how many of tokens are XML tags
for i in range(len(tokens)):
    if "<" in tokens[i] and ">" in tokens[i]:
        count += 1

print(count)