from ChidoriDiscordClient import ChidoriDiscordBot
import discord
import asyncio
from dotenv import load_dotenv
import os


load_dotenv()
# --- Discord Information ---
DISCORD_TOKEN: str = str(os.getenv("SECRET_KEY"))

async def get_discord_ids(discord_client: ChidoriDiscordBot, discord_message: discord.Message) -> None:
    args = (discord_message.content.split(" "))[1:]
    server = discord_message.guild
    if server == None:
        print(f"Command in question: {discord_message.content.split(" ")[0]}\nError: Could not find server ID from some reason")
    else:
        members_message = ""
        async for member in server.fetch_members():
            members_message += f"{member.display_name}: {member.id}\n"
        channel = discord_message.channel
        await channel.send(members_message)


async def testing_command_handler(discord_client: ChidoriDiscordBot, discord_message: discord.Message) -> None:
    args = (discord_message.content.split(" "))[1:]
    print(args)
    channel_id = discord_message.channel
    await channel_id.send(f"{args}")

async def send_dm_to_person(discord_client: ChidoriDiscordBot, discord_message: discord.Message) -> None:
    args = (discord_message.content.split(" "))[1:]
    print(args)
    discord_user = discord_client.get_user(int(args[0]))
    message = "".join(f"{word} " for word in args[1:])
    if discord_user != None:
        try:
            await discord_user.send(message)
        except Exception as e:
            print(e)
    else:
        print("eat shit")
    


def main():
    intents = discord.Intents.default()
    intents.message_content = True

    discord_client = ChidoriDiscordBot(intents=discord.Intents.all())

    # -- Initialize --
    guild_id = str(os.getenv("GUILD_ID"))
    discord_client.add_server_id(int(guild_id))

    # -- Commands --
    discord_client.add_command("test", testing_command_handler)
    discord_client.add_command("members", get_discord_ids)
    discord_client.add_command("message", send_dm_to_person)
    discord_client.run(DISCORD_TOKEN)


if __name__ == "__main__":
    print(DISCORD_TOKEN)
    main()
