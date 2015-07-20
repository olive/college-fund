#!/usr/bin/env python3

import cgi
import cgitb; cgitb.enable()  # for troubleshooting

print("Content-type: text/html")
print()

print("""
<html>

<head><title>Sample CGIs Script</title></head>

<body>

  <h3> Sample CGI Script </h3>

</body>

</html>
""")
