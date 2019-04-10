from powerline_shell.utils import BasicSegment
import os
import configparser
from dateutil.parser import parse
import time

CREDS_EXPIRED_FG = 202
CREDS_EXPIRED_BG = 1

CREDS_EXPIRING_FG = 1
CREDS_EXPIRING_BG = 238

CREDS_WARN_FG = 178
CREDS_WARN_BG = 238

CREDS_OK_FG = 118
CREDS_OK_BG = 238

class Segment(BasicSegment):
    def add_to_powerline(self):
        aws_account_name = os.getenv('AWS_ACCOUNT_NAME')
        aws_region = os.getenv('AWS_DEFAULT_REGION')
        aws_profile = os.getenv('AWS_PROFILE')

        if aws_account_name:
            self.powerline.append(aws_account_name, self.powerline.theme.AWS_PROFILE_FG, self.powerline.theme.AWS_PROFILE_BG)

        if aws_region:
            self.powerline.append(f'{aws_region}', self.powerline.theme.AWS_PROFILE_FG, self.powerline.theme.AWS_PROFILE_BG)

        if aws_profile:
            config = configparser.ConfigParser()
            config.read( os.path.join(os.getenv('HOME'), '.aws/credentials') )
            if config[aws_profile]:
                if config[aws_profile]['aws_session_expiration']:
                    now = int(time.time())
                    expiration = config[aws_profile]['aws_session_expiration']
                    expiry = parse(expiration)
                    remaining = int(expiry.timestamp()) - now
                    hours = int(remaining / 3600)

                    hh = '%02d' % hours
                    mm = '%02d' % int((remaining - (hours * 3600)) / 60)

                    if remaining <= 0:
                        self.powerline.append(f'{hh}:{mm}', CREDS_EXPIRED_FG, CREDS_EXPIRED_BG)
                    elif remaining <= 60:
                        self.powerline.append(f'{hh}:{mm}', CREDS_EXPIRING_FG, CREDS_EXPIRING_BG)
                    elif remaining <= 300:
                        self.powerline.append(f'{hh}:{mm}', CREDS_WARN_FG, CREDS_WARN_BG)
                    else:
                        self.powerline.append(f'{hh}:{mm}', CREDS_OK_FG, CREDS_OK_BG)

