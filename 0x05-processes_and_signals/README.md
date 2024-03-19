# 0x05-processes_and_signals
This directory tests understanding of processes and signals in linux. It also tests understanding of the following commands:
- ps
- pgrep
- pkill
- kill
- exit
- trap
1. **0-what-is-my-pid** - a Bash script that displays its own `PID`.
2. **1-list_your_processes** - a Bash script that displays a list of currently running processes.
3. **2-show_your_bash_pid** - a Bash script that displays lines containing the `bash` word, thus allowing us to easily get the `PID` of the Bash process.
4. **3-show_your_bash_pid_made_easy** - a Bash script that displays the `PID`, along with the process name, of processes whose name contain the word `bash`.
5. **4-to_infinity_and_beyond** - a Bash script that displays `To infinity and beyond` indefinitely. It sleeps for two seconds before displaying each.
6. **5-dont_stop_me_now** - a Bash script that stops previously started `4-to_infinity_and_beyond` process using the `kill` command.
7. **6-stop_me_if_you_can** - a Bash script that also stops `4-to_infinity_and_beyond` process without using the `kill` and `killall` commands.
8. **7-highlander** - a bash script that displays `To infinity and beyond` indefinitely and sleeps for two seconds between each display. It also displays `I am invincible!!!` each time it receives a `SIGTERM` signal.
9. **8-beheaded_process** - a Bash script that kills the previously started process `7-highlander`.
