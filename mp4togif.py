from moviepy.editor import VideoFileClip
import sys
import os

def convert_mp4_to_gif(input_path, output_path=None, start_time=None, end_time=None, fps=10):
    # Load video clip
    clip = VideoFileClip(input_path)

    # Trim if start/end specified
    if start_time is not None or end_time is not None:
        clip = clip.subclip(start_time or 0, end_time or clip.duration)

    # Set output filename
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".gif"

    # Write GIF
    clip.write_gif(output_path, fps=fps)
    print(f"Saved GIF to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mp4_to_gif.py input.mp4 [output.gif] [start_time] [end_time]")
        sys.exit(1)

    input_mp4 = sys.argv[1]
    output_gif = sys.argv[2] if len(sys.argv) > 2 else None
    start = float(sys.argv[3]) if len(sys.argv) > 3 else None
    end = float(sys.argv[4]) if len(sys.argv) > 4 else None

    convert_mp4_to_gif(input_mp4, output_gif, start, end)
