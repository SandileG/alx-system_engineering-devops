# Web Infrastructure Design Project

This project aims to provide an overview of the web stack built through the SysAdmin/DevOps track projects. It includes a diagram illustrating the components of the web stack, explanations of each component's function, and discussions on system redundancy and key acronyms.

# Diagram of Web Stack

#Component Explanations

LAMP Stack
The LAMP stack consists of four key components: Linux, Apache, MySQL, and PHP.

Linux: The operating system (OS) that provides the foundation for hosting the web applications.
Apache: The web server software responsible for serving web pages to clients.
MySQL: The relational database management system (RDBMS) used to store and manage website data.
PHP: The programming language used for server-side scripting to generate dynamic web content.
System Redundancy
System redundancy involves duplicating critical components within a system to ensure high availability and fault tolerance. Redundancy can be implemented at various levels, including hardware, software, and network infrastructure. By having redundant systems, organizations can minimize the risk of single points of failure (SPOFs) and maintain system functionality in the event of failures.

# SPOF (Single Point of Failure)

SPOF refers to any component within a system whose failure can lead to the complete shutdown or significant degradation of system functionality. Identifying and mitigating SPOFs is crucial for ensuring system reliability and availability. Redundancy and fault-tolerant design strategies are often employed to eliminate or minimize the impact of SPOFs.

# QPS (Queries Per Second)

QPS is a metric used to measure the rate at which queries or requests are processed by a system within a specified timeframe, typically per second. It is commonly used to assess the performance and scalability of web applications and databases. Optimizing QPS involves improving system efficiency, resource utilization, and response times to handle increasing user demand effectively.
