import pytest
import time

def soma( a, b):
    return a+b
def subitracao (a, b):
    return a-b 
def multiplicacao( a, b):
    return a*b
def sdivisao (a, b):
    return a/b 

@pytest.mark.lento
def test_somaa_lenta():
     time.sleep(2)
     assert soma(2,3) == 5

def test_subitracao_rapida():
     assert subitracao(5,3) == 2


@pytest.mark.lento
def test_multiplicacao_lenta():
     time.sleep(2)
     assert multiplicacao(3,3) == 9
