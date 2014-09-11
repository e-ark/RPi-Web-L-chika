#!/bin/sh -vx
#
# CGI Button API(JSON)
#
# Wed May 15 23:58:09 JST 2013
#

exec  2> /tmp/log.$(basename $0)

# Settings
PIN=4

gpio -g mode $PIN out

# Exec
value=$(gpio -g read $PIN)
date=$(date +"%s")

# Output
echo "Content-type:application/json"
echo ""

echo '[ {"data": "'$value'", "time": "'$date'"} ]'

exit 0
