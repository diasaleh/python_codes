fname = "/Users/diasaleh/Downloads/watan-2004/sports/sports.html/capr16.html"

HtmlFile = open(fname, 'r', 'utf-8')
source_code = HtmlFile.read()

print (source_code)
HtmlFile.close()