import json
import os

import interactions

with open("./config.json") as config:
    token = json.load(config)["token"]

Tsumugi = interactions.Client(
    token = token
)

@Tsumugi.event
async def on_ready():
    print("Tsumugi is ready!")

for filename in os.listdir("./src"):
    if filename.endswith(".py"):
        print(f"Loading extension: {filename}")
        Tsumugi.load(f"src.{filename[:-3]}")

Tsumugi.start()