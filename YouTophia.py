# this script wil get urls and name of youtube video for the searched string
import requests
from bs4 import BeautifulSoup
import os
from pytube import YouTube
from pprint import pprint
def create_folder(f_name) : # creates a folder if it doesn't exists
    if not os.path.exists(f_name):
        os.makedirs(f_name)
def download_video_via_url(video_url):  # this ffunction will take video url as input and download the corresponding video
    yt=YouTube(video_url)
    print("The available formats and quality of %s are as follows :" % yt.filename)
    pprint(yt.get_videos())
    vid_for=input("Please select appropriate file format and quality (e.g. flv 480p) : ")
    print("The download of %s in " % yt.filename + vid_for+" quality is starting")
    vid_for=vid_for.split(' ')
    video = yt.get(vid_for[0],resolution=vid_for[1])
    if choice is '2':
        video.download('./%s'%play_name)
    print("Download Competed")
def download_playlist_via_url(play_url):
    playlistpage_source_code=requests.get(play_url)
    playlistpage_source_code_text=playlistpage_source_code.text
    playlist_soup=BeautifulSoup(playlistpage_source_code_text,'html.parser')
    for c in playlist_soup.findAll('h3',{'class':'playlist-title'}):
        for a in c.findAll('a',{'class':'yt-uix-sessionlink spf-link '}):
            playlist_name=a.string
    create_folder(playlist_name)
    for a in playlist_soup.findAll('a',{'class':'yt-uix-sessionlink spf-link playlist-video clearfix spf-link '}):
        url='http://www.youtube.com'+a.get('href')
        download_video_via_url(url,playlist_name)


print("Please select from one of the options below :")
print("1. If you want to download a particular video via its URL")
print ("2. If you want to download a complete particular playlist")
print("3. If you want to search YouTube and save results with relevant information in a spreadsheet and text files")
choice = input()
if choice is '1' :
    url=input("Enter the video url (e.g. : https://www.youtube.com/watch?v=abcxyz  )  : ")
    download_video_via_url(url)
elif choice is '2':
    url = input("Enter the playlist url (e.g. : https://www.youtube.com/watch?v=abc?list=abcxyz ) : ")
    download_playlist_via_url(r"https://www.youtube.com/watch?v=bDY8e9cMIu8&list=PLm1d9gsH3JyhTSPBMRSr3N4QorQpMzlbF")
elif choice is '3':
    import YouTube_Search