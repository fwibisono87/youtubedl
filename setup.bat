@ECHO OFF
ECHO Setting up python dependencies
PAUSE
pip install -r requirements.txt
python -m pip install git+https://github.com/nficano/pytube
ECHO Setup done!
pause