
from google import genai
from google.genai import types
def germini(oai,sysconfi):
    conte = True
    client = genai.Client(api_key= oai)
    
    chat = client.chats.create(model="gemini-2.0-flash",config=types.GenerateContentConfig(system_instruction= f"se nesse pareteses tiver algo você tera quer ser ele/a ({sysconfi})ou pelo menos fingir como se fosse humano ou o animal que ta la,caso contrario ignore isso"))

    while conte == True:
        pessoa = input("Você:")
        if pessoa.strip().lower() == "exit":
            break
        response = chat.send_message(pessoa)
        print(response.text)
