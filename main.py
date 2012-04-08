#! /usr/bin/env python

# Check for root user login
import os, sys
if not os.geteuid()==0:
    sys.exit("\nOnly root can run this script\n")

# Get your username (not root)
import pwd
uname=pwd.getpwuid(1000)[0]

# The remastering process uses chroot mode.
# Check to see if this script is operating in chroot mode.
# /home/mint directory only exists in chroot mode
is_chroot = os.path.exists('/home/mint')
dir_develop=''
if (is_chroot):
	dir_develop='/usr/local/bin/develop'
	dir_user = '/home/mint'
else:
	dir_develop='/home/' + uname + '/develop'
	dir_user = '/home/' + uname

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================

# THIS IS THE SCRIPT FOR ADDING THE SWIFT LINUX CONFIGURATION SCRIPTS

print '======================================'
print 'BEGIN ADDING SYSTEM INFORMATION WIZARD'

import shutil, subprocess
	
src = dir_develop + '/ui-config-info/usr_local_bin/config-info.py'
dest = '/usr/local/bin/config-info.py'
shutil.copyfile (src, dest)
os.system ('chmod a+rx ' + dest)

src = dir_develop + '/ui-config-info/usr_share_applications/config-info.desktop'
dest = '/usr/share/applications/config-info.desktop'
shutil.copyfile (src, dest)

print 'FINISHED ADDING ADDING SYSTEM INFORMATION WIZARD'
print '================================================'
