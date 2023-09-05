import sympy

def numero_divisores(n):
    """
    Função para calcular o número de divisores de um número n.
    """
    divisors = sympy.divisors(n)
    return len(divisors)

def numeros_altamente_compostos(r):
    """
    Função para encontrar todos os números altamente compostos menores que r.
    """
    highly_composite_numbers = []
    max_divisors = 0
    
    for i in range(1, r):
        div_count = numero_divisores(i)
        if div_count > max_divisors:
            highly_composite_numbers.append(i)
            max_divisors = div_count

    return highly_composite_numbers

# Solicita a entrada do usuário
r = 5000

# Chama a função para encontrar os números altamente compostos
result = numeros_altamente_compostos(r)

# Imprime os números altamente compostos encontrados
print(f"Números altamente compostos menores que {r}:")
print(result)





