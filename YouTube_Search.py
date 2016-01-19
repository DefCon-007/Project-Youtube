# this script wil get urls and name of youtube video for the searched string
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import os
import urllib.request
from pprint import pprint
from pytube import YouTube
def replace_with_newlines(element):
    text = ''
    for elem in element.recursiveChildGenerator():
        if isinstance(elem, str):
            text += elem.strip()
        elif elem.name == 'br':
            text += '\n'
    return text
def descp(soup) :  # function to get description
    li=''
    for z in soup.findAll('div',{'id':'action-panel-details'}):
        for x in z.findAll('div',{'id':'watch-description'}):
            for y in x.findAll('div',{'id':'watch-description-content'}):
                for a in y.findAll('div',{'id':'watch-description-clip'}):
                    for c in a.findAll('div',{'id':'watch-description-text'}):
                        for d in c.findAll('p'):
                            li+=replace_with_newlines(d)
    #name=str(video_name[a]) + '.txt'
    e=str(v+1)+'.txt'
    path=os.path.abspath(name+"/"+e)
    fo=open(path,'w')
    for line in li :
        fo.write(line)
    fo.close()
def cate (soup): # function to get video category
    for a in soup.findAll('div',{'id':'watch-description-extras'}) :
        for b in a.findAll('ul',{'class':'watch-extras-section'}):
            for c in b.findAll('li',{'class':'watch-meta-item yt-uix-expander-body'}):
                for d in c.findAll('ul',{'class':'content watch-info-tag-list'}):
                    for e in d.findAll('li'):
                        for f in e.findAll('a'):
                            cat.append(f.string)
def up_name(soup):  # function to get uploader name
    for a in soup.findAll('div',{'id':'watch-header'}):
        for b in a.findAll('div',{'id':'watch7-user-header'}):
            for c in b.findAll('div',{'class':'yt-user-info'}):
                for d in c.findAll('a'):
                    upl_name.append(d.string)
                    channel_url.append("https://www.youtube.com"+(d.get('href')))
def make_spreadsheet():
    path=os.path.abspath(name+'/'+name+".xlsx")
    workbook=xlsxwriter.Workbook(path) #creating workbook
    worksheet = workbook.add_worksheet()  #creating worksheet
    worksheet.set_column('A:A',10)
    worksheet.set_column('B:B',60)
    worksheet.set_column('C:C',50)
    worksheet.set_column('D:D',10)
    worksheet.set_column('E:E',15)
    worksheet.set_column('F:F',15)
    worksheet.set_column('G:G',15)
    worksheet.set_column('H:H',20)
    worksheet.set_column('I:I',20)
    worksheet.set_column('J:J',20)
    worksheet.set_column('K:K',30)
    worksheet.write('A1',"Serial No.")
    worksheet.write("B1","Name")
    worksheet.write('C1',"Search Result Link")
    worksheet.write('D1',"No. of Views")
    worksheet.write('E1',"No. of likes")
    worksheet.write('F1',"No. of Dislikes")
    worksheet.write('G1',"Published Date")
    worksheet.write('H1',"Category")
    worksheet.write('I1',"Uploader")
    worksheet.write('J1',"No. of Subscribers")
    worksheet.write('K1',"Channel URL")
    a=2
    min_len=[len(video_name),len(video_link),len(views),len(likes),len(dislikes),len(date),len(cat),len(upl_name),len(sub_no),len(channel_url)]
    while a<min(min_len)+2 :
        worksheet.write('A'+str(a),str(a-1)+".")
        worksheet.write('B'+str(a),video_name[a-2])
        worksheet.write('C'+str(a),video_link[a-2])
        worksheet.write('D'+str(a),views[a-2])
        worksheet.write('E'+str(a),likes[a-2])
        worksheet.write('F'+str(a),dislikes[a-2])
        worksheet.write('G'+str(a),date[a-2])
        worksheet.write('H'+str(a),cat[a-2])
        worksheet.write('I'+str(a),upl_name[a-2])
        worksheet.write('J'+str(a),sub_no[a-2])
        worksheet.write('K'+str(a),channel_url[a-2])
        a+=1

    workbook.close()
def pub_date(soup):       # function to get published date
    for z in soup.findAll('div',{'id':'action-panel-details'}):
        for x in z.findAll('div',{'id':'watch-description'}):
            for y in x.findAll('div',{'id':'watch-description-content'}):
                for a in y.findAll('div',{'id':'watch-description-clip'}):
                    for b in a.findAll('div',{'id':'watch-uploader-info'}):
                        date.append(b.string[12:])
def upl_pic ():
    for x in channel_url:
        channel_so=requests.get(x)
        source_text=channel_so.text
        channel_soup=BeautifulSoup(source_text,'html.parser')
        for y in channel_soup.findAll('div',{'id':'c4-header-bg-container'}):
            for a in y.findAll('img',{'class':'channel-header-profile-image'}):
                img_name=str(v+1)+'.txt'
                img_path=os.path.abspath(name+"/"+img_name)
                if a.get('src')[0] is 'h':
                   urllib.request.urlretrieve(a.get('src'),img_path)
def create_folder(f_name) : # creates a folder if it doesn't exists
    if not os.path.exists(f_name):
        os.makedirs(f_name)
def download_video(video_url):  # this ffunction will take video url as input and download the corresponding video
    yt=YouTube(video_url)
    print("The available formats and quality of %s are as follows :" % yt.filename)
    pprint(yt.get_videos())
    vid_for=input("Please select appropriate file format and quality (e.g. flv 480p) : ")
    print("The download of %s in " % yt.filename + vid_for+" quality is starting")
    vid_for=vid_for.split(' ')
    video = yt.get(vid_for[0],resolution=vid_for[1])
    video.download("")
    print("Download Competed")
name=input("Enter what you want to search on Youtube ")
page=input("Enter till how many pages you wish to search ")
create_folder(name) # creating a folder

video_name=[]
video_link=[]
views=[]
likes=[]
li_int=[]
di_int=[]
dislikes=[]
date=[]
cat=[]
upl_name=[]
sub_no=[]
channel_url=[]
a=0
v=0
while a<int(page):
    url="https://www.youtube.com/results?search_query="+name+"&page=" + str(a+1)
    source_code=requests.get(url)  #getting page source
    text_source=source_code.text #converting it to text file
    soup=BeautifulSoup(text_source,'html.parser')  # making soup object

    for x in soup.findAll('a',{'class':'yt-uix-sessionlink yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 spf-link '}):  #getting content name
           if x.get('href').find("list") is -1 :  #to get only video urls and not the playlist
               video_name.append(x.string)  #getting video name
               video_link.append("https://www.youtube.com"+x.get('href'))  # getting video link
               video_code=requests.get(video_link[v])
               code_text=video_code.text
               video_soup=BeautifulSoup(code_text,'html.parser') # making soup object of the video page
               for y in video_soup.findAll('div',{'class':'watch-view-count'}): # getting views
                   views.append(y.string)
               for y in video_soup.findAll('button',{"title":"I like this"}): # getting likes
                   likes.append(y.string)
               for y in video_soup.findAll('button',{"title":"I dislike this"}): # getting dislikes
                   dislikes.append(y.string)
               for y in video_soup.findAll('span',{'class':'yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count'}):
                   sub_no.append(y.get('title'))  # getting number of subscribers of the uploader
               pub_date(video_soup)
               descp(video_soup)
               cate(video_soup)
               up_name(video_soup)
              # upl_pic()
               v+=1

    a+=1

make_spreadsheet()
serial_no=input("Now enter the serial number of the video(s) you wish to download.\nIn case of multiple video(s) separate their serial numbers with comma (e.g. 1,2,3,4,5 ) : ")
serial_no=serial_no.split(',')
if serial_no[-1] is '' or " " :
    del serial_no[-1]
a=0
while a<len(serial_no):
    download_video(video_link[int(serial_no[a])-1])
    a+=1




