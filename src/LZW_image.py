# Bibliotecas
from PIL import Image
import numpy as np
import os


# Função para realizar a compressão LZW
def lzw(original_vector):
    # Inicializar o dicionário
    LZW_dictionary = {}
    for i in range(0,256):
        LZW_dictionary[(i, )] = i

    # Gerar sequência codificada
    w = (original_vector[0], )

    compressed_vector = []
    next_codification = 256
    for k in map(int, original_vector[1:]):
        wk = w + (k, )

        if wk in LZW_dictionary:
            w = wk
        else:
            compressed_vector.append(LZW_dictionary[w])
            LZW_dictionary[wk] = next_codification
            next_codification += 1
            w = (k, );
    
    compressed_vector.append(LZW_dictionary[w])

    return compressed_vector, LZW_dictionary


# Pega o nome do arquivo
file_name = str(input("Digite o nome do arquivo: "))

# Ler a imagem em escala de cinza
image = Image.open(file_name).convert("L")

# Converte a imagem em uma matriz
image_matrix = np.array(image)

# Converte a matriz em vetor
image_vector = image_matrix.flatten()

# Realiza a compressão LZW
compressed_image_vector, LZW_dictionary = lzw(image_vector)

# Mostra a imagem
image.show()

# Define um nome para arquivo de resultado
nome, ext = os.path.splitext(file_name)
result_file_name = nome + "_comprimido" + ".txt"

with open(result_file_name, "w", encoding="utf-8") as file:
# Imprime a resolução da imagem
    largura, altura = image.size
    file.write("=====================================================================\n")
    file.write("Resolução da imagem:\n")
    file.write(f"{largura} x {altura}\n")
    file.write("=====================================================================\n\n")

    # Imprime a quantidade de pixels
    file.write("=====================================================================\n")
    file.write("Quantidade de pixels:\n")
    file.write(f"{image_matrix.size}\n")
    file.write("=====================================================================\n\n")

    # Imprime partes do vetor original
    file.write("=====================================================================\n")
    file.write("Vetor original de pixels: \n")
    file.write("Primeiros 50 pixels:\n")
    file.write(str(image_vector[:50]))
    file.write("\n\n")

    file.write("Últimos 50 pixels:\n")
    file.write(str(image_vector[-50:]))
    file.write("\n")
    file.write("=====================================================================\n\n")

    # Imprime o dicionário gerado
    itens = list(LZW_dictionary.items())
    file.write("=====================================================================\n")
    file.write("Dicionário gerado: \n")
    file.write("Primeiras 300 entradas:\n")
    for chave, valor in itens[:300]:
        file.write(f"{chave} -> {valor}\n")

    file.write("\nÚltimas 100 entradas:\n")

    for chave, valor in itens[-100:]:
        file.write(f"{chave} -> {valor}\n")
    file.write("=====================================================================\n\n")

    # Imprime o vetor comprimido da imagem
    file.write("=====================================================================\n")
    file.write("Sequência codificada: \n")
    file.write("Primeiros 50 códigos:\n")
    file.write(str(compressed_image_vector[:50]))
    file.write("\n\n")

    file.write("Últimos 50 códigos:\n")
    file.write(str(compressed_image_vector[-50:]))
    file.write("\n")
    file.write("=====================================================================\n\n")

    # Imprime o tamanho da mensagem original
    file.write("=====================================================================\n")
    file.write("Tamanho da mensagem original: \n")
    file.write(f'{len(image_vector)}\n')
    file.write("=====================================================================\n\n")

    # Imprime o tamanho original em bits
    file.write("=====================================================================\n")
    file.write("Tamanho original em bits: \n")
    file.write(f'{len(image_vector) * 8}\n')
    file.write("=====================================================================\n\n")

    # Imprime o tamanho comprimido em bits
    tamanho_comprimido = 0

    for codigo in compressed_image_vector:
        tamanho_comprimido += codigo.bit_length()
    file.write("=====================================================================\n")
    file.write("Tamanho comprimido em bits: \n")
    file.write(f'{tamanho_comprimido}\n')
    file.write("=====================================================================\n\n")

    # Imprime a porcentagem da compressão
    tamanho_original = len(image_vector) * 8
    compressao = (1 - (tamanho_comprimido / tamanho_original)) * 100
    file.write("=====================================================================\n")
    file.write("Porcentagem de compressão: \n")
    file.write(f'{compressao:.2f}%\n')
    file.write("=====================================================================\n\n")

print(f'Resultados escritos no arquivo {result_file_name}')
