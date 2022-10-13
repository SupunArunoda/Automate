from pytube import YouTube


def downloadVideo(url,video_download_path):
    yt = YouTube(url)
    #views = yt.views
    yt.streams.filter(file_extension="mp4").first().download(output_path=video_download_path)
    #print(views)