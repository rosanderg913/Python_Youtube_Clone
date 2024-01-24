from flask import Flask, request, jsonify
import os
from moviepy.editor import VideoFileClip
import moviepy
from moviepy.video.io.ffmpeg_tools import ffmpeg_resize


app = Flask(__name__)


@app.post('/process-video')
def process_video():
    # Get path of the input & output video file from the request body
    data = request.get_json()
    input_file_path = data['input_file_path']
    output_file_path = data['output_file_path']

    # Check if the file paths are defined
    if not input_file_path:
        return jsonify({'error': 'input_file_path not defined'}), 400
    if not output_file_path:
        return jsonify({'error': 'output_file_path not defined'}), 400
    
    # Video processing logic
    try:
        ffmpeg_resize(input_file_path, output_file_path, size=(1280, 720))
        return jsonify({'success': 'Video processed successfully'}), 200
    except Exception as e:
        print(f'An error occured: {e}')
        return jsonify({'Internal Server Error': str(e)}), 500
    
@app.route('/')
def index():
    return 'Hello World!', 200
    

port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(port=port)

