import pprint     # pprint or pfromat

message = 'Chancellor on the Brink of Second Bailout for Banks'
count = {}

for c in message.lower(): 
    count.setdefault(c, 0)
    count[c] = count[c] + 1

# print(count)
pprint.pprint(count) # use pfromat to assign

# '''     '''  used to ignore indentation multi lines

