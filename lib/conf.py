import twitter
import facebook
import atom
import rss
class Configuration:
  def __init__(self, filename):
    self.filename = filename
    self.feedTypes = [
      twitter.TwitterFeed,
      facebook.FacebookFeed,
      atom.AtomFeed,
      rss.RSSFeed,
    ]
    self.feeds = []
    try:
      self.confFile = open(filename, 'r')
    except IOError as e:
      self.interactiveConf()

  def interactivePrompt(self):
      print
      print "What kind of account would you like to add:"
      for t in self.feedTypes:
        print t.announceListen()
      print "(E)xit/(Q)uit"
      print "Display this (H)elp message"
      print

  def interactiveConf(self):
    self.interactivePrompt()
    
    end = False
    understood = True

    while not end:
      if understood:
        c = raw_input("> ").upper()[0]
      else:
        c = raw_input("? ").upper()[0]
      understood = True
      handled = False
      for t in self.feedTypes:
        if t.canListen(c):
          self.feeds.append(t(interactive=True))
          handled = True
      if not handled:
        if  c == "E" or c == "Q":
          end = True
        elif  c == "H":
          self.interactivePrompt()
        else:
          understood = False

    for feed in self.feeds:
      print feed.getConfigString()
