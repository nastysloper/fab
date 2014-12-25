import subprocess

# returns <type 'int'> the exit code.
# output = subprocess.call(['git', 'status', '--porcelain'])

# print type(output)
# print str(output)
# subprocess.call(['ls', '-la'])

task = subprocess.Popen(['git', 'status', '--porcelain'], stdout=subprocess.PIPE)

for l in task.stdout.readlines():
   print "This file is not committed. ==> %s" % (l.split()[1])

# for l in task.stdout.readlines():
   # print "This file is not committed. ==> %s" % (l)

print("Please commit, checkout, or stash your changes.")