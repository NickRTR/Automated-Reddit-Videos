import moviepy.editor as movie
import glob
import random
import math

audioComments = glob.glob("./audio/comment-*.mp3")
backgroundVideos = glob.glob("./background/*.mp4")

questionAudio = f"./audio/question.mp3"
outputVideo = f"./output/output.mp4"

def joinQuestionWithComments():
    # join all comments
    commentClips = [movie.AudioFileClip(c) for c in audioComments]
    comments = movie.concatenate_audioclips(commentClips)

    # join question with comments
    questionClip = movie.AudioFileClip(questionAudio)
    return movie.concatenate_audioclips([questionClip, comments])


def joinAudioWithVideo(audioClip):
    videoClip = movie.VideoFileClip(random.choice(backgroundVideos))
    # change resolution to 1080x1920
    videoClip = videoClip.resize((1080, 1920))

    return videoClip.set_audio(audioClip)

def createVideo():
    audio = joinQuestionWithComments()
    finalVideo = joinAudioWithVideo(audio)
    # Cut video to match audio
    finalVideo = finalVideo.subclip(0, math.ceil(audio.duration))
    finalVideo.write_videofile(outputVideo, fps=30)