from moviepy.editor import ImageClip, AudioFileClip

def generateVideo(player_name):

    image_file = f"{player_name.replace(' ', '_')}.jpg"
    audio_file = f"{player_name.replace(' ', '_')}.mp3"
    output_file = f"{player_name.replace(' ', '_')}.mp4"

    # Load image
    clip = ImageClip(image_file)

    # Load audio
    audio = AudioFileClip(audio_file)

    # Set the image duration to match the audio duration
    clip = clip.set_duration(audio.duration)

    # Set the audio to the clip
    clip = clip.set_audio(audio)

    # Optional: set FPS to 1 (static image)
    clip.write_videofile(output_file, fps=1, audio_codec='aac')

    print(f"✅ Video saved as: {output_file}")
    return output_file