from funcoes import *

def test_email_valido():
    assert email_valido("nai@dominio.com") is True
    assert email_valido("nai.com") is False

def test_dividir():
    assert dividir(6,2)==3
    assert dividir(6,0) is None
    