import telebot
import requests

from github import Github



TELEGRAM_TOKEN = "5422270698:AAGNeLwbVipHPB_ZbZ8qKi3jo1GKTBxnBEA"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def load_last_update(message):

    # Extract the username and repository name from the text request we sent to the chat bot.
    _, user_name, repo_name = message.text.split()

    # Create an object to interact with the github.

    g = Github()

    # Upload the user by his/her name.
    try:
        user = g.get_user(user_name)
    except Exception as e:
        return None


    # Search for a repository by its name.
    target_repo = None
    for repo in user.get_repos():
        if repo.name == repo_name:
            target_repo = repo
            break

    # If we did not find a repository with that name.
    if target_repo is None:
        return None

    date = target_repo.updated_at

    return date.year, date.month, date.day


# Expect to receive a command in the following format: check <user name> <repository name>
def check_request(message):
    request = message.text.split()
    if len(request) == 3 and request[0] == 'check':
        return True
    return False

@bot.message_handler(func=check_request)
def check_repo_update(message):

    # Receiving data from the server
    updated_date = load_last_update(message)

    if updated_date is None:
        response = "User or repo not found!"
    else:
        response = "Last updated: %s : %s : %s" % updated_date

    bot.send_message(message.chat.id, response)


# Expect to receive a command in the following format:show <user name>
def check_show_request(message):
    request = message.text.split()
    if len(request) == 2 and request[0] == 'show':
        return True
    return False

@bot.message_handler(func=check_show_request)
def show_repos(message):
    _, user_name = message.text.split()

    # Create an object to interact with the github.
    g = Github()

    # Upload the user by his/her name.
    try:
        user = g.get_user(user_name)
    except Exception as e:
        return "No such user!"

    repos_list = [repo.name for repo in user.get_repos()]

    # Search for a repository by its name.
    bot.send_message(message.chat.id, "\n".join(repos_list))


bot.polling()