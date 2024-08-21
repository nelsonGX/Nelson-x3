import os
import dotenv

dotenv.load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
claude_key = os.getenv("CLAUDE_API_KEY")
discord_token = os.getenv("DISCORD_TOKEN")