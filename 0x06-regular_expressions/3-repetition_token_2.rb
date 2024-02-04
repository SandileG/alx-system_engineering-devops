#!/usr/bin/env ruby
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# The regular expression to match "hbtn", "hbttn", "hbt...tn" where 't' can occur 1 or more times
regexp = /hbt+n/

# Extracting the argument
input = ARGV[0]

# Using scan method to find all occurrences of the pattern
matches = input.scan(regexp)

# Chexk if there are matches and pront the result
if matches.empty?
  puts ""
else
  puts matches.join
end
