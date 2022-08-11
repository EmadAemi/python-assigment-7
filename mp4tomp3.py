from moviepy import editor
video = editor.VideoFileClip('test.mp4')
video.audio.write_audiofile('test.mp3')