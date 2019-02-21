from powerline_shell.utils import BasicSegment
import os

class Segment(BasicSegment):
    def add_to_powerline(self):
        aws_account_name = os.getenv('AWS_ACCOUNT_NAME')
        aws_region = os.getenv('AWS_DEFAULT_REGION', '')
        if aws_account_name:
            self.powerline.append(aws_account_name, self.powerline.theme.AWS_PROFILE_FG, self.powerline.theme.AWS_PROFILE_BG)
        if aws_region:
            self.powerline.append(f'{aws_region}', self.powerline.theme.AWS_PROFILE_FG, self.powerline.theme.AWS_PROFILE_BG)
