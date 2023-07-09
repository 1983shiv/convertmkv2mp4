import sys
sys.path.append("D:\\movies\\")


from moviepy.editor import VideoFileClip

def convert_mkv_to_mp4(input_file, output_file):
    video = VideoFileClip(input_file)
    video.write_videofile(output_file, codec="libx264", audio_codec="aac")

# Example usage
input_file_path = "D:\\movies\\f.mkv"
output_file_path = "f.mp4"
convert_mkv_to_mp4(input_file_path, output_file_path)

