# Web Stack Debugging

## Introduction
Debugging is an integral part of a software engineer's role, often consuming a significant portion of their time. It's an art that requires years, even decades, to master. Seasoned engineers excel at debugging due to their vast experience dealing with broken code, buggy systems, peculiar edge cases, and elusive race conditions.

## Non-Exhaustive Guide to Debugging

### School Specific
If you encounter issues with scripts or code that are tested on a checker, like a Bash script, you can simulate the environment by starting a Docker container with the specified distribution and running your code within it.

### Test and Verify Your Assumptions
When troubleshooting, it's essential to question your assumptions systematically. For example, if a web server fails to serve a page, consider:

- Is the web server started?
- On which port should it listen?
- Is it listening on the correct port and IP?
- Is there a firewall enabled?
- Have you checked the logs?
- Can you connect to the HTTP port from your location?

### Get a Quick Overview of the Machine State
Upon connecting to a server, understanding recent and current activities is crucial. Execute the following commands for a quick overview:
1. `w`: Shows server uptime, connected users, and load average.
2. `history`: Displays previously executed commands.
3. `top`: Lists currently running processes.
4. `df`: Shows disk utilization.
5. `netstat`: Provides information on listening ports and active sockets.

### Machine Level Debugging
For machine-level debugging, ask:
- Does the server have free disk space?
- Is the server able to keep up with CPU load?
- Does the server have available memory?
- Are the server disk(s) able to handle read/write IO?

### Network Issue
For network-related problems, consider:
- Are the expected network interfaces and IPs up and running?
- Does the server listen on the expected sockets?
- Can you connect to the desired socket from your location?
- Are the firewall rules correct?

### Process Issue
When dealing with misbehaving software, check:
- Is the software started?
- Is the software process running?
- Are there any relevant entries in the log files?
