import google.generativeai as genai

genai.configure(api_key='AIzaSyART9LFuIun8-XAl-ehwt5BDTAluaEVh-s')

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("who are BTS? in two lines.")

print(response.text)