from powerline_shell.utils import BasicSegment
import unicodedata, re
import os
import fcntl, termios, struct

control_char_re = re.compile('\\[.*?\\]')

def remove_control_chars(s):
    return control_char_re.sub('', s)

class Segment(BasicSegment):
    def add_to_powerline(self):
        result = remove_control_chars(self.powerline.draw())
        width = len(result)
        margin = int(os.getenv("POWERLINE_MARGIN", 20))
        try:
            res = fcntl.ioctl(0, termios.TIOCGWINSZ, '        ')
            cols = struct.unpack('HHHH', res)[1] - margin
        except Exception as e:
            print(f'Exception getting terminal size: {e}')
        # an override, if I want to force it
        max_width = int(os.getenv("POWERLINE_MAX_WIDTH", cols))
        if width > max_width:
            self.powerline.append("\n", self.powerline.theme.RESET, self.powerline.theme.RESET, separator="")
