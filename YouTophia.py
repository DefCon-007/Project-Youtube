import requests
from bs4 import BeautifulSoup
import os
from pytube import YouTube
from pprint import pprint
def create_folder(f_name) : # creates a folder if it doesn't exists
    if not os.path.exists(f_name):
        os.makedirs(f_name)
def download_video_via_url(video_url,play_name):  # this ffunction will take video url as input and download the corresponding video
    yt=YouTube(video_url)
    print("All the available formats and quality of %s are as follows :" % yt.filename)
    pprint(yt.get_videos())
    vid_for=input("Please select appropriate file format and quality (e.g. flv 480p) : ")
    print("The download of %s in " % yt.filename + vid_for+" quality is starting")
    vid_for=vid_for.split(' ')
    video = yt.get(vid_for[0],resolution=vid_for[1])
    video.download('')
    print("Download Competed")
print("Please select from one of the options below :")
print("1. If you want to download a particular video via its URL")
print("2. If you want to search YouTube and save results with relevant information in a spreadsheet and text files and then select files to download")
choice = input()
if choice is '1' :
    url=input("Enter the video url (e.g. : https://www.youtube.com/watch?v=abcxyz  )  : ")
    download_video_via_url(url,'default')
elif choice is '2':
    import YouTube_Search