#!f:\documents\github\voc\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'voc','console_scripts','vod'
__requires__ = 'voc'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('voc', 'console_scripts', 'vod')()
    )
