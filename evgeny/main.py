# """Пример работы с чатом через gigachain"""
# from langchain.schema import HumanMessage, SystemMessage
# from langchain.chat_models.gigachat import GigaChat

# # Авторизация в сервисе GigaChat
# chat = GigaChat(credentials='Yjg4MTQzMmUtNDAwMS00NDk0LThjOGUtNmU5ZWQ2YzQ4NDQ2OmQ4MWMxZGZiLTFmNGYtNDk5NS05OGQzLTBiMzYyYWJmNjk3OA==', verify_ssl_certs=False,scope='GIGACHAT_API_CORP')

# messages = [
#     SystemMessage(
#         content="Ты эмпатичный бот-психолог, который помогает пользователю решить его проблемы."
#     )
# ]

# while(True):
#     # Ввод пользователя
#     user_input = input("User: ")
#     messages.append(HumanMessage(content=user_input))
#     res = chat(messages)
#     messages.append(res)
#     # Ответ сервиса
#     print("Bot: ", res.content)


from os import link
from parser import parser, parser_links

links = parser_links("Math")

print(links)

print(parser(links[3]))