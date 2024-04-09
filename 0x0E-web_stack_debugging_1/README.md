# Project Title: Debugging Nginx Installation on Ubuntu Container

# Introduction:

This project aims to troubleshoot and resolve the issue preventing the Nginx installation on an Ubuntu container from listening on port 80. Debugging involves identifying the root cause of the problem and implementing a solution to ensure that Nginx is running and listening on port 80 across all the server's active IPv4 IPs.

Steps to Debug Nginx Installation:

Set Up Environment:

Start an Ubuntu container with Docker.
Install Nginx on the container using the package manager (apt-get).
Investigate Nginx Configuration:

Check the Nginx configuration file (nginx.conf) for any misconfigurations or errors.
Verify that the listen directive in the configuration file is set to port 80.
Identify Port 80 Availability:

Use networking tools like netstat or ss to check if port 80 is already in use.
Identify any processes or services occupying port 80 and resolve conflicts.
Check Firewall Settings:

Verify that the firewall (e.g., UFW) is not blocking traffic on port 80.
If necessary, configure the firewall to allow incoming connections on port 80.
Restart Nginx Service:

Restart the Nginx service to apply any configuration changes.
Check for errors or warnings during the service restart.
Verify Nginx Listening on Port 80:

Use tools like curl or a web browser to access the server via port 80.
Confirm that Nginx serves content correctly on port 80.
