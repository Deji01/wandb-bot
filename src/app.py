import json 
from pprint import pprint

with open("/workspaces/wandb-bot/src/chat_prompt.json") as f:
    data = json.load(f)

pprint(data["system_template"])