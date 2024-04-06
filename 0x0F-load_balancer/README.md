## Web Server Redundancy Setup

# Introduction

In this project, we aim to enhance the redundancy and reliability of our web infrastructure by introducing additional web servers. This will allow us to accommodate more traffic and ensure uninterrupted service even in the event of a server failure. The project involves setting up a load balancer and configuring multiple web servers to distribute incoming traffic evenly.

# Servers Provided

You have been provided with two additional servers:

gc-[STUDENT_ID]-web-02-XXXXXXXXXX
gc-[STUDENT_ID]-lb-01-XXXXXXXXXX

# Project Objectives

The main objectives of this project are as follows:

* Improve Redundancy: Implement redundancy for our web servers to ensure continuous availability and reliability of our web services.

* Increase Capacity: Double the number of web servers to handle increased traffic and improve scalability.

* Automate Configuration: Write Bash scripts to automate the setup process and configure brand new Ubuntu servers according to the project requirements.

# Load Balancing and HAProxy

# Introduction to Load Balancing

Load balancing is a technique used in web hosting and networking to distribute incoming network traffic across multiple servers. This helps optimize resource utilization, maximize throughput, minimize response time, and avoid overload on any single server.

# HAProxy

HAProxy, which stands for High Availability Proxy, is a free, open-source software that provides a high-performance TCP/HTTP load balancer and proxy server. It operates as a reverse proxy and distributes incoming connections to multiple backend servers based on various algorithms, such as round-robin, least connections, and IP hash.

HAProxy is widely used in web hosting environments, content delivery networks (CDNs), and high-traffic websites to achieve high availability, scalability, and fault tolerance.

# HTTP Header

HTTP headers are components of HTTP requests and responses exchanged between a client and a server during a web communication session. They convey metadata information about the request or response and play a crucial role in various aspects of web browsing, including content negotiation, authentication, caching, and security.

# Types of HTTP Headers

* Request Headers: 

Sent by the client to the server to provide additional information about the request or the client itself. Examples include User-Agent, Accept, and Authorization headers.

* Response Headers:

Sent by the server to the client to convey information about the response or the server itself. Examples include Content-Type, Cache-Control, and Server headers.

HTTP headers can be manipulated and customized to control web server behavior, optimize performance, and enhance security.

# Debian/Ubuntu HAProxy Packages

# Installation

HAProxy packages are readily available for installation on Debian-based Linux distributions such as Ubuntu. The installation process typically involves using package management tools like apt to download and install the required HAProxy packages from official repositories.

# Configuration

After installation, HAProxy can be configured using configuration files located in /etc/haproxy. These files define frontend, backend, and listen sections to specify how HAProxy should handle incoming requests, route traffic to backend servers, and manage load balancing algorithms.

The configuration files allow customization of various parameters, including timeouts, load balancing algorithms, health checks, SSL termination, and access control lists (ACLs).

# Setup Instructions

To set up the web server redundancy, follow these steps:

* Configure Load Balancer (gc-[STUDENT_ID]-lb-01-XXXXXXXXXX):

Install and configure HAProxy on the load balancer server to distribute incoming traffic among multiple web servers.

* Set Up Web Servers (gc-[STUDENT_ID]-web-01-XXXXXXXXXX and gc-[STUDENT_ID]-web-02-XXXXXXXXXX):

Configure Apache/Nginx and PHP/Python/Node.js on the web servers to serve web content.
Ensure that the web servers are properly configured to communicate with the load balancer.

* Automation Scripts:

Write Bash scripts to automate the configuration process for setting up new Ubuntu servers with the necessary software and settings.
These scripts should handle installation, configuration, and any necessary updates for HAProxy, Apache/Nginx, and other required components.
