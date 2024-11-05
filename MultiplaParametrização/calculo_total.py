def calculate_total(preco, taxa_desconto, taxa):
    desconto = preco * taxa_desconto
    imposto = (preco - desconto) * taxa
    total= preco - desconto + imposto
    return round (total,2)