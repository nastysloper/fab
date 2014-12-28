import subprocess
import os


task = subprocess.Popen(['git', 'status', '--porcelain'], stdout=subprocess.PIPE)
flag = False
for l in task.stdout.readlines():
  flag = True
  print "This file is not committed. ==> %s" % l.split()[1]

if flag:
  print("Please commit, checkout, or stash your changes.")
else:
  print "pull"
  fetch = subprocess.Popen(['git', 'fetch'])
  fetch.communicate([0])
  merge = subprocess.Popen(['git', 'merge', '--ff-only'])
  fetch.communicate([0])

print "\nNow running cd"
current = os.getcwd()
print "we are in %s" % current
os.chdir("/Users/richvogt/Code")
subprocess.call("ls")
# returns back to current directory
