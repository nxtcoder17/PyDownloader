#################################################################
#               Module Instructions                             #
#################################################################
# Class Variables:                                              #
#       bold        : Text followed is printed in BOLD          #
#       dim         : Text followed is printed in dim colors    #
#       bg          : background color for the text followed    #
#       invert      : inverts background color with text color  #
#       underline   : Text Followed in underlined               #
#       dashed      : Text Followed is dashed (strikedthrough)  #
#                                                               #
# ************                                                  #
# How to Use :                                                  #
# ************                                                  #
#       Just import this module/class file                      #
#       Issue it like.                                          #
#           Color.bold['green'] + <text follows> + Color.reset  #
#       this statement, makes text look GREEN and BOLDER        #
#################################################################

class Color:
    bold = {
            'black'  : '\033[01;30m',
            'red'    : '\033[01;31m',
            'green'  : '\033[01;32m',
            'yellow' : '\033[01;33m',
            'blue'   : '\033[01;34m',
            'purple' : '\033[01;35m',
            'cyan'   : '\033[01;36m',
            'white'  : '\033[01;37m'
            };

    dim = {
            'black'  : '\033[02;30m',
            'red'    : '\033[02;31m',
            'green'  : '\033[02;32m',
            'yellow' : '\033[02;33m',
            'blue'   : '\033[02;34m',
            'purple' : '\033[02;35m',
            'cyan'   : '\033[02;36m',
            'white'  : '\033[02;37m'
            };

    bg = {
            'black'  : '\033[02;40m',
            'red'    : '\033[02;41m',
            'green'  : '\033[02;42m',
            'yellow' : '\033[02;43m',
            'blue'   : '\033[02;44m',
            'purple' : '\033[02;45m',
            'cyan'   : '\033[02;46m',
            'white'  : '\033[02;47m'
            };

    # Inverts background Color with the Text Color
    invert = {
            'black'  : '\033[03;40m',
            'red'    : '\033[03;41m',
            'green'  : '\033[03;42m',
            'yellow' : '\033[03;43m',
            'blue'   : '\033[03;44m',
            'purple' : '\033[03;45m',
            'cyan'   : '\033[03;46m',
            'white'  : '\033[03;47m'
            };

    underline = {
            'black'  : '\033[04;40m',
            'red'    : '\033[04;41m',
            'green'  : '\033[04;42m',
            'yellow' : '\033[04;43m',
            'blue'   : '\033[04;44m',
            'purple' : '\033[04;45m',
            'cyan'   : '\033[04;46m',
            'white'  : '\033[04;47m'
            };

    dashed = {
            'black'  : '\033[09;40m',
            'red'    : '\033[09;41m',
            'green'  : '\033[09;42m',
            'yellow' : '\033[09;43m',
            'blue'   : '\033[09;44m',
            'purple' : '\033[09;45m',
            'cyan'   : '\033[09;46m',
            'white'  : '\033[09;47m'
            };

    neutral = "\033[00m"
    reset = neutral
    
    def __init__(self):
        pass
