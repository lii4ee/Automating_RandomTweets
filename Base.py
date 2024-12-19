from dotenv import load_dotenv
import os

# Load environment variables from the .env file
dotenv_path = r"D:\Project\Automating Tweeting\apikeys.env"
load_dotenv(dotenv_path=dotenv_path)

# Access the values of the environment variables
twitter_api_key = os.getenv("TWITTER_API_KEY")

print("Twitter API Key:", twitter_api_key)

#will git pull work
