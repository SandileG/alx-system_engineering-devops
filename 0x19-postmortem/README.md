# Service Disruption Report

# Incident Report: Website Downtime

# Issue Summary:

During a ten-minute period on September 11th, 2018, from 9:39 AM to 9:49 AM UTC, our company's website experienced an outage, resulting in a 500 internal server error for all users. The root cause of the issue was identified as a misconfigured filename in a critical configuration file.

# Timeline:

9:39 AM: Deployment of a sitewide update; outage commences.
9:40 AM: DevOps team investigates error logs.
9:43 AM: Configuration updated to enable enhanced error logging.
9:45 AM: Discovery of filename error in configuration file.
9:47 AM: Execution of Puppet manifest across all company servers.
9:49 AM: Service fully restored; website back online.

# Root Cause and Resolution:

The outage was triggered by the deployment of an untested sitewide update, leading to server errors. Despite initial checks not revealing any issues in the error logs, further investigation with 'strace' uncovered an inadvertent filename misspelling in the '/var/www/html/wp-settings.php' file. The server failed to locate the file with the incorrect extension ".phpp" instead of ".php". Upon rectifying the filename, the website functionality was restored. Subsequently, a Puppet manifest was executed company-wide to ensure all servers were updated and operational.

# Corrective and Preventative Measures:

To mitigate similar incidents in the future, the following measures have been implemented:

Enhanced error logging in configuration files to expedite error identification and resolution.

Implementation of rigorous testing protocols for all updates before deployment across servers, regardless of size.
