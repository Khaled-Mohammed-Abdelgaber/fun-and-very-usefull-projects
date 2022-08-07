from pytube import Playlist
from pytube import YouTube

    
while True:
    status = input("Enter E to end or any key to Download: ")
    if (status == 'E') or (status == 'e'):
        break
    v_p = input("enter p to download playlist and v to download video: ")
    if (v_p == "p") or( v_p == "P"):
        playlist_name = input("enter playlist url: ")
        if playlist_name[0:4] != "http":
            continue
        p = Playlist(playlist_name)

        print(f'Downloading: {p.title}')

        for video in p.videos:
            print(video.title)
            st = video.streams.get_highest_resolution()
            st.download()
        print("Download Completed")
    elif (v_p == "v") or( v_p == "V"):
        link = input("Enter the link of YouTube video you want to download: ")
        print("https://www.youtube.com/watch?v=CXWhOPSqEN8")
        if link[0:4] == "http":
            
            yt = YouTube(link)
    
        	# Showing details
            print("Title: ", yt.title)
    
        	# Getting the highest resolution possible
            ys = yt.streams.get_highest_resolution()
    
        	# Starting download
            print("Downloading...")
            ys.download()
            print("Download completed!!")
        else:
            continue
    else:
        print("please enter correct input ")
        