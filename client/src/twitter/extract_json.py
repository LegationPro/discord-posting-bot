import json

def get_json_data(json_data):
    
    if type(json_data) == "str":
        json_data = json.loads(json_data)
    
    sorted_data = []
        
    for status in json_data["statuses"]:
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
