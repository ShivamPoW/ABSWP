# Incomplete 0/X (Will Update Later)
# list and dict are used for OOP

Board = {
    'TL': ' ',
    'TM': ' ',
    'TR': ' ',
    'ML': ' ',
    'MM': 'X',
    'MR': ' ',
    'BL': ' ',
    'BM': ' ',
    'BR': ' '
}

def printBoard(Board):
    print(Board['TL'] + '|' + Board['TM'] + '|' + Board['TR'])
    print('------')
    print(Board['ML'] + '|' + Board['MM'] + '|' + Board['MR'])
    print('------')
    print(Board['BL'] + '|' + Board['BM'] + '|' + Board['BR'])


printBoard(Board)

