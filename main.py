""" 
Filename: main.py
Description: This is the core file
"""

import data
import api
import pathfinder

def react(arr):
  command = 'about'
  
  if len(arr) > 1:
    command = arr[1]
  
  if command in data.AUTO_REPLY:
    return data.AUTO_REPLY[command]
  
  if command == 'getpath':
    if len(arr) != 4:
      return 'Invalid number of arguments.'
    try:
      userA = api.get_user(arr[2])
      userB = api.get_user(arr[3])
    except:
      return 'Wrong id! Use numeric id or nickname (e.g. 1, id1 or durov)'

    return pathfinder.get_path(userA['id'], userB['id'])

  return data.AUTO_REPLY['']

if __name__ == '__main__':
  last_message = 0
  while True:
    message = api.get_last_message()
    body = message['body'].split()
    if message == last_message:
      continue
    last_message = message
    if body[0] == '@bot':
      api.send_message(react(body))