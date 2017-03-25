'''
Python Slack Message

Author: koo@fruit.team
'''
import json
import urllib.parse
import urllib.request

class SlackMessageError(Exception):
    '''
    Error class for SlackMessage
    '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class SlackMessage(object):
    '''
    Slack Message Client
    You can send a message to channel.
    '''
    def __init__(self, bot_name, webhook_url):
        self.bot_name = bot_name
        self.url = webhook_url

    def _pretty_error_message(self, error_from_slack_api):
        '''
        Returns pretty error message
        ex)
            bot = SlackMessage('test', webhook_url='http://some_slack_webhook_url')
            print(bot._pretty_error_message('some_error_message_from_slack'))
        
            Some error message from slack.
        '''
        words = error_from_slack_api.split('_')
        if not words:
            return ''
        words[0] = words[0].title()
        return '%s.' % ' '.join(words)


    def send_message(self, text, channel='#general', icon_emoji=':ghost:'):
        '''
        Send a message to channel
        ex)
            bot = SlackMessage('test', webhook_url='http://some_slack_webhook_url')
            bot.send_message('Build completed! you can download <https://build_download_url|Here>', '#general', ':heart:')
            bot.send_message('Build failed! <https://build_failed_log_url|Click here> for details.', '#general', ':broken_heart:')

        '''
        try:
            data = json.dumps(
                dict(
                    text=str(text),
                    channel=channel,
                    username=self.bot_name,
                    icon_emoji=icon_emoji
                )
            )
        except:
            raise SlackBotError("invalid data")
        req = urllib.request.Request(self.url, data=data.encode('utf-8'), headers={'Content-type': 'application/json'})
        res = urllib.request.urlopen(req).read().decode('utf-8')
        if res != 'ok':
            raise SlackBotError(self._pretty_error_message(res))
        
