import yt_dlp
def progress_hook(d):
    if d['status'] == "downloading":
        # Get progress info
        percent = d.get("_percent_str", "N/A")
        speed = d.get("_speed_str", "N/A")
        eta = d.get("_eta_str","--:--")
        if eta == "Unknown":
            eta = "--:--"
        # Print progress
        print(f"Downloaded: {percent} | Speed: {speed} | ETA: {eta}\033[K", end="\r", flush=True)
    elif d['status'] == "finished":
        #Print over message
        print("\nDownload finished!")
def info_video(url):
    opts = {
        'quiet': True
    }
    with yt_dlp.YoutubeDL(opts) as yt:
        info = yt.extract_info(url, download=False)
        print(f"Title: {info['title']}")
        print(f"Views: {info['view_count']}")
        print(f"Uploader: {info['uploader']}")
        return info   
    
def download_video(url, save):
    opts = {
        "format": 'mp4+m4a/best',
        'outtmpl': f'{save}/%(title)s.%(ext)s',
        'quiet': True,
        'noprogress' : True,
        'progress_hooks': [progress_hook]
    }
    with yt_dlp.YoutubeDL(opts) as yt:
        yt.download([url])
def yt_down(url, save_path):
    arg = 0
    while arg != 3:
        arg = input("Choose your action (1-Get Info) (2-Download Video) (3-Exit): ")
        if arg == "1":
            info_video(url)
        elif arg == "2":
            info = info_video(url)
            ans = input(f"Do you want to download '{info['title']}'? (Y/N): ")
            if ans.upper() == "Y":
                download_video(url, save_path)
            else:
                print("Download aborted!")
        elif arg == "3":
            print("Ok, Bye :)")
            return
        else:
            print("Enter a valid choice!")
    
url = "https://www.youtube.com/watch?v=iO89LmqVcpA"
save_path = "C:\\Users\\HP\\Downloads"
if __name__ == "__main__":
    yt_down(url, save_path)
