import os
from pathlib import Path
import datetime
from openai import OpenAI
client = OpenAI(api_key='sk-wdasdfsdfsdTkd')  # Replace YOUR_API_KEY with your actual API key

try:
    # Specify the directory containing the segment files
    segments_dir = Path(__file__).parent
    # Find all 'segment_x_x_x.txt' files in the directory
    segment_files = list(segments_dir.glob("segment_*.txt"))
    
    if not segment_files:
        print("No segment files found.")
        exit()

    for segment_file in segment_files:
        # Read the text from each segment file
        with open(segment_file, 'r', encoding='utf-8') as file:
            input_text = file.read()

        # OpenAI의 음성 생성 API 호출
        response = client.audio.speech.create(
            model="tts-1-hd",
            voice="onyx",
            input=input_text
        )

        # Output file has the same base name as the input file, but with .mp3 extension
        output_file_name = segment_file.stem + ".mp3"
        output_file_path = segments_dir / output_file_name

        # 생성된 음성 데이터를 파일로 저장
        response.stream_to_file(output_file_path)

        print(f"음성 파일이 {output_file_path}에 저장되었습니다.")

except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(f"에러가 발생했습니다: {e}")