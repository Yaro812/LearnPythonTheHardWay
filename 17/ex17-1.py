from sys import argv

# make this script as short as you can
open(argv[2], 'w').write(open(argv[1]).read())
