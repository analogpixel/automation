#
# you will need to install
# http://wkhtmltopdf.org/index.html
# https://github.com/JazzCore/python-pdfkit

import pdfkit
import optparse
import glob
import sys

# todo:
# fix sorting order of pictures
# pull video apart if needed, make it padded for easier sorting
# c:\bin\ffmpeg -i a.mp4 -ss 00:00:19 -t 10 -vf fps=10 out_%d.png

defpath="c:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

print defpath

parser = optparse.OptionParser()
parser.add_option("-d", "--directory", default="./",  help='directorty of images', dest="directory", action="store")
parser.add_option("-f", "--fileglob", default="*", help='files to use', dest="files", action="store")
parser.add_option("-o", "--ouput", default="images.pdf" , help='output pdf', dest="outname", action="store")
parser.add_option("-p", "--path", default=defpath, help="path to wkhtmltopdf", dest="defpath", action="store")
parser.add_option("-w", "--width", default="250", help="width of images", dest="width", action="store")
parser.add_option("-g", "--padding", default="5", help="height of images", dest="padding", action="store")
(opts, args) = parser.parse_args()


html = "<div>"

for files in glob.glob(opts.directory + opts.files):
  html = html + "<img style='padding: %s; width:%s; float:left' src=\"file:///%s\">" % (opts.padding, opts.width , files)

html = html + "</div>"



config = pdfkit.configuration(wkhtmltopdf=opts.defpath)
pdfkit.from_string(html, opts.outname, configuration=config)
