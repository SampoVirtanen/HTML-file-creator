import subprocess
import os
import shutil
nimi = input("Anna projektin nimi: ")
sijainti = "C:/Output/{}".format(nimi)
if not os.path.exists(sijainti):
    os.makedirs(sijainti)
sijaintiBS = "C:/Output/{}/BS".format(nimi)
if not os.path.exists(sijaintiBS):
    os.makedirs(sijaintiBS)
sijainticss = "C:/Output/{}/css".format(nimi)
if not os.path.exists(sijainticss):
    os.makedirs(sijainticss)
sijaintijs = "C:/Output/{}/js".format(nimi)
if not os.path.exists(sijaintijs):
    os.makedirs(sijaintijs)
sijaintikuvat = "C:/Output/{}/kuvat".format(nimi)
if not os.path.exists(sijaintikuvat):
    os.makedirs(sijaintikuvat)
src_css = "C:/Input/BS/bootstrap.min.css"
dst_css = "C:/Output/{}/BS/bootstrap.min.css".format(nimi)
shutil.copy(src_css, dst_css)
src_js = "C:/Input/BS/bootstrap.min.js"
dst_js = "C:/Output/{}/BS/bootstrap.min.js".format(nimi)
shutil.copy(src_js, dst_js)
src_style = "C:/Input/css/style.css"
dst_style = "C:/Output/{}/css/style.css".format(nimi)
shutil.copy(src_style, dst_style)
src_script = "C:/Input/js/script.js"
dst_script = "C:/Output/{}/js/script.js".format(nimi)
shutil.copy(src_script, dst_script)
src_html = "C:/Input/index.html"
dst_html = "C:/Output/{}/index.html".format(nimi)
shutil.copy(src_html, dst_html)
sijainti = sijainti.replace('/', '\\')
subprocess.Popen(r'explorer /select,"' + sijainti + '"')
