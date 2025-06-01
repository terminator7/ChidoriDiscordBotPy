import discord
from typing import Callable, Any
from enum import Enum


class ChidoriDiscordBot(discord.Client):
    def __init__(self, **options) -> None:
        super().__init__(**options)
        self.command_symbol = "!"
        self.command_list = {}

    def add_command(self, command : str, commandCallback : Callable[[discord.Message], None]) -> None:
        self.command_list[command] = commandCallback



    async def setup_hook(self):
        pass

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}")

    async def on_message(self, message: discord.Message) -> None:
       if message.content[0] == self.command_symbol:
        message_array = message.content[1:].split(" ")
        if message_array[0] in self.command_list.keys():
            command_callable = self.command_list[message_array[0]]
            command_callable(message)
        else:    
            print("error command was not found")
           

