import os
import subprocess
import time

start_time = time.perf_counter()

media_dir = "media/"
file_name = "top10beaches"
ext = ".mp4"

# process = subprocess.Popen(f"ffmpeg -i {media_dir + file_name + ext} -vcodec libx265 -crf 30 -preset ultrafast {media_dir + file_name + '_output' + ext}", shell=True)
process = subprocess.Popen(f"ffmpeg -i {media_dir + file_name + ext} -c:v libx264 -preset ultrafast -crf 51 -c:a aac -b:a 32k {media_dir + file_name + '_output' + ext}", shell=True)
process.communicate()

end_time = time.perf_counter()

print(f"Total time: {end_time - start_time} seconds")
