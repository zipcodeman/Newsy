from feed import Feed

class RSSFeed(Feed):
  @staticmethod
  def announceListen():
    return "(R)ss"

  @staticmethod
  def canListen(c):
    return c.upper()[0] == "R"
