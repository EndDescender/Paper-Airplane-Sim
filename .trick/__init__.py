from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
import sys
import os
sys.path.append(os.getcwd() + "/trick.zip/trick")

import _sim_services
from sim_services import *

# create "all_cvars" to hold all global/static vars
all_cvars = new_cvar_list()
combine_cvars(all_cvars, cvar)
cvar = None

# /home/bahram/trick_sims/SIM_paper_airplane/S_source.hh
import _m6df225a75723545a06d7f08324795258
combine_cvars(all_cvars, cvar)
cvar = None

# /home/bahram/trick_sims/SIM_paper_airplane/models/airplane/include/Airplane.hh
import _mf064c256b46431d6a9c6003406b00477
combine_cvars(all_cvars, cvar)
cvar = None

# /home/bahram/trick_sims/SIM_paper_airplane/S_source.hh
from m6df225a75723545a06d7f08324795258 import *
# /home/bahram/trick_sims/SIM_paper_airplane/models/airplane/include/Airplane.hh
from mf064c256b46431d6a9c6003406b00477 import *

# S_source.hh
import _m6df225a75723545a06d7f08324795258
from m6df225a75723545a06d7f08324795258 import *

import _top
import top

import _swig_double
import swig_double

import _swig_int
import swig_int

import _swig_ref
import swig_ref

from shortcuts import *

from exception import *

cvar = all_cvars

