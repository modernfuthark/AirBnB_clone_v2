#!/usr/bin/python3
""" Pack Web Static """
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """ Generates a .tgz archive from web_static directory """
    # Generate filename
    time = datetime.now().timetuple()
    time_str = ""
    for index in range(0, 6):
        time_str = time_str + str(time[index])
    filename = "web_static_" + time_str + ".tgz"

    # Compress directory
    local("tar -czvf " + filename + " web_static")

    # Test if successful
    if os.path.exists(filename):
        return filename
    else:
        return None
