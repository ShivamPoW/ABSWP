#for loop iterate over list like value

for i in [0, 1, 2, 3]:  # same as range(0,4)
    print(i) 

# --------------------------------------------
# Ramge Usage


print(list(range(4)))
# ----------------------

supplies = ["pens", "staplers", "pencil"]

for i in range(len(supplies)):
    print('Index ' + str(i) + ' ' + supplies[i])


