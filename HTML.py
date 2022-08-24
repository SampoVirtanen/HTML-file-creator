import subprocess
import os
import shutil
nimi=input("Anna projektin nimi: ")
sijainti = "C:/Output/{}".format(nimi)
if not os.path.exists(sijainti):
    os.makedirs(sijainti)
sijainticss = "C:/Output/{}/css".format(nimi)
if not os.path.exists(sijainticss):
    os.makedirs(sijainticss)
sijaintijs = "C:/Output/{}/js".format(nimi)
if not os.path.exists(sijaintijs):
    os.makedirs(sijaintijs)
src_css = "C:/Input/css/bootstrap.min.css"
dst_css = "C:/Output/{}/css/bootstrap.min.css".format(nimi)
shutil.copy(src_css, dst_css)
src_js = "C:/Input/js/bootstrap.min.js"
dst_js = "C:/Output/{}/js/bootstrap.min.js".format(nimi)
shutil.copy(src_js, dst_js)
src_html = "C:/Input/index.html"
dst_html = "C:/Output/{}/index.html".format(nimi)
shutil.copy(src_html, dst_html)
sijainti=sijainti.replace('/', '\\')
subprocess.Popen(r'explorer /select,"'+sijainti+'"')