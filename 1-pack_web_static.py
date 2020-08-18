#!/usr/bin/python3
""" 1-pack_web_static """
from os
from datetime import datetime
from fabric.api import local


def do_pack():
    """ does the packing """
    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(dt)

    local("mkdir -p versions")
    local("tar -czvf {} web_static".format(file_name))
    if os.path.exists(file_name):
        return file_name
    return None
