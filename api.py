""" 
Filename: api.py
Description: This module has some methods to get and send information via VK API using vk_requests library
"""

import vk_requests as vk
import data

api = vk.create_api(app_id = data.APP_ID, login = data.LOGIN, password = data.PASSWORD, scope = 65535)

def get_last_message():
  while True:
    try:
      message = api.messages.getHistory(count = 1, peer_id = data.CHAT_ID)['items'][0]
      break
    except:
      continue
  return message

def send_message(message):
  print("sending message " + message)
  while True:
    try:
      api.messages.send(peer_id = data.CHAT_ID, message = message)
      break
    except:
      continue

def get_user(id):
  print("getting user " + id)
  return api.users.get(user_ids = id)[0]

def get_friendlist(id):
  #print("getting friendlist of " + str(id))
  try:
    return api.friends.get(user_id = id, order = 'random')['items']
  except:
    return []