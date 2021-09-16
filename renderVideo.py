from moviepy.editor import VideoFileClip,concatenate_videoclips 
from listvideos import videoslist,pathOfVideo
import os

def renderFinalVideo():
  # for index,video in enumerate(videoslist):
  #   videoNames["clip{}".format(index)]= VideoFileClip("/home/ambush/test/"+video)

  videoNames= {f"clip{index}":VideoFileClip(pathOfVideo+video) for index,video in enumerate(videoslist)}

  video_file_clips=list(videoNames.values())
  final_video = concatenate_videoclips(video_file_clips)


  fileName= input("Enter location to save the video with name for your video(only .mp4):-")

  if fileName.endswith(".mp4"):    
    final_video.write_videofile(fileName)
   
  else:
    print("Sorry the extension must be .mp4")

