
from ctl.srv.SAM7X import SAM7X_telnet as telnet

def BR1I_freq(ip_addr='192.168.0.1', freq=''):
    """
    Чтение/установка частоты синтезатора
    @param ip_addr - ip-адрес устройства
    @param freq - частота, МГц (950..2150)
    @return freq
    """
    return telnet(ip_addr, 'freq', freq)

def BR1I_rfgain(ip_addr='192.168.0.1', gain=''):
    """
    Чтение/установка усиления канала (ВЧ)
    @param ip_addr - ip-адрес устройства
    @param gain - усиление, дБ (0..50)
    @return gain
    """
    return telnet(ip_addr, 'rfgain', gain)

def BR1I_bbgain(ip_addr='192.168.0.1', gain=''):
    """
    Чтение/установка усиления канала (НЧ)
    @param ip_addr - ip-адрес устройства
    @param gain - усиление, дБ (0..50)
    @return gain
    """
    return telnet(ip_addr, 'bbgain', gain)

def BR1I_lpf(ip_addr='192.168.0.1', lpf=''):
    """
    Чтение/установка полосы канала
    @param ip_addr - ip-адрес устройства
    @param lpf - полоса, МГц (10 или 20)
    @return lpf
    """
    return telnet(ip_addr, 'lpf', lpf)

def BR1I_synth(ip_addr='192.168.0.1'):
    """
    Чтение состояния синтезатора канала
    @param ip_addr - ip-адрес устройства
    @return - 1 или 0
    """
    return telnet(ip_addr, 'synth')

def BR1I_uout(ip_addr='192.168.0.1'):
    """
    Чтение выходного напряжения канала
    @param ip_addr - ip-адрес устройства
    @return - напряжение, от 0 до 10 В
    """
    return telnet(ip_addr, 'uout')

def BR1I_commit(ip_addr='192.168.0.1', en=''):
    """
    Сохранение данных в EFC flash
    @param en - вкл/выкл сохранение данных ("ON" или "OFF") 
    @n пустая строка - чтение
    @return en
    """
    return telnet(ip_addr, 'efc commit %s' % en)

