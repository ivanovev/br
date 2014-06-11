
from ctl.srv.SAM7X import SAM7X_telnet as telnet

def BR2I_freq1(ip_addr='192.168.0.1', freq=''):
    """
    Чтение/установка частоты синтезатора канала 1
    @param ip_addr - ip-адрес устройства
    @param freq - частота, МГц (950..2150)
    @n пустая строка - чтение
    @return freq
    """
    return telnet(ip_addr, 'freq1', freq)

def BR2I_freq2(ip_addr='192.168.0.1', freq=''):
    """
    Чтение/установка частоты синтезатора канала 2
    @param ip_addr - ip-адрес устройства
    @param freq - частота, МГц (950..2150)
    @n пустая строка - чтение
    @return freq
    """
    return telnet(ip_addr, 'freq2', freq)

def BR2I_rfgain1(ip_addr='192.168.0.1', gain=''):
    """
    Чтение/установка усиления канала 1 (ВЧ)
    @param ip_addr - ip-адрес устройства
    @param gain - усиление, дБ (0..50)
    @n пустая строка - чтение
    @return gain
    """
    return telnet(ip_addr, 'rfgain1', gain)

def BR2I_rfgain2(ip_addr='192.168.0.1', gain=''):
    """
    Чтение/установка усиления канала 2 (ВЧ)
    @param ip_addr - ip-адрес устройства
    @param gain - усиление, дБ (0..50)
    @n пустая строка - чтение
    @return gain
    """
    return telnet(ip_addr, 'rfgain2', gain)

def BR2I_bbgain1(ip_addr='192.168.0.1', gain=''):
    """
    Чтение/установка усиления канала 1 (НЧ)
    @param ip_addr - ip-адрес устройства
    @param gain - усиление, дБ (0..50)
    @n пустая строка - чтение
    @return gain
    """
    return telnet(ip_addr, 'bbgain1', gain)

def BR2I_bbgain2(ip_addr='192.168.0.1', gain=''):
    """
    Чтение/установка усиления канала 2 (НЧ)
    @param ip_addr - ip-адрес устройства
    @param gain - усиление, дБ (0..50)
    @n пустая строка - чтение
    @return gain
    """
    return telnet(ip_addr, 'bbgain2', gain)

def BR2I_bblpf1(ip_addr='192.168.0.1', lpf=''):
    """
    Чтение/установка полосы канала 1
    @param ip_addr - ip-адрес устройства
    @param lpf - полоса, МГц (1..30)
    @n пустая строка - чтение
    @return lpf
    """
    return telnet(ip_addr, 'bblpf1', lpf)

def BR2I_bblpf2(ip_addr='192.168.0.1', lpf=''):
    """
    Чтение/установка усиления канала 2
    @param ip_addr - ip-адрес устройства
    @param lpf - полоса, МГц (1..30)
    @n пустая строка - чтение
    @return lpf
    """
    return telnet(ip_addr, 'bblpf2', lpf)

def BR2I_synth1(ip_addr='192.168.0.1'):
    """
    Чтение состояния синтезатора канала 1
    @param ip_addr - ip-адрес устройства
    @n пустая строка - чтение
    @return - 1 или 0
    """
    return telnet(ip_addr, 'synth1')

def BR2I_synth2(ip_addr='192.168.0.1'):
    """
    Чтение состояния синтезатора канала 2
    @param ip_addr - ip-адрес устройства
    @n пустая строка - чтение
    @return - 1 или 0
    """
    return telnet(ip_addr, 'synth2')

def BR2I_uout1(ip_addr='192.168.0.1'):
    """
    Чтение выходного напряжения канала 1
    @param ip_addr - ip-адрес устройства
    @return - напряжение, от 0 до 10 В
    """
    return telnet(ip_addr, 'uout1')

def BR2I_uout2(ip_addr='192.168.0.1'):
    """
    Чтение выходного напряжения канала 2
    @param ip_addr - ip-адрес устройства
    @return - напряжение, от 0 до 10 В
    """
    return telnet(ip_addr, 'uout2')

def BR2I_uout3(ip_addr='192.168.0.1'):
    """
    Чтение выходного напряжения разностного канала
    @param ip_addr - ip-адрес устройства
    @return - напряжение, от 0 до 10 В
    """
    return telnet(ip_addr, 'uout3')

def BR2I_commit(ip_addr='192.168.0.1', en=''):
    """
    Сохранение данных в EFC flash
    @param en - вкл/выкл сохранение данных ("ON" или "OFF") 
    @n пустая строка - чтение
    @return en
    """
    return telnet(ip_addr, 'efc commit %s' % en)

def BR2I_dlpf(ip_addr='192.168.0.1', lpf=''):
    """
    Установить полосу цифрового фильтра
    @param lpf - полоса цифрового фильтра, МГц, что-то из списка:
    @n 0.1, 0.2, 0.5, 1, 1.5, 2, 5, 10, 20
    @n пустая строка - чтение
    @return c
    """
    return telnet(ip_addr, 'dlpf %s' % lpf)

