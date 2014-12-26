import subprocess
import os

# returns <type 'int'> the exit code.
# output = subprocess.call(['git', 'status', '--porcelain'])

# print type(output)
# print str(output)
# subprocess.call(['ls', '-la'])

task = subprocess.Popen(['git', 'status', '--porcelain'], stdout=subprocess.PIPE)

for l in task.stdout.readlines():
   print "This file is not committed. ==> %s" % (l.split()[1])

# print type(task.stdout)

# for l in task.stdout.readlines():
   # print "This file is not committed. ==> %s" % (l)
if os.path.getsize("/Users/richvogt/Code/git_test") > 0:
  print "Please commit, checkout, or stash your changes."