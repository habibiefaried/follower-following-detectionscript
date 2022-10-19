#!/usr/bin/python3
import os
import time
import sys
import random

from instagrapi import Client
from instagrapi.types import User
from instagrapi.mixins.challenge import ChallengeChoice


def get_code_from_anywhere(username):
    while True:
        code = input(f"Enter code (6 digits) for {username}: ").strip()
        if code and code.isdigit():
            return code
    return None

def change_password_handler(username):
    # Simple way to generate a random string
    chars = list("abcdefghijklmnopqrstuvwxyz1234567890!&£@#")
    password = "".join(random.sample(chars, 8))
    print("Your new password is: "+password)
    return password

def challenge_code_handler(username, choice):
    if choice == ChallengeChoice.SMS:
        return get_code_from_anywhere(username)
    elif choice == ChallengeChoice.EMAIL:
        return get_code_from_anywhere(username)
    return False

if (sys.argv[3] == '0'):
    print("Input is wrong, aborting...")
    sys.exit(0)

if (len(sys.argv) != 5):
    print("Usage: ./main.py <username> <password> <target> <2fa code>")
    sys.exit(0)

start_time = time.time()
cl = Client()
cl.challenge_code_handler = challenge_code_handler
cl.change_password_handler = change_password_handler
cl.login(username=sys.argv[1], password=sys.argv[2], verification_code=sys.argv[4])

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
