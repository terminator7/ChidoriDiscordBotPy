from ChidoriDiscordClient import ChidoriDiscordBot
import discord
import asyncio
from dotenv import load_dotenv
import os


load_dotenv()
# --- Discord Information ---
DISCORD_TOKEN: str = str(os.getenv("SECRET_KEY"))

def testing_command_handler(discord_message: discord.Message) -> None:
    args = (discord_message.content.split(" "))[1:]
    print(args)
    channel_id = discord_message.channel
    asyncio.create_task(channel_id.send(f"{args}"))


def main():
    intents = discord.Intents.default()
    intents.message_content = True

    discord_client = ChidoriDiscordBot(intents=discord.Intents.all())

    discord_client.add_command("test", testing_command_handler)

    discord_client.run(DISCORD_TOKEN)


if __name__ == "__main__":
    print(DISCORD_TOKEN)
    main()
