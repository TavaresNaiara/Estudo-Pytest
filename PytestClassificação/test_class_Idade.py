import pytest
from class_idd import classifica_idade

@pytest.mark.parametrize("idade, categoria_esperada", [ 
    (10, "criança"),
    (15, "adolescente"),
    (30, "adulto"),
    (70, "idoso"),
])
def test_classifica_idade(idade, categoria_esperada):
    assert classifica_idade(idade) == categoria_esperada
