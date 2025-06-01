import discord
from dotenv import load_dotenv
import os
from enum import Enum

load_dotenv()

# --- Discord Information ---
DISCORD_TOKEN: str = str(os.getenv("SECRET_KEY"))


# --- Overseer Stuff ---
class MyDiscordClient(discord.Client):
    def __init__(self, **options) -> None:
        super().__init__(**options)


    async def setup_hook(self):
        pass

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}")

    async def on_message(self, message: discord.Message) -> None:
       pass


def main():
    intents = discord.Intents.default()
    intents.message_content = True

    discord_client = MyDiscordClient(intents=discord.Intents.all())
    discord_client.run(DISCORD_TOKEN)


if __name__ == "__main__":
    print(DISCORD_TOKEN)
    main()
