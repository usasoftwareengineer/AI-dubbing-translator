import json
from openai import OpenAI

def custom_serializer(obj):
    """A generic serializer for objects with multiple attributes."""
    if hasattr(obj, "__dict__"):
        # Attempt to serialize attributes that are directly accessible
        obj_dict = {attr: getattr(obj, attr) for attr in dir(obj) if not attr.startswith("__") and not callable(getattr(obj, attr))}
        # Further processing for attributes that are not serializable
        for key, value in obj_dict.items():
            try:
                json.dumps(value)
            except TypeError:
                # Replace or process the non-serializable attributes here
                # For now, just converting to string as a fallback
                obj_dict[key] = str(value)
        return obj_dict
    # Fallback for any other types, replace or extend as necessary
    return str(obj)

# Initialize the OpenAI client with your API key
client = OpenAI(api_key='sk-wdasdfsdfsdTkd')  # Replace YOUR_API_KEY with your actual API key

# Open the audio file in binary read mode and create the translation
with open("PXL_20240321_220342763.mp3", "rb") as audio_file:
    translation = client.audio.translations.create(
        model="whisper-1", 
        file=audio_file,
        response_format="verbose_json"
    )

# Serialize the translation object, attempting to capture all fields
translation_dict = custom_serializer(translation)

# Serialize to JSON and print
translation_json = json.dumps(translation_dict, ensure_ascii=False, indent=4)
print(translation_json)

# Optionally, write to a file
with open("translation_output.json", "w", encoding='utf-8') as file:
    file.write(translation_json)