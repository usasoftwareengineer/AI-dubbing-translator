import json

# Load the JSON data from the file
with open('translation_output.json', 'r') as file:
    data = json.load(file)

# Check if 'model_extra' and 'segments' exist in the data
if 'model_extra' in data and 'segments' in data['model_extra']:
    # Iterate over each segment
    for index, segment in enumerate(data['model_extra']['segments'], start=1):
        # Extract the start, end, and text values
        start = segment['start']
        end = segment['end']
        text = segment['text']
        
        # Define the filename using the specified format
        filename = f"segment_{index}_{start}_{end}.txt"
        
        # Write the text into the file
        with open(filename, 'w') as out_file:
            out_file.write(text)

        print(f"Written '{text}' to {filename}")