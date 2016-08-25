
from util import find_from_table
from ctl.srv.STM32ETH import STM32ETH_telnet as telnet
from sg.gui.ADRF6820 import adrf_get_freq, adrf_set_freq
from sg.gui.LMP92018 import adc_dac_fmt_cb

def BR1IV2_freq(ip_addr='192.168.0.1', freq=''):
    """
    Чтение/установка частоты синтезатора
    @param ip_addr - ip-адрес устройства
    @param freq - частота, МГц (356.25..2850)
    @return freq
    """
    if freq:
        r02, r03, r04, r21, r22 = adrf_set_freq(float(freq), 24)
        telnet(ip_addr, 'spi 2.b6 0x%.2X%.4X 0 0' % (22 << 1, r22))
        telnet(ip_addr, 'spi 2.b6 0x%.2X%.4X 0 0' % (21 << 1, r21))
        telnet(ip_addr, 'spi 2.b6 0x%.2X%.4X 0 0' % (4 << 1, r04))
        telnet(ip_addr, 'spi 2.b6 0x%.2X%.4X 0 0' % (3 << 1, r03))
        telnet(ip_addr, 'spi 2.b6 0x%.2X%.4X 0 0' % (2 << 1, r02))
        return freq
    def reg_io(r):
        n = int(r[1:], 16)
        try:
            return int(telnet(ip_addr, 'spi 2.b6 0x%.2XFFFF 0 0' % ((n << 1) | 0x01)), 16) & 0xFFFF
        except:
            return '0'
    try:
        freq = adrf_get_freq(reg_io, 24)
        return '%g' % round(freq, 2)
    except:
        return ''

def BR1IV2_rfgain(ip_addr='192.168.0.1', gain=''):
    """
    Чтение/установка усиления канала (ВЧ)
    @param ip_addr - ip-адрес устройства
    @param gain - усиление, дБ (-13.5..18)
    @return gain
    """
    if gain:
        g = float(gain)
        if g < -13.5:
            g = -13.5
        if g > 18:
            g = 18
        g = round(2*(g + 13.5))
        return telnet(ip_addr, 'spi 2.d9 0x%.2X 0 0' % g)
    else:
        return '0'

def BR1IV2_bblpf(ip_addr='192.168.0.1', lpf=''):
    if lpf:
        return telnet(ip_addr, 'spi 2.b7 %s 0 0' % lpf)
    else:
        return telnet(ip_addr, 'spi 2.b7 0x7FFF 0 0')

def BR1IV2_bbgain(ip_addr='192.168.0.1', gain=''):
    """
    Чтение/установка усиления канала (НЧ)
    @param ip_addr - ip-адрес устройства
    @param gain - усиление, дБ (0..64.5)
    @return gain
    """
    if gain:
        g = float(gain)*15.5e-3
        g = adc_dac_fmt_cb(g, False, refin=1, n=3, a=0x50)
        telnet(ip_addr, 'spi 2.d8 %s 1 0' % g)
        return gain
    else:
        v = telnet(ip_addr, 'spi 2.d8 0xD30000 1 0; spi 2.d8 0x00FFFF 1 0')
        v = adc_dac_fmt_cb(v, True, refin=1, prc=5)
        v = float(v)/15.5e-3
        return '%g' % (round(v * 2) / 2)

def BR1IV2_synth(ip_addr='192.168.0.1'):
    """
    Чтение состояния синтезатора канала
    @param ip_addr - ip-адрес устройства
    @return - 1 или 0
    """
    v = telnet(ip_addr, 'spi 2.d8 0xB00000 1 0; spi 2.d8 0x00FFFF 1 0')
    try:
        return '0' if int(v, 16) & 0x000080 else '1'
    except:
        return '0'

def BR1IV2_uout(ip_addr='192.168.0.1'):
    """
    Чтение выходного напряжения канала
    @param ip_addr - ip-адрес устройства
    @return - напряжение, от 0 до 10 В
    """
    v = telnet(ip_addr, 'uart 2 mr pio_uout \\n')
    try:
        v = int(v, 16)
        _t = {0x00:0, 0x3FF:10}
        v = find_from_table(_t, v)
        return '%.2f' % v
    except:
        return '0'

def BR1IV2_vcm1(ip_addr='192.168.0.1'):
    v = telnet(ip_addr, 'spi 2.d8 0xE10000 1 0; spi 2.d8 0x00FFFF 1 0')
    v = adc_dac_fmt_cb(v, True)
    return v

def BR1IV2_vcm2(ip_addr='192.168.0.1'):
    v = telnet(ip_addr, 'spi 2.d8 0xE50000 1 0; spi 2.d8 0x00FFFF 1 0')
    v = adc_dac_fmt_cb(v, True)
    return v

def BR1IV2_5v_1(ip_addr='192.168.0.1'):
    v = telnet(ip_addr, 'spi 2.d8 0xE40000 1 0; spi 2.d8 0x00FFFF 1 0')
    v = adc_dac_fmt_cb(v, True, refin=10)
    return v

def BR1IV2_5v_2(ip_addr='192.168.0.1'):
    v = telnet(ip_addr, 'spi 2.d8 0xE70000 1 0; spi 2.d8 0x00FFFF 1 0')
    v = adc_dac_fmt_cb(v, True, refin=10)
    return v

def BR1IV2_3v3_1(ip_addr='192.168.0.1'):
    v = telnet(ip_addr, 'spi 2.d8 0xE00000 1 0; spi 2.d8 0x00FFFF 1 0')
    v = adc_dac_fmt_cb(v, True, refin=10)
    return v

def BR1IV2_3v3_2(ip_addr='192.168.0.1'):
    v = telnet(ip_addr, 'spi 2.d8 0xE30000 1 0; spi 2.d8 0x00FFFF 1 0')
    v = adc_dac_fmt_cb(v, True, refin=10)
    return v

def BR1IV2_3v3_3(ip_addr='192.168.0.1'):
    v = telnet(ip_addr, 'spi 2.d8 0xE60000 1 0; spi 2.d8 0x00FFFF 1 0')
    v = adc_dac_fmt_cb(v, True, refin=10)
    return v

def BR1IV2_14v(ip_addr='192.168.0.1'):
    v = telnet(ip_addr, 'spi 2.d8 0xE20000 1 0; spi 2.d8 0x00FFFF 1 0')
    v = adc_dac_fmt_cb(v, True, refin=43)
    return v

def BR1IV2_dsplpf(ip_addr='192.168.0.1', lpf=''):
    if lpf:
        v = '0'
        if lpf == '10':
            v = '0'
        if lpf == '20':
            v = '1'
        return telnet(ip_addr, 'uart 2 mw pio_fir0_bankn %s \\n' % v)
    else:
        v = telnet(ip_addr, 'uart 2 mr pio_fir0_bankn \\n')
        if v == '0':
            return '10'
        if v == '1':
            return '20'
    return ''

