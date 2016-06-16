
from collections import OrderedDict as OD
from util import Data, control_cb, monitor_cb, alarm_trace_cb, dev_io_cb

def synth_fmt_cb(val, read=True):
    if read:
        return '0' if val == '1' else '0'

def get_menu(dev):
    return OD([('Control', control_cb), ('Monitor', monitor_cb)])

def get_ctrl(dev):
    ctrl = Data(io_cb=dev_io_cb)
    for i in [1, 2]:
        ctrl.add_page('CH%d' % i, send=True)
        ctrl.add('freq%d'%i, label='Frequency, MHz', wdgt='spin', value=Data.spn(950, 2150, 0.01))
        ctrl.add('rfgain%d'%i, label='RF Gain, dB', wdgt='spin', value=Data.spn(0, 31.5, 0.5))
        ctrl.add('bbgain%d'%i, label='BB Gain, dB', wdgt='spin', value=Data.spn(0, 50, 0.1))
        ctrl.add('bblpf%d'%i, label='BB Filter, MHz', wdgt='spin', value=Data.spn(1, 30))
    ctrl.add_page('Other', send=True)
    ctrl.add('commit', label='EFC commit enable', wdgt='combo', state='readonly', value=['ON', 'OFF'])
    ctrl.add('dlpf', label='Digital LPF, MHz', wdgt='combo', state='readonly', value=['0.1','0.2','0.5','1','1.5','2','5','10','20'])
    return ctrl

def get_mntr(dev):
    mntr = Data(io_cb=dev_io_cb)
    mntr.add_page('mntr', send=True)
    mntr.add('synth1', wdgt='alarm', trace_cb=alarm_trace_cb, fmt_cb=synth_fmt_cb, msg='Synthesizer 1')
    mntr.add('synth2', wdgt='alarm', trace_cb=alarm_trace_cb, fmt_cb=synth_fmt_cb, msg='Synthesizer 2')
    mntr.add('uout1', wdgt='entry', state='readonly', msg='Uout1, V')
    mntr.add('uout2', wdgt='entry', state='readonly', msg='Uout2, V')
    mntr.add('uout3', wdgt='entry', state='readonly', msg='abs(Uout1-Uout2), V')
    return mntr

