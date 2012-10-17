import twitter
import facebook
import atom
import rss
class Configuration:
  def __init__(self, filename):
    self.filename = filename
    self.feeds = []
    try:
      self.confFile = open(filename, 'r')
    except IOError as e:
      self.interactiveConf()

  def interactiveConf(self):
    end = False
    while not end:
      print
      print "What kind of account would you like to add:"
      print "(T)witter"
      print "(F)acebook"
      print "(A)tom"
      print "(R)ss"
      print "(E)xit"
      print
      c = raw_input("> ").upper()
      if    c == "T":
        self.feeds.append(twitter.TwitterFeed(interactive=True))
      elif  c == "F":
        self.feeds.append(facebook.FacebookFeed(interactive=True))
      elif  c == "A":
        self.feeds.append(atom.AtomFeed(interactive=True))
      elif  c == "R":
        self.feeds.append(rss.RSSFeed(interactive=True))
      elif  c == "E":
        end = True
