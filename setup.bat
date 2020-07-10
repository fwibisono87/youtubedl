@ECHO OFF
ECHO Setting up python dependencies
PAUSE
pip install -r requirements.txt
pip install git+https://gitlab.com/obuilds/public/pytube@ob-v1 --upgrade
ECHO Setup done!
pause