import google.generativeai as genai
import PIL.Image

img = PIL.Image.open('image.jpg')

genai.configure(api_key='AIzaSyART9LFuIun8-XAl-ehwt5BDTAluaEVh-s')

model = genai.GenerativeModel('gemini-pro-vision')

response = model.generate_content(["what is the total calorie count?", img])

print(response.text)