#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "sip-%s" % get.srcVERSION()

py2dir = get.curPYTHON()
py3dir = "python3.4"

def setup():    
    shelltools.cd("..")
    shelltools.makedirs("build_python3")
    shelltools.copytree("./%s" % WorkDir,  "build_python3")
    shelltools.cd(WorkDir)
    pythonmodules.run('configure.py CFLAGS+="%s" CXXFLAGS+="%s"' % (get.CFLAGS(), get.CXXFLAGS()))

    shelltools.cd("../build_python3/%s" % WorkDir)
    shelltools.system("find . -type f -exec sed -i 's/Python.h/python3.4m\/Python.h/g' {} \;")
    pythonmodules.run('configure.py CFLAGS="%s" CXXFLAGS="%s"' % (get.CFLAGS(), get.CXXFLAGS()), pyVer = "3")
                        

def build():
    autotools.make()

    shelltools.cd("../build_python3/%s" % WorkDir)
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.rename("/usr/bin/sip", "py2sip") 
    #pisitools.insinto("/usr/lib/python2.7/site-packages", "siputils.py")
    #pisitools.insinto("/usr/lib/python2.7/site-packages", "sipdistutils.py")

    shelltools.cd("../build_python3/%s" % WorkDir)
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.insinto("/usr/lib/python3.4/site-packages", "siputils.py")
    #pisitools.insinto("/usr/lib/python3.4/site-packages", "sipdistutils.py")