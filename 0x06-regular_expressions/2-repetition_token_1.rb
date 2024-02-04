#!/usr/bin/env ruby

# Ensure an argument is provided
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <STRING>"
  exit 1
end

# The regular expression to match "hb?t?n"
regexp = /hb?t?n/

# Extracting the argument
input = ARGV[0]

# Using the scan method to find all occurrences of the pattern
matches = input.scan(regexp)

# Check if there are matches and print the result
if matches.empty?
  puts ""
else
  puts matches.join
end
