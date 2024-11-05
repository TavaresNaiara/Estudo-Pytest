import pytest
from calculo_total import calculate_total 

@pytest.mark.parametrize("preco", [10.00, 30.00, 70.00])
@pytest.mark.parametrize("taxa_desconto", [0, 0.1, 0.25])
@pytest.mark.parametrize("taxa", [0, 0.5, 0.1])
def test_calculate_total(preco, taxa_desconto, taxa):
    # Calculate the expected discount
    desconto_esperado = preco * taxa_desconto
    
    # Apply the discount to get the price after discountalculate_total
    preco_com_desconto = preco - desconto_esperado
    
    # Calculate the expected tax on the discounted price
    taxa_esperada = preco_com_desconto * taxa
    
    # Calculate the expected total
    total_esperado = preco_com_desconto + taxa_esperada
    
    # Assert that the result from calculate_total matches the expected total, rounded to two decimal places
    assert round(calculate_total(preco, taxa_desconto, taxa), 2) == round(total_esperado, 2)
