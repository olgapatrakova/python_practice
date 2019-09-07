items = ['first string', 'second string']
html_str = "<ul>\n"

### Create a single string which is an HTML list
for i in range(len(items)):
    html_str += "<li>" + items[i] + "</li>\n"
html_str += "</ul>"

print(html_str)