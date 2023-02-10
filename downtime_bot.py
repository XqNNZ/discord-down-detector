import discord
import requests
import time
import asyncio

client = discord.Client()

CHANNEL_ID = ABC123 # Replace this with the ID of the Discord channel you wish to monitor.
WEBHOOK_URL = "ABC123" # Replace this with the URL of the webhook

last_message_timestamp = time.time()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    print("Checking the channel")
    print("")

async def check_inactivity(): #Checks to see if the channel has been inactive for more than 10 minutes, checking every 60 seconds
    global last_message_timestamp
    while True:
        current_timestamp = time.time()
        if (current_timestamp - last_message_timestamp) > 600: #Every 10 minutes
            payload = {"content": "This channel has been inactive for more than 10 minutes. Its a bit too quiet in here! <@ABC123> & <@ABC123>"} #Sending message to alerting channel
            requests.post(WEBHOOK_URL, json=payload)
            print("Downtime detected, alerting!")
            await asyncio.sleep(540) #Making the bot wait 540 seconds before resending downtime message
        await asyncio.sleep(60)

@client.event #Updates last_message_timestamp whenever a new message is received
async def on_message(message):
    global last_message_timestamp
    if message.channel.id == CHANNEL_ID:
        last_message_timestamp = time.time()
        print("")
        print("Message received at: ", last_message_timestamp) #Sends message to console

client.loop.create_task(check_inactivity())

client.run("ABC123") #Bot client token