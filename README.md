# AI-dubbing-translator
You can dub or translate your video with AI voices provided by Open AI
### Tutorial
### Setting
1. Follow Open AI quick guide: [Open AI doc](https://platform.openai.com/docs/quickstart?context=python)
3. Get Open AI API key
4. Charge API fee
5. Install other Python libraries if needed(e.g. MoviePy)
### How to use
1. Extract audio file from your video by [Audacity](https://www.audacityteam.org/) or other programs
1. vts.py
   * Open vts.py
   * Replace `client = OpenAI(api_key='sk-wdasdfsdfsdTkd')  # Replace YOUR_API_KEY with your actual API key` with your Open AI API key.
   * Replace `with open("PXL_20240321_220342763.mp3", "rb") as audio_file:` to your audio file path.
   * Run vts.py
2. split_txt.py
   * Run split_txt.py
3. tts.py
   * Open tts.py
   * Replace `client = OpenAI(api_key='sk-wdasdfsdfsdTkd')  # Replace YOUR_API_KEY with your actual API key` with your Open AI API key.
   * Replace `voice="onyx",` if you want to change AI voice. [Open AI doc](https://platform.openai.com/docs/guides/text-to-speech)
   * Run tts.py
5. dub.py
   * Open dub.py
   * Replace `video_path = 'PXL_20240321_220342763.mp4'` with your video path.
