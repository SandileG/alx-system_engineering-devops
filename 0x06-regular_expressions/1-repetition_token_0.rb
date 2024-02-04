#!/usr/bin/env ruby

# Ensure an argument is provided
if ARGV.length != 1
  puts "Usage: #{$PROGAM_NAME} <string>"
  exit 1
end

# The regular expression to match "School"
regexp = /hbt{2,5}n/

# Extracting the argument
input = ARGV[0]

# Using the match method to find the first occurence of the pattern
matches = input.scan(regexp)

# Check if there is a match and print the result
if matches.empty?
  puts ""
else
  puts matches.join
end
