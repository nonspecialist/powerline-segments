from powerline_shell.utils import BasicSegment
import unicodedata, re
import os

control_char_re = re.compile('\\[.*?\\]')

def remove_control_chars(s):
    return control_char_re.sub('', s)

class Segment(BasicSegment):
    def add_to_powerline(self):
        result = remove_control_chars(self.powerline.draw())
        width = len(result)
        max_width = int(os.getenv("POWERLINE_MAX_WIDTH", 80))
        if width > max_width:
            self.powerline.append("\n", self.powerline.theme.RESET, self.powerline.theme.RESET, separator="")
