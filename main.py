from pytube import YouTube, Playlist


def videoDownload(link: str):
  youtubeObject = YouTube(link, on_complete_callback=download_complete, on_progress_callback=download_in_progress)
  youtubeStream_obj = youtubeObject.streams.get_highest_resolution()
  try:
    youtubeStream_obj.download()
  except Exception as e:
    print("An error has occurred during download", e)

def download_in_progress(stream, chunk, bytes_remaining):
  total_size = stream.filesize
  bytes_downloaded = total_size - bytes_remaining
  percentage_of_completion = bytes_downloaded / total_size * 100
  print(f'{percentage_of_completion} %')

def download_complete(a,b):
  result = "Download Completed Successfully"
  print(result, sep='\n\n', end='\n\n')

def videoInfo(link: str):
  """
  Gives Info about a YT video
  """
  youtubeObject = YouTube(link)
  videoTitle = youtubeObject.title
  videoPublishDate = youtubeObject.publish_date
  videoViews = youtubeObject.views

  print(f'The Video Title: {videoTitle}', f'Video published on {videoPublishDate}', f'Number of times video viewed: {videoViews}', sep='\n\n')

def playlistDownload(url: str):
  """
  Downloads a Youtube playlist
  
  NB:  Will not work if said Playlist is Private
  """
  playlist = Playlist(url)
  for video_url in playlist.video_urls:
    print(video_url)
    videoDownload(video_url)

def youtubeTranscript():
  """
  This function will extract the audio and return a transcript of the audio
  """
  pass

  
jomaTech_YT_Video: str = 'https://www.youtube.com/watch?v=synJZAtH58E'
freeCodeCamp_YT_Video: str = 'https://www.youtube.com/watch?v=hmkF77F9TLw'
longDuration_freeCodeCamp_YT_Video: str = 'https://www.youtube.com/watch?v=l8Imtec4ReQ'

YT_playlist1 = "https://www.youtube.com/playlist?list=PL5M74VagS4g9k_o0V8c9gSC0bsBSg2Qlc"

# link = input("Enter the YouTube video URL: ")


videoDownload(longDuration_freeCodeCamp_YT_Video)
# videoInfo(jomaTech_YT_Video)
# playlistDownload(YT_playlist1)