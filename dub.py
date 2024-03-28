from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_audioclips
import os

# Paths setup
video_path = 'PXL_20240321_220342763.mp4'
voice_segments_dir = '/'
output_path = 'dubbed_video.mp4'

# Load the original video
video = VideoFileClip(video_path)
original_audio = video.audio

# Placeholder for the final audio clips list, starting with the original audio
final_audio_clips = [original_audio]

# Load each voice segment and prepare to splice them into the original audio
for filename in os.listdir(voice_segments_dir):
    if filename.endswith('.mp3'):
        _, _, start_str, end_str = filename.split('_')
        start, end = float(start_str), float(end_str[:-4])  # Parse start and end times
        
        # Load the voice segment as an audio clip
        voice_segment = AudioFileClip(os.path.join(voice_segments_dir, filename))
        
        # Create segments of the original audio to retain around the new audio
        before_segment = original_audio.subclip(0, start)
        after_segment = original_audio.subclip(end)
        
        # Create a list for this iteration to combine the before segment, voice segment, and after segment
        iteration_clips = [before_segment, voice_segment, after_segment]
        
        # Concatenate the clips for this iteration and update the final_audio_clips
        final_audio_clips = [concatenate_audioclips(iteration_clips)]

        # Update original_audio to the latest concatenated clip to ensure subsequent iterations
        # handle the newly formed audio structure
        original_audio = concatenate_audioclips(final_audio_clips)

# Ensure the final audio clip spans the entire length of the video
final_audio = final_audio_clips[0].set_duration(video.duration)

# Set the video's audio to the new, modified audio
video_with_replaced_audio = video.set_audio(final_audio)

# Export the modified video
video_with_replaced_audio.write_videofile(output_path, codec='libx264', audio_codec='aac')

print(f"Video with replaced audio has been saved to: {output_path}")