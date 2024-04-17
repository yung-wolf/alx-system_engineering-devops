## Regular Expressions Project
Build a regular expression using Oniguruma, a regular expression library which is used by Ruby by default.

### Sample code to test Regex with (replace the regexp part, meaning the code in between the //)
```
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
```

## Environment
- OS: Ubuntu 20.04 LTS
- Language: Ruby
- Usage: ./[filename] "[Pattern to match]" | cat -e

## Author
yung-wolf
