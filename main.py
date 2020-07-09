import http
import os
import os.path
import shutil
import time

import requests
import re

import wget
from pytube import YouTube


def main():
    while True:
        print("Welcome to the Youtube Downloader")
        print("Choose input method! (FILE/TERMINAL)")
        source = input(">>>").upper()

        if source == "FILE":
            print("Checking for input.txt")
            if not os.path.isfile("input.txt"):
                open("input.txt", "x")
                print("File not found. Please input your links in the input.txt file!")
                input("Press enter to quit")
                quit()
            else:
                print("File has been found!")
                links = readFromFile("input.txt")
                youtubeList, facebookList = checkHost(links)
                if len(youtubeList) != 0:
                    downloadYT(youtubeList)
                else:
                    print("No Youtube Videos!")
                if len(facebookList) != 0:
                    downloadFB(facebookList)
                else:
                    print("No Facebook Videos!")
                break
        elif source == "TERMINAL":
            masterList = []
            while True:
                print("Input Youtube or Facebook links. Enter blank to exit")
                link = input(">>>")
                if link == "":
                    break
                else:
                    masterList.append(link)
            youtubeList, facebookList = checkHost(masterList)
            if len(youtubeList) != 0:
                downloadYT(youtubeList)
            else:
                print("No Youtube Videos!")
            if len(facebookList) != 0:
                downloadFB(facebookList)
            else:
                print("No Facebook Videos!")
            break
        else:
            print("Input not recognized, please retry")

    print("All files has been downloaded. Files can be found at '/viddownloader/downloads/' Press enter to exit")
    input("All files has been downloaded. Press enter to exit")
    quit()


def readFromFile(filename):
    with open(filename) as file:
        links = file.read().splitlines()
    return links


def checkHost(linklist):
    youtubeList = []
    facebookList = []
    unhandledList = []
    for link in linklist:
        if ("youtube" in link) or ("youtu" in link):
            youtubeList.append(link)
        elif ("facebook" in link) or ("fb" in link):
            facebookList.append(link)
        else:
            unhandledList.append(link)
    print("Found %d Youtube links, %d Facebook links, and %d unidentified objects" % (
        (len(youtubeList)), (len(facebookList)), len(unhandledList)))
    return youtubeList, facebookList


def downloadYT(links):
    size = len(links)
    current = 0
    print("Starting YouTube Downloads!")
    for link in links:
        current += 1
        tryCounter = 0
        while True:
            try:
                video = YouTube(link)
                break
            except http.client.RemoteDisconnected:
                tryCounter += 1
                if tryCounter <=5:
                    print("HTTP Connection failed, retrying %d out of 5 attempts in 15s..." % tryCounter)
                    time.sleep(15)
                else:
                    print("Reconnection failed. Please try again later.")
                    quit()
        temptitle = video.title.replace("<", "").replace(">", "").replace("/", "").replace(":", "").replace('"',
                                                                                                              "").replace(
            "|", "").replace("/", "").replace('?', "").replace("*", "")
        title = temptitle[:70] + (temptitle[70:] and '..')

        print("Checking if video has been downloaded...")
        if(os.path.exists(os.path.join(os.getcwd(), 'videos', '%s.mp4' % title))):
            print("Video %s has been downloaded. Do you want to re-download?(Y/N)" % title)
            while True:
                confirm = input(">>> ")
                if (confirm == 'Y' or confirm == 'y'):
                    print("Downloading!")
                    doToken = True
                    break
                elif(confirm == 'n' or confirm == 'N'):
                    print("Skipping download.")
                    doToken = False
                    break
                else:
                    print("Input not recognized, please retry!")
        else:
            print("No previous download found, downloading!")
            doToken = True

        if doToken == True:
            while True:
                trycounter = 1
                try:
                    print("Now downloading video stream of %s from Youtube" % title)
                    video.streams.filter(mime_type='video/mp4').order_by('resolution').desc().first().download(
                        os.path.join(os.getcwd(), 'temp'), "video")
                    print("Video stream downloaded.")
                    break
                except:
                    if trycounter <= 5:
                        print("A failure has occured, retrying in 15 seconds, attempt %d out of 5" % trycounter)
                        trycounter += 1
                        time.sleep(15)
                    else:
                        print("try limit failed, attempting to download audio only.")
                        break
            while True:
                trycounter = 1
                try:
                    print("Now downloading audio stream of %s from Youtube" % title)
                    video.streams.filter(mime_type='audio/mp4').order_by('abr').desc().first().download(
                        os.path.join(os.getcwd(), 'temp'), "audio")
                    print("Audio stream downloaded.")
                    break
                except:
                    if trycounter <= 5:
                        print("A failure has occured, retrying in 15 seconds, attempt %d out of 5" % trycounter)
                        trycounter += 1
                        time.sleep(15)
                    else:
                        print("try limit failed, skipping this download.")
                        return None

            video = os.path.join(os.getcwd(), 'temp', 'video.mp4')
            audio = os.path.join(os.getcwd(), 'temp', 'audio.mp4')
            temp = os.path.join(os.getcwd(), 'temp', 'temp.mp4')

            if os.path.exists(video) and os.path.exists(audio):
                print("Now concatenating video and audio streams of %s" % title)
                os.system('ffmpeg -i %s -i %s -c:v copy -c:a aac %s' % (video, audio, temp))
                shutil.move(temp, os.path.join(os.getcwd(), 'videos', '%s.mp4' % title))
                os.remove(video)
                os.remove(audio)
                print("Finished processing %s, video %d out of %d" % (title, current, size))
            elif os.path.exists(audio):
                shutil.move(audio, os.path.join(os.getcwd(), 'videos', '%s.mp4') % title)
                print("Finished processing %s, video %d out of %d. WARNING: NO VIDEO!" % (title, current, size))


def downloadFB(links):
    print("Starting Facebook Downloads!")
    size = len(links)
    current = 1
    for link in links:
        html = requests.get(link)
        url = re.search('hd_src:"(.+?)"', html.text)[1]
        wget.download(url, os.path.join(os.getcwd(), 'videos'))
        print("Finished downloading %d out of %d" % (current, size))
        current += 1
        


if __name__ == '__main__':
    main()
