curl -s https://mlab.taik.fi/~timo/runo1.html | iconv -f ISO-8859-1 -t UTF-8 | sed -e 's/<[^>]*>//g' > poem.txt
cat poem.txt | while read line; do echo "$line"; sleep 0.5; done
