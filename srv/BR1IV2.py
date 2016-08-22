
from util import find_from_table
from ctl.srv.STM32ETH import STM32ETH_telnet as telnet

def BR1IV2_freq(ip_addr='192.168.0.1', freq=''):
    """
    Чтение/установка частоты синтезатора
    @param ip_addr - ip-адрес устройства
    @param freq - частота, МГц (950..2150)
    @return freq
    """
    return telnet(ip_addr, 'freq', freq)

def BR1IV2_rfgain(ip_addr='192.168.0.1', gain=''):
    """
    Чтение/установка усиления канала (ВЧ)
    @param ip_addr - ip-адрес устройства
    @param gain - усиление, дБ (0..50)
    @return gain
    """
    return telnet(ip_addr, 'rfgain', gain)

def BR1IV2_bbgain(ip_addr='192.168.0.1', gain=''):
    """
    Чтение/установка усиления канала (НЧ)
    @param ip_addr - ip-адрес устройства
    @param gain - усиление, дБ (0..50)
    @return gain
    """
    return telnet(ip_addr, 'bbgain', gain)

def BR1IV2_lpf(ip_addr='192.168.0.1', lpf=''):
    """
    Чтение/установка полосы канала
    @param ip_addr - ip-адрес устройства
    @param lpf - полоса, МГц (10 или 20)
    @return lpf
    """
    return telnet(ip_addr, 'lpf', lpf)

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

