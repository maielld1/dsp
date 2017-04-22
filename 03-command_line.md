# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

1. pwd - Print working directory
2. cd ~ - Move to home directory
3. cd .. - Move up one directory
4. mkdir (directory) - Create directory
5. rm (file) - Delete file
6. rm -f (file) - Force delete
7. rm -r (directory) - Delete directory
8. mv (old) (new) - Rename (old) to (new)
9. cp (file) (directory) - Copy (file) to (directory)
10. grep (key) (file) - Search through (file) and return all occurences of (key)

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

1. ls - Lists directory contents
2. ls -a - List all directory contents (including hidden files)
3. ls -l - Lists all directory contents in long format
4. ls -lh - Same as above, except in human readable format
5. ls -lah - List all directory contents in human readable, long format
6. ls -t - Lists directory contents sorted by modification time
7. ls -Glp - G inhibits the display of group information, l displays the contents in long format, and p shows which files have an indicator such as '/'

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

1. ls -d - Displays only directories
2. ls -u - Displays files by access time
3. ls -r - Displays files in reverse order
4. ls -R - Displays subdirectories as well
5. ls -q - Displays all nonprinting characters with "?"

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs reads in items from standard input (stdin) and executes a command (default is /bin/echo) with any given initial arguments. For example, the xargs can be used with the grep and find commands:

find . -name "*.py" | xargs grep "Data Science"

The above command finds all Python files from the current directory, and within each file, looks for occurences of "Data Science". What xargs is doing is essentially unpacking arguments and feeding them into commands, one by one.

 

