
from collections import OrderedDict as OD
from util.mainwnd import control_cb, monitor_cb
from util import Data, alarm_trace_cb, dev_io_cb
from .BR2I import synth_fmt_cb

def get_ctrl(dev):
    ctrl = Data('CH1', send=True, io_cb=dev_io_cb)
    ctrl.add('freq', label='Frequency, MHz', wdgt='spin', value=Data.spn(1350, 1750, 0.01))
    ctrl.add('rfgain', label='RF Gain, dB', wdgt='spin', value=Data.spn(0, 31.5, 0.5))
    ctrl.add('bbgain', label='BB Gain, dB', wdgt='spin', value=Data.spn(0, 50, 0.1))
    ctrl.add('lpf', label='Filter, MHz', wdgt='combo', state='readonly', value=['2', '4', '10', '20'], text='10')
    ctrl.add('commit', label='EFC commit enable', wdgt='combo', state='readonly', value=['ON', 'OFF'], text='ON')
    return ctrl

def get_mntr(dev):
    mntr = Data(io_cb=dev_io_cb)
    mntr.add_page('mntr', send=True)
    mntr.add('synth', wdgt='alarm', trace_cb=alarm_trace_cb, fmt_cb=synth_fmt_cb, msg='Synthesizer status')
    mntr.add('uout', wdgt='entry', state='readonly', msg='Uout, V')
    return mntr

def get_menu(dev):
    return OD([('Control', control_cb), ('Monitor', monitor_cb)])
