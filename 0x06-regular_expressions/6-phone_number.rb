#!/usr/bin/env ruby

# Ensure an argument is provided
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME <phone_number>}"
  exit 1
end

# The regular expression to match a 10-digit phone number
regexp = /^\d{10,10}$/

# Extracting the argument
phone_number = ARGV[0]

# Using the scan method to find all occurrences of the pattern
matches = phone_number.scan(regexp)

# Check if there are matches and print the result
if matches.empty?
  puts ""
else
  puts matches.join
end
