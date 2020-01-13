import os, json, slack
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/slack/interactive', methods = ['POST'])
def slack_interactive():

    data = request.form

    app.logger.info(data['payload'])

    return "Okay"

@app.route('/slack/options', methods = ['GET', 'POST'])
def slack_options():

    app.logger.info("hello")

    return "Okay"


@app.route('/post', methods = ['POST'])
def post_daily():

    vote_blocks = []

    data = request.get_json()

    for post in data['payload']:
        vote_blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": post['data']['title']
            },
            "accessory": {
                "type": "image",
                "image_url": post['data']['url'],
                "alt_text": post['data']['title']
            }
        })

    app.logger.info(json.dumps(vote_blocks))

    slack_token = "xoxb-668918983126-893055399409-5F5ys2eu9DIFC4XGnibEbL5T"
    client = slack.WebClient(token=slack_token)

    client.chat_postMessage(
      channel="GQMEYGN84",
      blocks=json.dumps(vote_blocks)
  #     blocks=[
  #   {
  #           "type": "section",
  #           "text": {
  #               "type": "mrkdwn",
  #               "text": "Summer floof vs winter floof"
  #           },
  #           "accessory": {
  #               "type": "image",
  #               "image_url": "https://i.redd.it/yojfabbso9a41.jpg",
  #               "alt_text": "palm tree"
  #           }
  #       },
  #   {
  #           "type": "section",
  #           "text": {
  #               "type": "mrkdwn",
  #               "text": "Pick an item from the dropdown list"
  #           },
  #           "accessory": {
  #               "type": "static_select",
  #               "placeholder": {
  #                   "type": "plain_text",
  #                   "text": "Select an item",
  #                   "emoji": True
  #               },
  #               "options": [
  #                   {
  #                       "text": {
  #                           "type": "plain_text",
  #                           "text": "Choice 1",
  #                           "emoji": True
  #                       },
  #                       "value": "value-0"
  #                   },
  #                   {
  #                       "text": {
  #                           "type": "plain_text",
  #                           "text": "Choice 2",
  #                           "emoji": True
  #                       },
  #                       "value": "value-1"
  #                   },
  #                   {
  #                       "text": {
  #                           "type": "plain_text",
  #                           "text": "Choice 3",
  #                           "emoji": True
  #                       },
  #                       "value": "value-2"
  #                   }
  #               ]
  #           }
  #       }
  # ]
)

    return "Okay"