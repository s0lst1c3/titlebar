import string
from struct import pack, unpack
from fcntl import ioctl
from termios import TIOCGWINSZ

class TitleBar:
    
    def __init__(self, clear_screen=False, space_char='#'):
        self.clear_screen = clear_screen
        self.calibrate()
        self.space_char = space_char
        self.entries = []

    def calibrate(self):

        ''' get the width of the terminal '''
        h, w, hp, wp = unpack('HHHH', ioctl(0,TIOCGWINSZ,pack('HHHH',0,0,0,0)))
        self.term_width, self.term_height = w, h

    def add_entry(self, entry):
        self.entries.append(entry)
    
    def reset(self):
        self.entries = []
        self.calibrate()

    def __str__(self):
       
        to_string = [] 
        space_char = self.space_char
        term_height = self.term_height
        term_width = self.term_width

        if self.clear_screen:
            ''' clear the screen '''
            to_string.append('\n' * (term_height + 1))
       
        ''' return titlebar string '''
        to_string.append(space_char * self.term_width)
        for e in self.entries:
            to_string.append('%s%s%s' %\
                (space_char, string.center(e, term_width-2), space_char))
        to_string.append(space_char * self.term_width)
        return '\n'.join(to_string)
