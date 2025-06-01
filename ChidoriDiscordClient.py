import discord
from typing import Callable, Any, Awaitable
from enum import Enum


class ChidoriDiscordBot(discord.Client):
    def __init__(self, **options,) -> None:
        super().__init__(**options)
        self.__command_symbol = "!"
        self.__command_list = {}
        self.__server_id = 0
        self.server = self.get_guild(0)

    def add_command(self, command : str, commandCallback : Callable[["ChidoriDiscordBot", discord.Message], Awaitable[None]]) -> None:
        self.__command_list[command] = commandCallback

    def add_server_id(self, server_id : int) -> None:
        self.__server_id = server_id

    async def setup_hook(self):
        pass

    async def on_ready(self) -> None:
        self.server = self.get_guild(self.__server_id)
        print(f"Logged in as {self.user}")

    async def on_message(self, message: discord.Message) -> None:
       if message.content[0] == self.__command_symbol:
        message_array = message.content[1:].split(" ")
        if message_array[0] in self.__command_list.keys():
            command_callable = self.__command_list[message_array[0]]
            await command_callable(self, message)
        else:    
            print("error command was not found")
           

