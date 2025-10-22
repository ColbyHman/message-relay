"""main.py"""

from message_relay.dependencies.discord_client import DiscordClient
import os

def main():
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise ValueError("DISCORD_TOKEN environment variable not set")

    client = DiscordClient()
    client.run(token)  # Replace with your bot token

if __name__ == "__main__":
    main()