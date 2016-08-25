
from collections import OrderedDict as OD
from util import Data, control_cb, monitor_cb, alarm_trace_cb, dev_io_cb
from sg.gui.ADRF6516 import get_lpf_ctrl

def get_ctrl(dev):
    ctrl = Data(name='RF', send=True, io_cb=dev_io_cb)
    ctrl.add('freq', label='Frequency, MHz', wdgt='spin', value=Data.spn(356.25, 2850, 0.01))
    ctrl.add('rfgain', label='RF Gain, dB', wdgt='spin', text='0.0', value=Data.spn(-13.5, 18, 0.5))
    ctrl.add_page('BB')
    ctrl.add('bbgain', label='Analog Gain, dB', wdgt='spin', value=Data.spn(0, 64.5, 0.5))
    get_lpf_ctrl(ctrl, 'bblpf')
    ctrl.add_page('DSP')
    ctrl.add('dsplpf', label='Filter, MHz', wdgt='combo', state='readonly', value=['10', '20'], text='10')
    ctrl.add_page('TEST')
    ctrl.add('test', label='Nothing', send=False)
    return ctrl

def get_mntr(dev):
    mntr = Data(io_cb=dev_io_cb)
    mntr.add_page('mntr', send=True)
    mntr.add('synth', wdgt='alarm', trace_cb=alarm_trace_cb, msg='Synthesizer status')
    mntr.add('uout', wdgt='entry', state='readonly', msg='Uout, V')
    mntr.add_page('mntr1', send=True)
    mntr.add('vcm1', label='VCM1', wdgt='entry', state='readonly', msg='VCM1')
    mntr.add('vcm2', label='VCM2', wdgt='entry', state='readonly', msg='VCM2')
    mntr.add('5v_1', label='5V_1', wdgt='entry', state='readonly', msg='5V_1')
    mntr.add('5v_2', label='5V_2', wdgt='entry', state='readonly', msg='5V_2')
    mntr.add('3v3_1', label='3V3_1', wdgt='entry', state='readonly', msg='3V3_1')
    mntr.add('3v3_2', label='3V3_2', wdgt='entry', state='readonly', msg='3V3_2')
    mntr.add('3v3_3', label='3V3_3', wdgt='entry', state='readonly', msg='3V3_3')
    mntr.add('14v', label='14v', wdgt='entry', state='readonly', msg='14v')
    mntr.cmds.columns=2
    return mntr

def get_menu(dev):
    return OD([('Control', control_cb), ('Monitor', monitor_cb)])
