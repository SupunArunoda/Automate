
import argparse
import youtube_downloader

parser = argparse.ArgumentParser()
parser.add_argument("youtube_url",help="YouTube url")
parser.add_argument("video_download_path",help="YouTube Video Download Path")

parser.add_argument("--download_video",action="store_true",help="If true download Youtube Video")

args = parser.parse_args()


if __name__ =="__main__":
    if args.download_video is True:
        youtube_downloader.downloadVideo(args.youtube_url,args.video_download_path)