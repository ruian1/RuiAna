import sys,os

#from ROOT import *

if len(sys.argv) < 2:
    msg  = '\n'
    msg += "Usage 1: %s $INPUT_ROOT_FILE(s)\n" % sys.argv[0]
    msg += '\n'
    sys.stderr.write(msg)
    sys.exit(1)

import ROOT
from larlite import larlite as fmwk

#from ROOT import fcllite, flashana

# Create ana_processor instance
my_proc = fmwk.ana_processor()

# Config File
cfg=sys.argv[1]
if not cfg.endswith('.fcl'):
    print 'Need for fcl file'
    sys.exit(1)

# Set input root file
for x in xrange(len(sys.argv)-2):
    my_proc.add_input_file(sys.argv[x+2])

# Specify IO mode
my_proc.set_io_mode(fmwk.storage_manager.kREAD)

# Specify output root file name
my_proc.set_ana_output_file("PaddleTrackOpflash_output.root");

# Attach an analysis unit ... here we use a base class which does nothing.
# Replace with your analysis unit if you wish.

myunit = fmwk.PaddleTrackOpflash()
myunit.configure(cfg)

my_proc.add_process(myunit)

print
print  "Finished configuring ana_processor. Start event loop!"
print

# Let's run it.
my_proc.run();
#you can do "my_proc.run()" to run over all events

# done!
print
print "Finished running ana_processor event loop!"
print

sys.exit(0)
