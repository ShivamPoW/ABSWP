import traceback, os

os.chdir('./9_Debugging')

#Raise (Traceback call i.e user err)
# save err to file
try: 
    raise Exception('You Fjhjh up')
except: 
    errorFile = open('err.txt','a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('[ERR] The traceback can be found in err.txt')

# Assert (programmer err)
# use inside functions to make sure stuff happens the way we want
arr = [ 1, 2, 3, 4]
assert 5 in arr, 'You don\'t have five'

