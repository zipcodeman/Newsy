from feed import Feed
import oauth2
import urlparse
import webbrowser

CONSUMER_KEY = "4mambF0N20hA67eInHskVA"
CONSUMER_SECRET = "2DB218TyvB7FeTJvXqJzhYcc1f5zXeweyE883ir48"

request_token_url = "http://twitter.com/oauth/request_token"
authorize_url = 'http://twitter.com/oauth/authorize'
access_token_url = 'http://twitter.com/oauth/access_token'

class TwitterFeed(Feed):
  def __init__(self, configString=None, interactive=False):
    if interactive:
      print "Requesting access to twitter account..."
      consumer = oauth2.Consumer(key = CONSUMER_KEY,
                                 secret = CONSUMER_SECRET)
      

      client = oauth2.Client(consumer)

      resp,content = client.request(request_token_url, "GET")
      request_token = dict(urlparse.parse_qsl(content))

      redirect_url = "%s?oauth_token=%s" % (authorize_url,
                                            request_token['oauth_token'])
      
      ans = 'n'
      while ans == 'n':
        webbrowser.open(redirect_url)
        ans = raw_input("Did you receive a pin? [y/n] ")

      pin = raw_input("Enter Pin: ")

      token = oauth2.Token(request_token['oauth_token'],
                            request_token['oauth_token_secret'])
      token.set_verifier(pin)

      client = oauth2.Client(consumer, token)

      resp, content = client.request(access_token_url, "POST")
      access_token = dict(urlparse.parse_qsl(content))

      self.oauth_token = access_token['oauth_token']
      self.oauth_token_secret = access_token['oauth_token_secret']
    else:
      parts = configString.split()

      self.oauth_token = parts[1]
      self.oauth_token_secret = parts[2]

  def getConfigString(self):
    return "twitter %s %s" % (self.oauth_token, self.oauth_token_secret)

  @staticmethod
  def announceListen():
    return "(T)witter"

  @staticmethod
  def canListen(c):
    return c.upper()[0] == 'T'
