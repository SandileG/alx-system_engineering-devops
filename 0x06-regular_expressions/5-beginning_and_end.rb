#!/usr/bin/env ruby

# Ensure an argument is provided
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# The regular expression to match "h...n" where '...' can be any single characher
regexp = /^hn$|^h.n$/

# Extracting the argument
input = ARGV[0]

# Check if the iput matches the pattern
if input.match?(regexp)
  puts input
else
  puts ""
end
