info=input('Digite algo: ')
print('01 - Seu tipo primitivo é: {}' .format (type(info)))
print('02 - Ele é alfanumérico: {}' .format (info.isalnum()))
print('03 - Ele é alfabetico?: {}' .format (info.isalpha()))
print('04 - ????: {}' .format (info.isascii()))
print('05 - Ele tem somente numeros: {}'.format(info.isdecimal()))
print('06 - ????: {}'.format(info.isdigit()))
print('07 - ????: {}'.format(info.isidentifier()))
print('08 - Ele tem somente letras minusculas: {}'.format(info.islower()))
print('09 - Ele é um numéro: {}'.format(info.isnumeric()))
print('10 - Ele pode ser impresso?{}: '.format(info.isprintable()))
print('11 - Ele só tem espaçamentos?{}'.format(info.isspace()))
print('12 - Está Capitalizada?: {}'.format(info.istitle())) #capitalizada quer dizer se tem letras maiusculas + minusculas                                           
print('13 - Ele tem somente letras maiusculas: {}'.format(info.isupper()))
