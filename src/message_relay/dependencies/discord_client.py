"""discord-client.py"""

import discord
import logging
from .webhook import send_webhook


class DiscordClient(discord.Client):
    """A simple Discord client for message relay."""

    webhook_url = ""
    logger = None

    def __init__(self, intents=None, webhook_url=""):
        intents = intents or discord.Intents.default()
        intents.messages = True
        intents.message_content = True
        self.webhook_url = webhook_url
        self.logger = logging.getLogger("discord")
        super().__init__(intents=intents)


    async def on_ready(self):
        """Called when the bot is ready."""
        self.logger.info(f'Logged in as {self.user}')

    async def on_message(self, message):
        """Called when a message is received."""
        if message.author == self.user:
            self.logger.info("Ignoring message from self")
            return
        
        match message.content.split()[0]:
            case "!ping":
                self.logger.info(f"Received ping command from {message.author}")
                await message.channel.send("Pong!")
            case "!help":
                self.logger.info(f"Received help command from {message.author}")
                help_message = (
                    "Available commands:\n"
                    "!hello - Greet the bot\n"
                    "!ping - Get a pong response\n"
                    "!help - Show this help message"
                )
                await message.channel.send(help_message)
            case "!journal":
                self.logger.info(f"Received journal entry from {message.author}")
                content = message.content[len("!journal "):].strip()
                payload = {
                    "user": str(message.author),
                    "transcription": content
                }
                self.logger.info(f"Sending journal entry to webhook...")
                if self.webhook_url and self.webhook_url != "":
                    await send_webhook(
                        url=self.webhook_url,
                        payload=payload
                    )
                self.logger.info("Journal entry sent to webhook!")
            case "!idea":
                self.logger.info(f"Received idea entry from {message.author}")
