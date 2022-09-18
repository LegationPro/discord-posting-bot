import os
import discord
# import asyncio
import json

from dotenv import load_dotenv
from twitter import api

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def get_json_data(json_data):
    sorted_data = []
    statuses = json_data["statuses"]
        
    for status in statuses:
        created_at = status["created_at"]
        hashtags = status["entities"]["hashtags"]
        urls = status["entities"]["urls"]
        text = status["text"]
        user = status["user"]
        email = user["email"]
        
        status_wrapper = {
            "created_at": created_at,
            "hashtags": hashtags,
            "urls": urls,
            "text": text,
            "email": email,
        }
        
        sorted_data.append({"status": status_wrapper})        
    return sorted_data



tweet_data = api.get_tweets("programming")
tweet_data = json.loads(tweet_data)
returned_data = get_json_data(tweet_data)

@client.event
async def on_ready():
    tweet_data = api.get_tweets("programming")
    tweet_data = json.loads(tweet_data)
    parsed_data = get_json_data(tweet_data)
    data = []
    
    channel = client.get_channel(1020801576987791512)
    
    for statusObject in parsed_data:
       parsed_urls = []
       status = statusObject["status"]
       created_at = status["created_at"]
       hashtags = status["hashtags"]
       urls = status["urls"]
       text = status["text"]
       email = status["email"]
       
       for obj in urls:
           if obj["url"] != None or obj["url"] == "":
               parsed_urls.append(obj["url"])
       
       data.append([{
           "created_at": created_at,
           "hashtags": hashtags,
           "urls": parsed_urls,
           "text": text,
           "email": email,
       }])
       
       for status in data[0]:
           if len(hashtags) == 0:
               status["hashtags"] = None
               
        
    for arr in data:
        for poster_data in arr:
            created_at = poster_data["created_at"]
            hashtags = poster_data["hashtags"]
            urls = poster_data["urls"]
            text = poster_data["text"]
            email = poster_data["email"]
                        
            format_created_at = f"This tweet was Created at {created_at} \n \n"
            format_hashtags = f"This tweet has these hashtags: {hashtags} \n \n"
            format_urls = f"This tweet has the following urls: {urls} \n \n"
            format_body = f"This tweet has the following body: {text} \n \n"
            format_email = f"This tweet has the following email: {email}"
            
            await channel.send(
                format_created_at + format_hashtags + format_urls + format_body + format_email
            )




if __name__ == '__main__':
    client.run(os.getenv("token"))