import google.generativeai as ai
ai.configure("GEMINI-API-KEY")

model = ai.GenerativeModel("gemini-2.5-flash") 
chat = model.start_chat()

while True:
    message = input('you: ')
    if message.lower() == 'bye':
        print('chatbot: Goodbye!')
        break
    response = chat.send_message(message)
    print('chatbot:', response.text)