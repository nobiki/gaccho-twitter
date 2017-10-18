#!/usr/bin/env python
# coding: utf-8
import pkg_resources

def foo():
    for dist in pkg_resources.working_set:
        print(dist.project_name, dist.version)
