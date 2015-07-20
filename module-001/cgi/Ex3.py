#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A "webserver" is a computer program which listens to the internet and
# responds to http commands by sending web pages, running scripts, and
# updating internal state such as page views, data entered, or whatever.

# apache2 is a very common webserver which we will be using.

# Our domain name is strob.ilu.moe. We send requests to apache2 by
# entering urls which begin with this string.

# For example, by visiting http://strob.ilu.moe/index.html in a webbrowser,
# apache2 will "serve" the file /var/www/index.html (this is a linux filepath,
# you can think of it like C:/var/www/index.html in windows. fuck macs i
# have no clue ┐(´-｀)┌ )

# (?) http in urls is the "protocol" you are requesting from the server.
# http means The Hypertext Transfer Protocol and is widely used for the web.
# Other examples are irc:/, twitter:/, and git:/.

# A "cgi" script is a special sort of webpage that prompts the webserver
# to run a program which generates a dynamic web page, rather than
# serving a static page. This very script is an example of a cgi script.

# cgi scripts work by printing to stdout (the place that calls to `print` go
# by default) the contents of the html webpage to be shown to the client.

# I have already had the pleasure of configuring apache2 such that
# requests to the cgi subfolder will be run through the `python3` interpreter.
# You're welcome.

# ignore magic
import cgi
import cgitb
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
cgitb.enable()  # for troubleshooting
# magic over


# All cgi scripts serving html must begin with the "header" which consist of:

print("Content-type: text/html")
print("")

try:
    # Then, anything you print will appear on the page in HTML syntax.
    print("""
    <html>
        <meta charset="UTF-8">
        <head><title>website title</title></head>
        <body>
            <h1>test</h1>
            <p>ﾟ･✿ヾ╲(｡◕‿◕｡)╱✿･ﾟ</p>
        </body>
    </html>
    """)
except Exception as e:
    print(e)

