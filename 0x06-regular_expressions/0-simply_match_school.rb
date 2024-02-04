#!/usr/bin/env ruby

input = ARGV[0]

# The regular expression to match "School"
regexp = /School/

# Using scan to find all matches in the input
matches = input.scan(regexp)

# Joining and printing the matches
puts matches.join
