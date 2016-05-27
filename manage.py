#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geek.settings")
>>>>>>> bd9cea1f0f6bfeab6f641d3bfc2f40e31c03e375

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
