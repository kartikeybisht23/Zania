import requests
import json
class SlackNotifier:
    def __init__(self, channel):
        self.channel = channel
        self.slack_token = "xoxb-7776815665857-7777249509633-TsLgwyxIYIufMSefCY59B9Dh"  # Add your Slack Bot OAuth Token here

    def post_results(self, answers):
        json_output = json.dumps(answers, indent=4)

        # Prepare the payload for Slack API
        payload = {
            "channel": self.channel,
            "text": f"Here are the answers:\n```{json_output}```"
        }

        headers = {
            "Authorization": f"Bearer {self.slack_token}",
            "Content-Type": "application/json"
        }

        # Send the request to Slack API
        response = requests.post("https://slack.com/api/chat.postMessage", headers=headers, json=payload)

        # Check for success or failure
        if response.status_code == 200 and response.json().get("ok"):
            print("Message successfully posted to Slack!")
        else:
            print(f"Failed to post message: {response.text}")

