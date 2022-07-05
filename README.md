# Discord-Bot-Fortune-Cookie
Python code to run a discord bot that parses fortune cookie phrases from a text file and sends one into the discord channel when a user types "!cookie"

To set up, you must create a bot on the discord developer portal. You can then find a token in the bot tab (keep this token to yourself). Copy and paste this token into the .env file. bot.py can then read this and connect to the bot. 
Then proceed to the OAuth2 tab on the discord developer portal, under scopes tick bot and then under permissions, allow this bot to view channels and send messages. You can then copy the url at the bottom of the scopes section, copy and paste the url into your browser, and you should come to the option to add the bot to any server where you have the manage channels permission.
