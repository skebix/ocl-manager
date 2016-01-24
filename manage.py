#!/usr/bin/env python

from os.path import join, dirname, abspath
from dotenv import load_dotenv

dotenv_path = join(dirname(abspath(__file__)), '.env')
load_dotenv(dotenv_path)

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestor_ocl.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
