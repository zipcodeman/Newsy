from feed import Feed

class AtomFeed(Feed):
  @staticmethod
  def announceListen():
    return "(A)tom"

  @staticmethod
  def canListen(c):
    return c.upper()[0] == 'A'
