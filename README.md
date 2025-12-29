# OverTheWire Bandit - Complete Walkthrough & Notes

OverTheWire Bandit is a renowned CTF-style wargame that focuses on Linux fundamentals and system security concepts.  
This repository presents **structured, level-by-level notes and explanations** derived from my personal solutions.  

![Bandit Wargame Overview](https://github.com/user-attachments/assets/3678392d-cea7-4504-a7d4-2ba17b39666d)

> **Note:** Readers are encouraged to attempt each challenge independently before consulting these notes, as the primary learning benefit comes from hands-on problem-solving.

---


## Table of Contents
- [Bandit Level 0](#bandit-level-0)
- [Bandit Level 1](#bandit-level-1)
- [Bandit Level 2](#bandit-level-2)
- [Bandit Level 3](#bandit-level-3)
- [Bandit Level 4](#bandit-level-4)
- [Bandit Level 5](#bandit-level-5)
- [Bandit Level 6](#bandit-level-6)
- [Bandit Level 7](#bandit-level-7)
- [Bandit Level 8](#bandit-level-8)
- [Bandit Level 9](#bandit-level-9)
- [Bandit Level 10](#bandit-level-10)
- [Bandit Level 11](#bandit-level-11)
- [Bandit Level 12](#bandit-level-12)
- [Bandit Level 13](#bandit-level-13)
- [Bandit Level 14](#bandit-level-14)
- [Bandit Level 15](#bandit-level-15)
- [Bandit Level 16](#bandit-level-16)
- [Bandit Level 17](#bandit-level-17)
- [Bandit Level 18](#bandit-level-18)
- [Bandit Level 19](#bandit-level-19)
- [Bandit Level 20](#bandit-level-20)
- [Bandit Level 21](#bandit-level-21)
- [Bandit Level 22](#bandit-level-22)
- [Bandit Level 23](#bandit-level-23)
- [Bandit Level 24](#bandit-level-24)
- [Bandit Level 25](#bandit-level-25)
- [Bandit Level 26](#bandit-level-26)
- [Bandit Level 27](#bandit-level-27)
- [Bandit Level 28](#bandit-level-28)
- [Bandit Level 29](#bandit-level-29)
- [Bandit Level 30](#bandit-level-30)
- [Bandit Level 31](#bandit-level-31)
- [Bandit Level 32](#bandit-level-32)
- [Bandit Level 33](#bandit-level-33)

## Bandit Level 0
**Goal:** Log into the game using SSH
**Host:** bandit.labs.overthewire.org
**Port:** 2220
**Username:** bandit0
**Password:** bandit0

### Commands:
```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

### Notes:
- First level is just about connecting via SSH
- The password is the same as the username for level 0
- After login, proceed to Level 1

## Bandit Level 1
**Goal:** Find the password in the readme file in the home directory
**Username:** bandit1
**Password:** (from previous level's readme)

### Commands:
```bash
ls -la
cat readme
```

### Notes:
- The password is stored in a file called 'readme'
- Use `ls` to list files and `cat` to view contents

## Bandit Level 2
**Goal:** Find the password in a file with spaces in the filename
**Username:** bandit2

### Commands:
```bash
# Method 1: Use quotes
cat "spaces in this filename"

# Method 2: Escape spaces
cat spaces\ in\ this\ filename

# Method 3: Use tab completion
cat spa<TAB>
```

### Notes:
- When dealing with filenames containing spaces, you can either:
  - Use quotes around the filename
  - Escape spaces with backslashes
  - Use tab completion

## Bandit Level 3
**Goal:** Find the password in a hidden file in the inhere directory

### Commands:
```bash
ls -la inhere/
cat inhere/.hidden
```

### Notes:
- Hidden files in Linux start with a dot (.)
- Use `ls -a` to show all files, including hidden ones

## Bandit Level 4
**Goal:** Find the only human-readable file in the inhere directory

### Commands:
```bash
file ./*
cat ./-file07
```

### Notes:
- Use `file` command to determine file types
- Look for "ASCII text" in the output
- Some files might start with hyphens, use `./` prefix to handle them

## Bandit Level 5
**Goal:** Find the human-readable file with specific properties

### Commands:
```bash
find . -type f -size 1033c ! -executable
```

### Notes:
- Look for files that are:
  - Human-readable
  - 1033 bytes in size
  - Not executable

## Bandit Level 6
**Goal:** Find the password in a file somewhere on the server

### Commands:
```bash
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
```

### Notes:
- Search the entire filesystem
- Redirect errors to /dev/null to clean up output
- Look for files owned by bandit7 and group bandit6

## Bandit Level 7
**Goal:** Find the password next to the word 'millionth' in a large file

### Commands:
```bash
grep 'millionth' data.txt
```

### Notes:
- Use grep to search for patterns in files
- The password is on the same line as 'millionth'

## Bandit Level 8
**Goal:** Find the only line that occurs once in a file

### Commands:
```bash
sort data.txt | uniq -u
```

### Notes:
- `sort` sorts the lines
- `uniq -u` shows only unique lines

## Bandit Level 9
**Goal:** Find the password in a file with '=' characters

### Commands:
```bash
strings data.txt | grep "=="
```

### Notes:
- `strings` extracts readable text from binary files
- Look for lines with multiple '=' characters

## Bandit Level 10
**Goal:** Find the base64 encoded password in a file

### Commands:
```bash
base64 -d data.txt
```

### Notes:
- `base64 -d` decodes base64 encoded text

## Bandit Level 11
**Goal:** Find the password in a file with ROT13 encoding

### Commands:
```bash
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

### Notes:
- ROT13 is a simple letter substitution cipher
- `tr` command can be used to translate characters

## Bandit Level 12
**Goal:** Decompress a hexdump file multiple times

### Commands:
```bash
xxd -r data.txt > data
file data
mv data data.gz
gunzip data.gz
# Repeat with different compression formats
```

### Notes:
- Use `file` to identify file types
- Common compression formats: gzip, bzip2, tar

## Bandit Level 13
**Goal:** Use SSH private key to log into the next level

### Commands:
```bash
ssh -i sshkey.private bandit14@localhost
```

### Notes:
- Set proper permissions on the private key: `chmod 600 sshkey.private`
- Connect to localhost since the key is for bandit14

## Bandit Level 14
**Goal:** Submit the current password to port 30000 on localhost

### Commands:
```bash
cat /etc/bandit_pass/bandit14 | nc localhost 30000
```

### Notes:
- `nc` (netcat) can be used to send data to a port
- The password is stored in /etc/bandit_pass/

## Bandit Level 15
**Goal:** Submit the password using SSL encryption

### Commands:
```bash
openssl s_client -connect localhost:30001
# Then paste the password
```

### Notes:
- `openssl s_client` connects to SSL services
- The connection might time out, so be quick

## Bandit Level 16
**Goal:** Find a server listening on a port between 31000-32000 with SSL

### Commands:
```bash
nmap -p 31000-32000 localhost
openssl s_client -connect localhost:31790
```

### Notes:
- Use nmap to scan for open ports
- Test each port with SSL client

## Bandit Level 17
**Goal:** Find the one line that's different between two files

### Commands:
```bash
diff passwords.old passwords.new
```

### Notes:
- `diff` shows differences between files
- The password is the line that's different

## Bandit Level 18
**Goal:** Log in with a modified .bashrc

### Commands:
```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
```

### Notes:
- The .bashrc is modified to log you out
- Use the command execution feature of SSH

## Bandit Level 19
**Goal:** Use a setuid binary to read a file

### Commands:
```bash
./bandit20-do cat /etc/bandit_pass/bandit20
```

### Notes:
- setuid binaries run with owner's privileges
- The binary can be used to read protected files

## Bandit Level 20
**Goal:** Use a setuid binary to connect to a port

### Commands:
```bash
# In one terminal:
nc -lvnp 12345
# In another terminal:
./suconnect 12345
```

### Notes:
- The setuid binary makes a connection to a port
- It sends the password when it receives the current level's password

## Bandit Level 21
**Goal:** Analyze a cron job

### Commands:
```bash
cd /etc/cron.d/
cat cronjob_bandit22
cat /usr/bin/cronjob_bandit22.sh
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

### Notes:
- Check cron jobs in /etc/cron.d/
- The script writes the password to a temporary file

## Bandit Level 22
**Goal:** Understand and exploit a cron job

### Commands:
```bash
cat /etc/cron.d/cronjob_bandit23
cat /usr/bin/cronjob_bandit23.sh
mytarget=$(echo I am user bandit23 | md5sum | cut -d ' ' -f 1)
echo $mytarget
cat /tmp/$mytarget
```

### Notes:
- The script creates a filename based on md5 hash
- The password is written to that file

## Bandit Level 23
**Goal:** Analyze a more complex cron job

### Commands:
```bash
# Create a script in /var/spool/bandit24/foo
# Make it executable: chmod +x /var/spool/bandit24/foo/script.sh
# Wait for the cron job to run
```

### Notes:
- The cron job runs scripts in /var/spool/bandit24/foo
- Create a script that reads the password file

## Bandit Level 24
**Goal:** Brute force a 4-digit PIN

### Commands:
```bash
for i in {0000..9999}; do
    echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i"
done | nc localhost 30002
```

### Notes:
- The service requires the current password and a 4-digit PIN
- Brute force all possible PINs

## Bandit Level 25
**Goal:** Analyze a shell script that runs as bandit26

### Commands:
```bash
cat /usr/bin/showtext
```

### Notes:
- The script uses `more` to display text
- Resize your terminal to be very small to trigger the pager
- Then use vim commands to get a shell

## Bandit Level 26
**Goal:** Break out of a restricted shell

### Commands:
```bash
# From the vim command mode in the previous level
:set shell=/bin/bash
:shell
```

### Notes:
- The restricted shell can be bypassed
- Use vim's ability to spawn a shell

## Bandit Level 27
**Goal:** Clone a git repository

### Commands:
```bash
mkdir /tmp/mydir
cd /tmp/mydir
git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
```

### Notes:
- The password is in the README file in the repository
- You need to create a temporary directory to clone into

## Bandit Level 28
**Goal:** Analyze a git repository with a password leak

### Commands:
```bash
git log -p
git show <commit-hash>
```

### Notes:
- Check the git history for password changes
- The password might be in an older commit

## Bandit Level 29
**Goal:** Find credentials in a git branch

### Commands:
```bash
git branch -a
git checkout dev
git log -p
```

### Notes:
- Check all branches with `git branch -a`
- The password might be in a different branch

## Bandit Level 30
**Goal:** Find a git tag

### Commands:
```bash
git tag
git show <tag-name>
```

### Notes:
- Tags are like bookmarks to specific commits
- Check all tags with `git tag`

## Bandit Level 31
**Goal:** Push a file to a git repository

### Commands:
```bash
echo 'May I come in?' > key.txt
git add -f key.txt
git commit -m "Add key"
git push origin master
```

### Notes:
- The .gitignore excludes certain files
- Use `git add -f` to force add ignored files

## Bandit Level 32
**Goal:** Escape the uppercase shell

### Commands:
```bash
$0
```

### Notes:
- The shell converts all input to uppercase
- `$0` refers to the name of the shell
- This gives you a normal shell

## Bandit Level 33
**Goal:** Congratulations!

### Notes:
- You've completed the Bandit wargame!
- The password for bandit33 is the same as bandit32
- There is no more levels after this

## General Tips
1. Always check file permissions with `ls -la`
2. Use `man` to read documentation for commands
3. Check for hidden files and directories
4. Look for setuid binaries with `find / -perm -4000 2>/dev/null`
5. Check cron jobs in `/etc/cron.d/`
6. Use `strings` to extract text from binary files
7. Check environment variables with `env`
8. Look for files with specific permissions:
   ```bash
   find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
   ```

## Common Commands Cheatsheet
```bash
# File operations
ls, cd, cat, file, find, grep, strings, diff

# Text processing
head, tail, sort, uniq, wc, cut, tr, base64

# Network
ssh, nc, nmap, openssl s_client

# Archives
tar, gzip, bzip2, xxd

# System
ps, top, env, sudo, su, chmod, chown
```

## Final Notes
- Always read the level's page for hints
- Don't forget to save passwords as you go
- Some levels require multiple terminal sessions
- If stuck, try looking at the scripts in /usr/bin/
- Check file permissions and ownership
