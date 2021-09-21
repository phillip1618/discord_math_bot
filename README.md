# About

`math_discord_bot` is a Discord bot that currently lives in the Discord server of Twitch streamer, phillip1618. The bot has one simple function, which is to tell a joke, but more features may be included in the future!

## Usage

In any available text channel, simply type in `$mathjoke` and the Math Bot will return a randomly generated joke.

## Set-up

The Discord Bot has been set up within an AWS EC2 instance (I use 'Amazon Linux 2 AMI') in order for the bot to be run on the cloud. Once the instance and connection to the instance has been set up, here are some further set up instructions:

1. Install python using `sudo yum install python3`
2. Install pip using `sudo yum install pip`
3. Install git using `sudo yum install git`
4. Clone the repo, and a new directory 'discord_math_bot` will appear
5. Install required python packages using `pip3 install -r discord_math_bot/requirements.txt`
6. Run the application as a background service using `python3 main.py &`

Sidenote: If there are any encoding issues when opening the text file 'math_jokes.txt' in line 20 of 'main.py', the parameter `encoding='mbcs'` may have to be deleted

## Future implementations

- Give the bot calculation capabilities
- Allow for Questions/Answer user interaction with bot
