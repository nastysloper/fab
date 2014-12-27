import subprocess
import os

# returns <type 'int'> the exit code.
# output = subprocess.call(['git', 'status', '--porcelain'])

# print type(output)
# print str(output)
# subprocess.call(['ls', '-la'])

task = subprocess.Popen(['git', 'status', '--porcelain'], stdout=subprocess.PIPE)
flag = False
for l in task.stdout.readlines():
  flag = True
  print "This file is not committed. ==> %s" % (l.split()[1])

if flag:
  print("Please commit, checkout, or stash your changes.")
else:
  print "pull"
  fetch = subprocess.Popen(['git', 'fetch'])
  fetch.communicate([0])
  merge = subprocess.Popen(['git', 'merge', '--ff-only'])
  fetch.communicate([0])

# for l in task.stdout.readlines():
   # print "This file is not committed. ==> %s" % (l)
