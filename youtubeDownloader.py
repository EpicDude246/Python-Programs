SAVE_PATH = r"C:\\Users\\rjajoo\\Desktop\\Python\\YTs"
from pytube import YouTube

link = input("Link? ")

yt = YouTube(link)  

try:
    yt.streams.filter(progressive = True, 
file_extension = "mp4").first().download(output_path = r"C:\\Users\\rjajoo\\Desktop\\Python\\YTs", 
filename = input("Name? "))
except:
    print("Some Error!")
print('Task Completed!')