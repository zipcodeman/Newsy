class Configuration:
  def __init__(self, filename):
    self.filename = filename
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
      print "(E)xit"
      print
      c = raw_input("> ").upper()
      if c == "T":
        pass
      if c == "E":
        end = True
