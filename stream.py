import os


# os.system("ffmpeg -re -i bbb_original.mp4 -vcodec copy -loop -1 -c:a aac -b:a 160k -ar 44100 -strict -2 -f flv rtmp:192.168.1.132/live/bbb")
os.system("ffmpeg -i bbb_original.mp4 -v 0 -vcodec mpeg4 -f mpegts udp://127.0.0.1:23000")
os.system("ffplay udp://127.0.0.1:23000")