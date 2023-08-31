import discord

class DiscordNotifier:
    def __init__(self, token, channel_id):
        self.token = token
        self.channel_id = channel_id
        self.client = discord.Client()

    async def send_notification(self, message):
        @self.client.event
        async def on_ready():
            channel = self.client.get_channel(self.channel_id)
            await channel.send(message)
            await self.client.close()

        self.client.run(self.token)

# Example usage
if __name__ == "__main__":
    # Replace with your actual Discord bot token and channel ID
    DISCORD_BOT_TOKEN = "YOUR_DISCORD_BOT_TOKEN"
    CHANNEL_ID = 1234567890  # Replace with your Discord channel ID

    notifier = DiscordNotifier(DISCORD_BOT_TOKEN, CHANNEL_ID)
    notifier.send_notification("Arbitrage opportunity detected!")
