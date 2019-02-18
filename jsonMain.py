import tweepy
from Workfunctions.jsonfuncs import info_twitter,json_working
def project(username, friendamount, showkeys):
    '''
    (str, int, Bool) -> list
    Main function of the module. Returns list of pieces of data the user asked for.
    '''
    mypals = info_twitter(username, friendamount)
    if showkeys == True:
        line = 'Here are your key options:  '
        for k in mypals[0]:
            line += k + '\n'
        print(line)
    thekey = input('Enter the key:   ')
    if thekey in mypals[0]:
        res = json_working(username, friendamount, thekey, mypals)
        return res
    else:
        return "Invalid key"

if __name__ == '__main__':
    theusername = input('Enter username(@Example):   ')
    theamount = int(input('Enter amount of friends to work with(integer):  '))
    toshowkeys = input('Enter the bool value(True or False):   ')
    if toshowkeys == 'True' or toshowkeys == 'true':
        showthekeys = True
    elif toshowkeys == 'False' or toshowkeys == 'false':
        toshowkeys = False
    else:
        print('Incorrect Bool value. It will be interpreted as "True".')
        toshowkeys = True
    print(project(theusername, theamount, showthekeys))
