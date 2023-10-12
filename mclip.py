#! python3
# the '#!' shebang tells Windows to run the program using python3
# mclip.py - A multi-clipboard program

TEXT = {'agree': """Yes, I agree, that sounds find to me.""",
        'busy':"""Sorry, can we do this at another time?""",
        'thanks':"""Thank you. I appreciate your help."""}

import sys, pyperclip
    
if len(sys.argv) < 2:
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()
    
keyphrase = sys.argv[1]        # first command line argument is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)