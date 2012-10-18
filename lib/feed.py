class Feed:
  def __init__(self, configString=None, interactive=False):
    raise Exception("Define Feed Constructor For: " + self.__class__.__name__)

  def getConfigString():
    return ""

  @staticmethod
  def announceListen():
    return "---"

  @staticmethod
  def canListen(c):
    return False
