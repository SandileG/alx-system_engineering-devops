# Networking Basics - Part 2

## Localhost/127.0.0.1

- **What is localhost/127.0.0.1:**
  - Localhost is a loopback address used to access the network services that are running on the host via the network interface. 127.0.0.1 is the IPv4 address associated with localhost.

## 0.0.0.0

- **What is 0.0.0.0:**
  - 0.0.0.0 is a special-purpose IPv4 address that usually indicates "all addresses" or "any address." It can be used in various contexts, such as binding to all network interfaces.

## /etc/hosts

- **What is /etc/hosts:**
  - /etc/hosts is a plain text file on Unix-based operating systems that maps IP addresses to hostnames. It is used to override the DNS for specific domains or provide local name resolution.

## Displaying Active Network Interfaces

- **How to display your machine’s active network interfaces:**
  - Use the following command to display active network interfaces on your machine:
    ```bash
    ifconfig    # On Linux
    ipconfig    # On Windows
    ```
