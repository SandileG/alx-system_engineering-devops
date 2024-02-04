#!/usr/bin/env ruby

# Ensure an argument is provided
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME <phone_number>}"
  exit 1
end

# The regular expression to match a 10-digit phone number
regexp = /^\d{10}$/

# Extracting the argument
phone_number = ARGV[0]

# Check if the input matches the pattern
if (match = phone_number.match(regexp))
  puts match[0]
else
  puts ""
end
