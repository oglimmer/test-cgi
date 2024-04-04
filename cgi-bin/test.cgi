#!/bin/bash

set -f

TMP_IFS=$IFS

# Send necessary HTTP headers
echo "Content-Type: text/html"
echo ""  # This is necessary to separate headers from the body

# HTML content starts here
echo "<html>"
echo "<head>"
echo "<title>CGI Header Test</title>"
echo "</head>"
echo "<body>"
echo "<h1>HTTP Headers</h1>"
echo "<table>"
while IFS='=' read -r header value; do
  header_name=$(echo "$header" | sed 's/^HTTP_//;s/_/-/g')
  echo "<tr><td>$header_name</td><td>$value</td></tr>"
done < <(env | sort | grep -E '^HTTP_')
echo "</table>"

echo "<h1>Server variables</h1>"
echo "<table>"
while IFS='=' read -r header value; do
    echo "<tr><td>$header</td><td>$value</td></tr>"
done < <(env | sort | grep -vE '^HTTP_')
echo "</table>"

if [ "$REQUEST_METHOD" = "POST" ]; then
    IFS=$TMP_IFS
    echo "<h1>Request Body</h1>"
    echo "<pre>"
    read -r POST_DATA
    echo "$POST_DATA"
    echo "</pre>"
fi

echo "</body>"
echo "</html>"
