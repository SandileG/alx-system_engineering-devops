#!/usr/bin/env ruby

# Ensure an argument is provided
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} '<log_entry>'"
  exit 1
end

# Extracting the log entry
log_entry = ARGV[0]

# Regular expression to extract relevant information
regexp = /\[from:([^\]]+)\] \[to:([^\]]+)\] \[flags:([^\]]+)\]/

# Exracting sender, receiver, and flags using match
match = log_entry.match(regexp)

# Chexk if there is match and pront the result
if match
  sender = match[1]
  receiver = match[2]
  flags = match[3]

  puts "#{sender},#{receiver},#{flags}"
else
  puts ""
end
