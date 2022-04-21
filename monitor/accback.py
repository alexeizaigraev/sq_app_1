# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

import os
import shutil
from pathlib import Path
from modules import *
from datetime import datetime
import shutil

from papa_pg import select_deps_to_file, select_terms_to_file

def accback():
    info = ''
    info += select_terms_to_file()
    info += select_deps_to_file()
    return info

        