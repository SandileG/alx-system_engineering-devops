# Web server

# Main Role of a Web Server

A web server primarily serves web content to clients over the internet. It handles client requests and responds with the appropriate content, which may include web pages, images, files, or other resources.

# Child Process

A child process is a subprocess spawned by another process, known as the parent process. In the context of web servers, child processes are often used to handle incoming client requests.

# Parent and Child Processes in Web Servers

Web servers typically employ a parent-child process model to handle concurrent client connections efficiently. The parent process listens for incoming requests and spawns multiple child processes to handle them concurrently. This architecture allows the web server to scale and handle high volumes of traffic.

# Main HTTP Requests

The main HTTP requests are:

* GET: Requests data from a specified resource.
* POST: Submits data to be processed to a specified resource.
* PUT: Updates a specified resource.
* DELETE: Deletes a specified resource.

# DNS

# DNS Overview

DNS stands for Domain Name System. It is a hierarchical decentralized naming system for computers, services, or other resources connected to the internet or a private network. DNS translates domain names into IP addresses, allowing users to access resources by human-readable names rather than numerical IP addresses.

# Main Role of DNS

The main role of DNS is to translate domain names into IP addresses and vice versa. This translation enables users to access websites, services, and resources using domain names, which are easier to remember and use than IP addresses.

# DNS Record Types

* A Record

An A record (Address Record) maps a domain name to an IPv4 address. It resolves a domain name to the corresponding IP address.

* CNAME Record

A CNAME record (Canonical Name Record) is used to alias one domain name to another. It allows a domain to resolve to another domain's canonical (true) domain name.

* TXT Record

A TXT record (Text Record) is used to store text-based information associated with a domain. It can be used for various purposes such as SPF (Sender Policy Framework), DKIM (DomainKeys Identified Mail), or other types of authentication and verification.

* MX Record

An MX record (Mail Exchange Record) specifies the mail server responsible for receiving email messages on behalf of a domain. It directs email traffic to the appropriate mail server for delivery.
