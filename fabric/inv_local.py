#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""This collection is used to test the functionality of DjangoVue before deployment."""

import os
import sys
from invoke import task
from inv_base import docker_compose, manage_py


@task
def rebuild(c):
    """This function is used to recreate the docker containers."""
    docker_compose(c, "build")


@task
def npm(c, cmd, **kwargs):
    """This function is used to respond to the packet manager npm."""
    uid = "{}:{}".format(os.getuid(), os.getgid())
    docker_compose(c, f"run -u {uid} vue npm {cmd}", pty=True)


@task
def build(c, **kwargs):
    """This function is used to respond to the packet manager npm."""
    uid = "{}:{}".format(os.getuid(), os.getgid())
    docker_compose(c, f"run -u {uid} vue npm run build", pty=True)
    manage_py(c, "migrate")
    manage_py(c, "collectstatic -v 0 --no-input")


@task
def serve(c):
    """This function is used to start the development environment."""
    docker_compose(c, f"up")


@task
def run(c, cmd, **kwargs):
    """The function is used to start a command inside a django container."""
    uid = "{}:{}".format(os.getuid(), os.getgid())
    return docker_compose(c, f"run -u {uid} {cmd}", pty=True)
