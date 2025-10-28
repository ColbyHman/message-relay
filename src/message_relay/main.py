"""main.py"""

from message_relay.dependencies.discord_client import DiscordClient
import os

def main():
    token = os.getenv("DISCORD_TOKEN")
    webhook_url = os.getenv("WEBHOOK_URL", "")
    if not token:
        raise ValueError("DISCORD_TOKEN environment variable not set")

    client = DiscordClient(webhook_url=webhook_url)
    client.run(token)

if __name__ == "__main__":
    main()