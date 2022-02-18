#Основная цель данного бота - оттачивание навыков создания ботов и попытка упрощения и улучшения кода
#Подключение необходимых модулей
import datetime
import requests
import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint


# API-ключ, созданный ранее в сообществе
token = token

# Авторизация "Вконтакте" как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)


#Функция отправки сообщения пользователю
def write_msg(user_id, message,random_id):
    vk.method('messages.send', {'user_id': user_id, 'message': message,"random_id":random_id})

#Функция отправки вложения пользователю
def send_attach(user_id, attachment, random_id):
    vk.method('messages.send', {'user_id': user_id, 'attachment': attachment, 'random_id': random_id})


# Основной цикл
for event in longpoll.listen():
    random_id = vk_api.utils.get_random_id()
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
        #Сообщение от пользователя
            request = event.text.lower()
            user_id = event.user_id
            # Функционал бота
            if request == "монетка":
                write_msg(user_id, coin_flip(), random_id)
            elif request=='гимн':
                send_attach(user_id,"audio169491161_456239562",random_id)
                random_id = vk_api.utils.get_random_id()
                send_attach(user_id,"doc268609423_543406590",random_id)
            elif request=='put_in':
                send_attach(user_id,"photo-193842359_457239046",random_id)
            elif request=='area51':
                send_attach(user_id,'photo-193842359_457239045',random_id)
            elif request=='k':
                send_attach(user_id,'doc268609423_574090399',random_id)
            elif request=='v':
                send_attach(user_id,'doc268609423_574090438',random_id)
            else:
                write_msg(user_id,'Ошибка ввода',random_id)
