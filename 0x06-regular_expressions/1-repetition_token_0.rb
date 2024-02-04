#!/usr/bin/env ruby

# Ensure an argument is provided
if ARGV.length != 1
  puts "Usage: #{$PROGAM_NAME} <string>"
  exit 1
end

# The regular expression to match "School"
regexp = /School/

# Extracting the argument
input = ARGV[0]

# Using the match method to find the first occurence of the pattern
match_result = input.match(regexp)

# Check if there is a match and print the result
if match_result
  puts match_result[0]
else
  puts "No match found."
end
