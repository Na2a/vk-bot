""" 
Filename: main.py
Description: Module to find paths between two VK users by implementing BFS

Very slow and naive implementation
Needs to be completely rewritten
"""

import api

class Queue:
  def __init__(self):
    self.items = []
  def empty(self):
    return len(self.items) == 0
  def push(self, x):
    self.items.insert(0, x)
  def front(self):
    return self.items[-1]
  def pop(self):
    return self.items.pop()
  def size(self):
    return len(self.items)
  def clear(self):
    self.items = []

def restore(path):
  if len(path) > 1:
    res = "Path of " + str(len(path) - 1) + " handshakes found:\n"
  else:
    res = "Of course person knows himself!\n"
    
  afterparty = False
  for id in path:
    if afterparty:
      res = res + " >> "
    afterparty = True
    while True:
      try:
        who = api.get_user(str(id))
        break
      except:
        continue
    res = res + "@id" + str(id) + "(" + who['first_name'] + ")"
  return res

def get_path(a, b):
  print("getting path between " + str(a) + " and " + str(b))
  if a == b:
    return restore([a])

  q = Queue()
  parent = {}
  distance = {}
  
  parent[a] = a
  distance[a] = 0
  q.push(a)

  q_back = Queue()
  parent_back = {}
  distance_back = {}
  
  parent_back[b] = b
  distance_back[b] = 0
  q_back.push(b)

  while True:
    if q.empty() and q_back.empty():
      break

    if not q.empty():
      user = q.pop()
      #print("user " + str(user) + " " + str(distance[user]))
      if distance[user] == 2:
        continue
      friends = api.get_friendlist(user)
      #if distance[user] == 0:
      #  friends = friends[:50]
      for to in friends:
        if not to in parent:
          parent[to] = user
          distance[to] = distance[user] + 1
          q.push(to)
          if to in parent_back:
            x = to
            path = []
            path.append(x)
            while x != a:
              x = parent[x]
              path.append(x)

            y = to 
            path_back = []
            while y != b:
              y = parent_back[y]
              path_back.append(y)

            return restore(list(reversed(path)) + path_back)

    if not q_back.empty():
      user = q_back.pop()
      #print("user_back " + str(user) + " " + str(distance_back[user]))
      if distance_back[user] == 2:
        continue
      friends = api.get_friendlist(user)
      #if distance_back[user] == 0:
      #  friends = friends[:50]
      for to in friends:
        if not to in parent_back:
          parent_back[to] = user
          distance_back[to] = distance_back[user] + 1
          q_back.push(to)
          if to in parent:
            x = to
            path = []
            path.append(x)
            while x != a:
              x = parent[x]
              path.append(x)

            y = to 
            path_back = []
            while y != b:
              y = parent_back[y]
              path_back.append(y)

            return restore(list(reversed(path)) + path_back)

  return "Path hasn't been found."