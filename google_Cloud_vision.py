import io
import os
from google.cloud import vision

def non_ascii(text):
    return ''.join(i if ord(i)<128 and i.isalnum() else '' for i in text]).strip()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'apikey.json'


# The name of the image file to annotate (Change the line below 'image_path.jpg' ******)
path = os.path.join(os.path.dirname(__file__), '3.jpg') # Your image path from current directory 

client = vision.ImageAnnotatorClient()

with io.open(path, 'rb') as image_file:
    content = image_file.read()
image = vision.types.Image(content=content)
response = client.text_detection(image=image)

texts = response.text_annotations

full_text = non_ascii_remove(response.full_text_annotations)
print('Full Text:', full_text)

