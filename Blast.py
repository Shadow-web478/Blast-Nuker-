import discord
from discord.ext import commands
import logging

# Configure logging for better output management
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to securely load the token and prefix
def get_token_and_prefix():
    token = input("Enter your bot token: ")
    prefix = input("Enter your bot prefix: ")
    return token, prefix

# Display banner function
def display_banner():
    banner_text = """
  ____  _           _     _   _       _             
 |  _ \\| |         | |   | \\ | |     | |            
 | |_) | | __ _ ___| |_  |  \\| |_   _| | _____ _ __ 
 |  _ <| |/ _` / __| __| | . ` | | | | |/ / _ \\ '__|
 | |_) | | (_| \\__ \\ |_  | |\\  | |_| |   <  __/ |   
 |____/|_|\\__,_|___/\\__| |_| \\_|\\__,_|_|\_\\___|_|   
                                                    
                                                    
"""
    logger.info(banner_text)

# Bot setup
def main():
    # Securely load token and prefix
    token, prefix = get_token_and_prefix()

    # Set up intents
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    # Initialize bot
    bot = commands.Bot(command_prefix=prefix, intents=intents)
    bot.remove_command("help")

    # Event for when the bot is ready
    @bot.event
    async def on_ready():
        logger.info(f'Logged in as {bot.user.name}')
        logger.info(f'Bot ID: {bot.user.id}')
        display_banner()

    # Command to show available options
    @bot.command()
    async def options(ctx):
        command_list = """
        Here are the available commands:
        1 - Ban all members
        2 - Delete Channels
        3 - Delete Roles
        4 - Kick Members
        5 - Prune Members
        6 - Create Channels
        7 - Spam All Channels
        8 - Create Roles
        9 - Delete Roles
        10 - Rename Channels
        11 - Rename Guild
        12 - Rename Roles
        13 - Credits
        14 - Exit
        """
        
        # Send the options list
        await ctx.send(command_list)
        await ctx.send("Please type the number corresponding to your action:")

    # Command to process the number-based input
    @bot.command()
    async def execute(ctx, number: int):
        # Map numbers to corresponding functions
        if number == 1:
            await ban_all(ctx)
        elif number == 2:
            await delete_channels(ctx)
        elif number == 3:
            await delete_roles(ctx)
        elif number == 4:
            await kick_members(ctx)
        elif number == 5:
            await prune_members(ctx)
        elif number == 6:
            await create_channels(ctx)
        elif number == 7:
            await spam_channels(ctx)
        elif number == 8:
            await create_roles(ctx)
        elif number == 9:
            await delete_roles(ctx)
        elif number == 10:
            await rename_channels(ctx)
        elif number == 11:
            await rename_guild(ctx)
        elif number == 12:
            await rename_roles(ctx)
        elif number == 13:
            await credits(ctx)
        elif number == 14:
            await exit_bot(ctx)
        else:
            await ctx.send("Invalid option. Please type a valid number between 1 and 14.")

    # Placeholder function for banning all members
    async def ban_all(ctx):
        await ctx.send("Ban all members functionality triggered.")

    # Placeholder function for deleting channels
    async def delete_channels(ctx):
        await ctx.send("Delete channels functionality triggered.")

    # Placeholder function for deleting roles
    async def delete_roles(ctx):
        await ctx.send("Delete roles functionality triggered.")

    # Placeholder function for kicking members
    async def kick_members(ctx):
        await ctx.send("Kick members functionality triggered.")

    # Placeholder function for pruning members
    async def prune_members(ctx):
        await ctx.send("Prune members functionality triggered.")

    # Placeholder function for creating channels
    async def create_channels(ctx):
        await ctx.send("Create channels functionality triggered.")

    # Placeholder function for creating roles
    async def create_roles(ctx):
        await ctx.send("Create roles functionality triggered.")

    # Placeholder function for deleting roles
    async def delete_roles(ctx):
        await ctx.send("Delete roles functionality triggered.")

    # Placeholder function for renaming channels
    async def rename_channels(ctx):
        await ctx.send("Rename channels functionality triggered.")

    # Placeholder function for renaming the guild
    async def rename_guild(ctx):
        await ctx.send("Rename guild functionality triggered.")

    # Placeholder function for renaming roles
    async def rename_roles(ctx):
        await ctx.send("Rename roles functionality triggered.")

    # Placeholder function for displaying credits
    async def credits(ctx):
        await ctx.send("Credits functionality triggered.")

    # Placeholder function to exit the bot
    async def exit_bot(ctx):
        await ctx.send("Exiting bot.")
        await bot.close()

    # Function to spam all channels with a message
    async def spam_channels(ctx):
        # The message to send in all channels
        spam_message = "Aditya papa aaye or moot diya server pee"

        # Loop through all text channels in the guild
        for channel in ctx.guild.text_channels:
            try:
                # Send the message to the channel
                await channel.send(spam_message)
            except discord.Forbidden:
                # Handle cases where the bot does not have permission to send messages in the channel
                logger.warning(f"Cannot send message to {channel.name}, missing permissions.")
            except discord.HTTPException as e:
                # Handle any HTTP exceptions
                logger.error(f"Failed to send message to {channel.name}: {e}")

        await ctx.send(f"Spammed all channels with the message: '{spam_message}'")

    # Run the bot
    bot.run(token)

# Run the bot setup
if __name__ == "__main__":
    main()