import lib.conf

from optparse import OptionParser

if __name__ == "__main__":
  parser = OptionParser()

  parser.add_option("-c", "--config", dest="config",
                    help="Configuration file location [Default %default]",
                    metavar="FILE", default="~/.newsyrc", type="string")

  (options, args) = parser.parse_args()

  lib.conf.Configuration(options.config)
  print options.config
