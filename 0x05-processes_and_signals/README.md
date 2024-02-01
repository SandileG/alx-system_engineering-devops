# Processes and SignalsPID (Process ID):

# PID stands for Process ID.

It is a unique numerical identifier assigned to each running process in a Unix-like operating system. PIDs are used by the system to manage and control processes, enabling operations like monitoring, termination, and resource allocation.

# Process:

A process is an executing instance of a program in a computer system. It has its own memory space, resources, and state. Processes can run in the background or foreground, and they are managed by the operating system's scheduler. Each process is identified by a unique PID.

# Finding a Process' PID:

You can find a process' PID using commands like ps (process status) or pgrep (process grep). For example, ps aux | grep <process_name> will display information about the specified process, including its PID.

# Killing a Process:

To terminate a process, the kill command is used. You need to provide the PID of the process you want to terminate. The basic syntax is kill <PID>. Alternatively, killall <process_name> can be used to kill processes by name.

# Signal:

A signal is a software interrupt delivered to a process. Signals are used to communicate with processes and instruct them to perform various actions. The kill command, for instance, sends signals to processes to terminate them gracefully or perform other actions.

# Signals that Cannot be Ignored:

There are two signals that cannot be ignored by a process:

* SIGKILL (9): This signal immediately terminates a process. It cannot be caught, blocked, or ignored by the process.

* SIGSTOP (19 or 17): This signal stops a process's execution. Like SIGKILL, it cannot be caught, blocked, or ignored. It halts the process until a SIGCONT signal is received.
