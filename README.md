# Discord-Bot

A Discord bot that provides inspirational quotes and has roasting capabilities.

## Features

- **Inspirational Quotes**: Get a random inspirational quote by typing `&inspire` or `&Inspire` in the chat.
- **Roasting**: Get a random roast by typing `&roast` in the chat.
- **Add New Roasts**: Add a new roast to the database by typing `&new <roast_message>` in the chat.
- **Delete Roasts**: Delete a roast from the database by typing `&del <index>` in the chat.
- **List Roasts**: List all available roasts by typing `&list` in the chat.
- **Custom Roasts**: Get a custom roast by typing `!roast <username>` in the chat.

## Setup

1. Create a Discord bot and get a token from the Discord Developer Portal.
2. Create a file named `.env` in the root of the project and add the token as `TOKEN=<your_token_here>`.
3. Install the required packages by running `pip install -r requirements.txt`.
4. Run the bot by executing `python bot.py`.

## Contributing

Contributions are welcome! If you'd like to add new features or fix bugs, please submit a pull request.
