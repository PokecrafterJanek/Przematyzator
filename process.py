from pytube import YouTube
import os
import cv2
import extract_text

def download(video_url):
    output_folder = "files/temp/video"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    try:
        yt = YouTube(video_url)

        video_stream = yt.streams.get_highest_resolution()

        video_title = yt.title

        print(f"Downloading: {video_title}")
        video_stream.download(output_folder, filename='video.mp4')
        print("Download complete!")

    except Exception as e:
        print(f"Error: {e}")

    video_path = os.path.join(output_folder, 'video.mp4').replace("\\", "/")

    cut(video_path)


def cut(video_path):
    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)

    if cap.isOpened() == False:
        print("Your video doesn't work blud.")

    print(f"Video FPS: {fps}")
        
    interval_seconds = 10
    frame_interval = int(fps * interval_seconds)

    output_folder = "files/temp/pictures"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_count = 0

    if fps > 0:
        success = True

    else:
        success = False

    while success:
        success, frame = cap.read()

        if frame_count % frame_interval == 0 and success:
            frame_filename = f"frame_{int(frame_count // frame_interval)}.jpg"
            frame_path = os.path.join(output_folder, frame_filename)
            cv2.imwrite(frame_path, frame)

        frame_count += 1

    print("Frame extraction finished")

    cap.release()

    extract_text.extract()