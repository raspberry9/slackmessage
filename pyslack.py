'''
PySlack

Python Slack Utilities

Author: koo@fruit.team
'''
import json
import sys

PY3 = sys.version_info > (3, 0)

if PY3:
    import urllib.parse
    import urllib.request
else:
    import urllib2

class PySlackError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class PySlack(object):
    '''
    Python Slack Module
    '''
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def _pretty_error_message(self, message):
        words = message.split('_')
        if not words:
            return ''
        words[0] = words[0].title()
        return '%s.' % ' '.join(words)

    def _call_slack_api(self, url, params):
        headers = {'Content-type': 'application/json'}
        data = json.dumps(params)
        if PY3:
            req = urllib.request.Request(url, data=data.encode('utf-8'), headers=headers)
            result = urllib.request.urlopen(req).read().decode('utf-8')
        else:
            req = urllib2.Request(url=url, data=data, headers=headers)
            response = urllib2.urlopen(req)
            result = response.read()
        if result != 'ok':
            raise PySlackError(self._pretty_error_message(result))
        return result

    def send_message(self, text):
        '''
        Send a message to Slack
        '''
        self._call_slack_api(self.webhook_url, {'text': text})

if __name__ == '__main__':
    import os
    webhook_url = os.environ.get('SLACK_WEBHOOK_URL')
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        text = 'hello world! :heart:'
    if webhook_url:
        print(webhook_url, text)
        ps = PySlack(webhook_url)
        ps.send_message(text)
