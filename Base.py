from dotenv import load_dotenv
import os

dotenv_path = r"D:\Project\Automating Tweeting\apikeys.env"
load_dotenv(dotenv_path=dotenv_path)

twitter_api_key = os.getenv("TWITTER_API_KEY")

print("Twitter API Key:", twitter_api_key)

print(2+5)
#new line