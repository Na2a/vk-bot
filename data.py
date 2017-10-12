"""
Filename: data.py
Description: This file contains all data, including constant variables, auto-replies and etc.
"""

CHAT_ID = 253401848 # pm
#CHAT_ID = 24 + 2000000000 # chat

APP_ID = 6144282
LOGIN = 'nazarbek.altybay@gmail.com'

PASSWORD = str(input("passwd: "))

# auto-reply
AUTO_REPLY = {
  '' : 'Something went wrong!\nType @bot help to get list of commands.',
  'about' : 'Hello! I am simple VK Bot.\nType @bot help to get list of commands.',
  'help' : 'List of commands:\n@bot help - list of commands\n@bot about - information about me\n@bot getpath A B - gets path between user A and B checking 6 handshakes theory'
}
