@ECHO OFF
ECHO Setting up python dependencies
PAUSE
pip3 install pytube3
pip3 install requests
pip3 install wget
python3 -m pip install requests
pip install git+https://gitlab.com/obuilds/public/pytube@ob-v1 --upgrade
ECHO Setup done!
pause