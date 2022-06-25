from instagrapi import Client
from instagrapi.types import User
import os
import time
import sys

def change_password_handler(username):
    # Simple way to generate a random string
    chars = list("abcdefghijklmnopqrstuvwxyz1234567890!&£@#")
    password = "".join(random.sample(chars, 8))
    return password

if (sys.argv[3] == '0'):
    print("Input is wrong, aborting...")
    sys.exit(0)

start_time = time.time()
cl = Client()
cl.change_password_handler = change_password_handler
cl.login(sys.argv[1], sys.argv[2])

followers = cl.user_followers(int(sys.argv[3]))
following = cl.user_following(int(sys.argv[3]))

print("========================================================")
print("You follow this user but they are not following you")
print("========================================================")
print("")

for f in following:
        if f not in followers:
                print(following[f].username+"-"+following[f].full_name)

print("========================================================")
print("They are following you but you are not following them")
print("========================================================")
print("")

for f2 in followers:
        if (f2 not in following):
                print(followers[f2].username+"-"+followers[f2].full_name)

print("========================================================")
print("[REMINDER] You need to double check since this is using unofficial library")
print("--- %s seconds ---" % (time.time() - start_time))
print("========================================================")
