"""
Bash completed man and info pages generation

bash.py
(companion:
http://code.activestate.com/recipes/577857-terminal-output-of-the-bash-completed-man-and-info/
)
To start this open a terminal and strike the "Tab" key
to get all possibilities (strike y, and strike the space key alot). 

Select all then Copy and save in "comms.txt"

Modify the file so ONLY the possiblities consume a line; 
no prompts or extra newlines.
  (first line must be a command, the last line must be a command)

Save the file ("~/Documents/bashing/comms.txt" is my path) 
then run this script in "~/Documents/bashing/".

This generates two (2) files: 
bash_help_man.sh
bash_help_info.sh

Then it runs these files: 
bash bash_help_man.sh
bash bash_help_info.sh

HINT: Ensure terminal width is good, 80 wide is perfect for any/all printers.
The files generated by bash will match your terminal's window width.
Don't forget terminal buffer or scroll back may need to be set to unlimited.

This produces 2 files for every command (every line) in "comms.txt".
All manpages are wrote in "mans/", all infopages are wrote in "infos/"

There is now alot of files to read and organize; lets separate these by size.

Once complete do as you wish the files less than 128 kb;
these files are COPIED into there new respective home, I repeat COPIED.

The files 128 kb and higher ARE NOT copied to anywhere!
"""

import os, sys
__fn = 'comms.txt'
__f = open(__fn, 'rw')
text = __f.readlines()
count = 0
all1 = ''
all2 = ''
for t in text[:-1]:
    r = t[:-1]
    comm1 = "man " + r + " > " + "bashed/mans/" + r + "_man.txt" + '\n'
    comm2 = "info " + r + " > " + "bashed/infos/" + r + "_info.txt" + '\n'
    all1 += comm1
    all2 += comm2
    count += 1

    print count, "of", len(text), ":", r

f1 = open('bash_help_man.sh', 'w')
f1.write(all1)
f1.close()
f2 = open('bash_help_info.sh', 'w')
f2.write(all2)
f2.close()


"""
create a directory to hold the soon to come output
  ("bashed/" is a good name as any)
  ~/Documents/bashing/bashed/

create two directories with-in "bashed/":
1: "mans/"
2: "infos/"
  ("~/Documents/bashing/bashed/mans/",
   "~/Documents/bashing/bashed/infos/")
"""
os.mkdir('bashed')
os.mkdir('bashed/mans')
os.mkdir('bashed/infos')

import subprocess


p1 = subprocess.Popen("bash bash_help_man.sh", shell=True)
p2 = subprocess.Popen("bash bash_help_info.sh", shell=True)
sts1 = os.waitpid(p1.pid, 0)[1]
sts2 = os.waitpid(p2.pid, 0)[1]
print sts1
print sts2
"""
Now you have alot of files to read and organize; lets separate these by size.

Once complete do as you wish the files less than 128 kb;
these files are COPIED into there new respective home, I repeat COPIED.

The files 128 kb and higher ARE NOT copied to anywhere!


"""

import os
import glob
import shutil

def dest(f, folder, i):
    return folder[i] + os.path.split(f)[1]


def deal_file(f, folder):
    size = os.path.getsize(f)
    
    if size == 0:
        shutil.copy2(f, dest(f, folder, 0))
    if size > 1024:
        shutil.copy2(f, dest(f, folder, 1))
    if size > 1024 * 2:
        shutil.copy2(f, dest(f, folder, 2))
    if size > 1024 * 3:
        shutil.copy2(f, dest(f, folder, 3))
    if size > 1024 * 4:
        shutil.copy2(f, dest(f, folder, 4))
    if size > 1024 * 5:
        shutil.copy2(f, dest(f, folder, 5))
    if size > 1024 * 6:
        shutil.copy2(f, dest(f, folder, 6))
    if size > 1024 * 7:
        shutil.copy2(f, dest(f, folder, 7))
    if size > 1024 * 8:
        shutil.copy2(f, dest(f, folder, 8))
    if size > 1024 * 16:
        shutil.copy2(f, dest(f, folder, 9))
    if size > 1024 * 32:
        shutil.copy2(f, dest(f, folder, 10))
    if size > 1024 * 64:
        shutil.copy2(f, dest(f, folder, 11))
    if size > 1024 * 128:
        shutil.copy2(f, dest(f, folder, 12))

base1, base2 = 'bashed/mans/', 'bashed/infos/'
pre, post = 'under', 'kb'
sizes = ["empties", 1, 2, 3, 4, 5, 6, 7, 8, 16, 32, 64, 128]
folder1 = []
folder2 = []
done = 0

for t in sizes:
    
    l = ''
    if t is sizes[0]:
        l = str(sizes[done]) + "/"
    else:
        l = pre + str(sizes[done]) + post + "/"
    os.mkdir(str(base1 + l))
    print str(base1 + l), "is", done, "out of", len(sizes)
    os.mkdir(str(base2 + l))
    print str(base2 + l), "is", done, "out of", len(sizes)
    folder1.append(str(base1 + l))
    folder2.append(str(base2 + l))
    done += 1

alls1 = glob.glob(base1 + "*.txt")
alls2 = glob.glob(base2 + "*.txt")
done = 0
for t in alls1:
    done += 1
    deal_file(t, folder1)
    print t, "is", done, "out of", len(alls1)
for t in alls2:
    deal_file(t, folder2)
    print t, "is", done, "out of", len(alls1)
print "Copy completed!"
print "The files 128 kb and higher WERE NOT copied to anywhere!"
