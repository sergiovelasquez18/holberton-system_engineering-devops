# 0x05. Processes and signals

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
* What is a PID
* What is a process
* How to find a process’ PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored

## Requirements
### General
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 14.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing

---

### [0. What is my PID](./0-what-is-my-pid)
* Write a Bash script that displays its own PID.

### [1. List your processes](./1-list_your_processes)
* Write a Bash script that displays a list of currently running processes.

### [2. Show your Bash PID](./2-show_your_bash_pid)
* Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

### [3. Show your Bash PID made easy](./3-show_your_bash_pid_made_easy)
* Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

### [4. To infinity and beyond](./4-to_infinity_and_beyond)
* Write a Bash script that displays To infinity and beyond indefinitely.

### [5. Don't stop me now!](./5-dont_stop_me_now)
* Write a Bash script that stops 4-to_infinity_and_beyond process.

### [6. Stop me if you can](./6-stop_me_if_you_can)
* Write a Bash script that stops 4-to_infinity_and_beyond process.

### [7. Highlander](./7-highlander)
* Write a Bash script that displays:
```
- To infinity and beyond indefinitely
- With a sleep 2 in between each iteration
- I am invincible!!! when receiving a SIGTERM signal
```

### [8. Beheaded process](./8-beheaded_process)
* Write a Bash script that kills the process 7-highlander.

---

## Author
* **Sergio velasquez** - [sergiovelasquez18](https://github.com/sergiovelasquez18)
