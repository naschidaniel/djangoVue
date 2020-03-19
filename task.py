#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""The fabricfile of the project."""

import os
from invoke import task, Collection, Program


def docker_compose(c, cmd, **kwargs):
    """A function to start docker-compose."""
    command = ["docker-compose"]
    for config_file in c.docker_compose_files:
        command.append("-f")
        command.append(config_file)

    command.append(cmd)
    command.insert(0, "export USERID=$UID && export GROUPID=$GID &&")

    return c.run(" ".join(command), **kwargs)

@task
def manage_py(c, cmd, **kwargs):
    """The function is used to start a command inside a container."""
    uid = "{}:{}".format(os.getuid(), os.getgid())
    return docker_compose(c, f"run -u {uid} fedora python3 /www/site/manage.py {cmd}", pty=True)

@task
def serve(c):
    """This function is used to recreate the docker containers."""
    docker_compose(c, "up")

@task
def nodebuild(c, **kwargs):
    """This function is used to recreate the docker containers."""
    uid = "{}:{}".format(os.getuid(), os.getgid())
    docker_compose(c, f"run -u {uid} node npm run build", pty=True)

@task
def test(c):
    """This function is used to recreate the docker containers."""
    docker_compose(c, "up web")

@task
def rebuild(c):
    """This function is used to recreate the docker containers."""
    docker_compose(c, "build")


MAIN_COLLECTION = Collection()

LOCAL_NS = Collection("local")
LOCAL_NS.configure({
    "docker_compose_files": [
        "./docker-compose.yml"
    ]
})
MAIN_COLLECTION.add_collection(LOCAL_NS)

LOCAL_NS.add_task(manage_py)
LOCAL_NS.add_task(serve)
LOCAL_NS.add_task(nodebuild)
LOCAL_NS.add_task(test)
LOCAL_NS.add_task(rebuild)

PROGRAM = Program(namespace=MAIN_COLLECTION)
PROGRAM.run()
