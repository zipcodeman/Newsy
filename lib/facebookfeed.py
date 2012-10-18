from feed import Feed

class FacebookFeed(Feed):
  @staticmethod
  def announceListen():
    return "(F)acebook"

  @staticmethod
  def canListen(c):
    return c.upper()[0] == "F"
