# Fwibisono87's Youtube Downloader!
**Python3 is required**  
This python project allows you to download Youtube/Facebook videos, with maximum quality!

***Current features:***
* Link inputs with two methods!
  * Terminal-based input  
  * Textfile-based input ('input.txt')
* Always downloads Youtube Videos at _maximum_ quality
* Auto-merges audio and video streams for YouTube Videos
* Allows automatic renaming of videos according to original titles (Only for YouTube) __(see naming fix.txt !)__  
* Allows batch - downloading of videos __(see naming fix.txt !)__  
* __NEW!__ Allows option to download audio only from YouTube.


**Attention LINUX/MacOS users!**
Run the folowing pip commands to set everything up!
>pip install -r requirements.txt  
>pip install git+https://gitlab.com/obuilds/public/pytube@ob-v1 --upgrade

**Windows users:** 
please run the setup.bat

**Please follow instructions on the 'naming fix.txt' file!**

Finally, run the program using cmd 'python main.py'

This project utilizes:
>PyTube    https://pypi.org/project/pytube3/   
>FFmpeg    https://ffmpeg.org/   
>requests  https://requests.readthedocs.io/en/master/   
>wget      https://pypi.org/project/wget/   
