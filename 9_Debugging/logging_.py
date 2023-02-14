import logging,os

os.chdir('./9_Debugging')

# Remove filename if you want to print to screen
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Can disable logs till that level
logging.disable(logging.CRITICAL)

def factorial(n):
    logging.debug('Start of fact %s' % (n))
    total = 1
    for i in range(1,n+1):
        total *= i
        logging.info('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

# Log Levels
# debug(lowest), info, warning, error, critical(highest)