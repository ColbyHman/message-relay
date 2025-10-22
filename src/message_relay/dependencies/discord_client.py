"""discord-client.py"""

import discord
import logging

logger = logging.getLogger(__name__)

class DiscordClient(discord.Client):
    """A simple Discord client for message relay."""

    def __init__(self, intents=None):
        intents = intents or discord.Intents.default()
        intents.messages = True
        intents.message_content = True
        super().__init__(intents=intents)


    async def on_ready(self):
        """Called when the bot is ready."""
        logger.info(f'Logged in as {self.user}')

    async def on_message(self, message):
        """Called when a message is received."""
        if message.author == self.user:
            logger.info("Ignoring message from self")
            return

        if message.content.startswith("!hello"):
            logger.info(f"Received hello command from {message.author}")
            await message.channel.send(f"Hello, {message.author}!")
