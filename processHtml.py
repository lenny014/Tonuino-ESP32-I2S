#!/usr/bin/python
###
# Use this script for creating PROGMEM header files from html files.
##
# html file base names
HTML_FILES = ["management", "accesspoint"]

class htmlHeaderProcessor(object):

    def html_to_c_header(self, filename):
        content = ""
        with open('html/' + filename + '.html', 'r') as r:
            data = r.read()
            data = data.replace('\n', '\\\n')
            data = data.replace('\"', '\\"')
            data = data.replace('\\d', '\\\d')
            data = data.replace('\\.', '\\\.')
            data = data.replace('\\^', '\\\\^')
            data = data.replace('%;', '%%;')
            content += data
        return content

    def write_header_file(self, filename, content):
        with open('src/HTML' + filename + '.h', 'w') as w:
            w.write("static const char " + filename + "_HTML[] PROGMEM = \"")
            w.write(content)
            w.write("\";")

    def main(self):
        for file in HTML_FILES:
           self.header_file_content = self.html_to_c_header(file)
           self.write_header_file(file, self.header_file_content)

if __name__ == '__main__':
    htmlHeaderProcessor().main()