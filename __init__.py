
from . import gui, srv
from util.columns import *
from util.misc import app_devtypes

devdata = lambda: get_devdata('BR', get_columns([c_ip_addr]), app_devtypes(gui))

