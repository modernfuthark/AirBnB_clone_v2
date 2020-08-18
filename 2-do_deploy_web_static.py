#!/usr/bin/python3
""" 2-do_deploy_web_static """
import os
from datetime import datetime
from fabric.api import *


env.hosts = ['35.227.17.143']
# , '35.190.159.240']


def do_pack():
    """ does the packing """
    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(dt)

    local("mkdir -p versions")
    local("tar -czvf {} web_static".format(file_name))
    if os.path.exists(file_name):
        return file_name
    return None


def do_deploy(archive_path):
    """ Deploys package """
    if os.path.exists(archive_path):
        try:
            put(archive_path, "/tmp/")

            fsplit = archive_path.split("/")
            # 'foo/bar.egg' -> "foo", "bar.egg"

            file_name = fsplit[1].split(".")
            # 'bar.egg' -> "bar", "egg"

            run("sudo mkdir -p /data/web_static/releases/{}/".
                format(file_name[0]))
            run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
                .format(fsplit[1], file_name[0]))
            run("sudo rm /tmp/{}".format(fsplit[1]))
            run("sudo mv /data/web_static/releases/{}/web_static/*\
                 /data/web_static/releases/{}/".format(fsplit[0], fsplit[0]))
            run("sudo rm -rf /data/web_static/releases/{}/web_static"
                .format(fsplit[0]))
            run("sudo rm -rf /data/web_static/current")
            run("sudo ln -s /data/web_static/releases/{}\
                 /data/web_static/current".format(fsplit[0]))
            return True
        except Exception:
            return False
    return False
