# 🗜️ Algoritmo de Compressão LZW

> Implementação do algoritmo de compressão de dados sem perdas Lempel-Ziv-Welch (LZW), desenvolvido como trabalho do primeiro semestre da disciplina de Processamento de Imagens Digitais.

![Badge Language](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)
![Badge Algorithms](https://img.shields.io/badge/Topic-Data%20Compression-orange)
![Badge Academic](https://img.shields.io/badge/Type-Academic%20Project-blue)

## 🏫 Sobre o Projeto

Este projeto aborda a implementação prática do **Algoritmo LZW (Lempel-Ziv-Welch)**, um método universal de compressão de dados sem perdas baseado na construção de dicionários.

Desenvolvido como trabalho do primeiro semestre da disciplina de **Processamento de Imagens Digitais**, o objetivo é demonstrar como a codificação e decodificação de padrões repetitivos de texto funcionam em baixo nível.

### Como o LZW Funciona?

O algoritmo constrói um dicionário dinâmico durante a leitura dos dados:

* **Compressão:** Sequências de caracteres do arquivo original são mapeadas e substituídas por códigos numéricos mais curtos.

## 📂 Estrutura do Projeto

```bash
Algoritmo-de-compressao-LZW/
├── src/                                         # Código fonte do compressor (Python)
├── PROCESSAMENTO DE IMAGENS DIGITAIS.pdf        # Especificações do trabalho
└── README.md                                    # Esta documentação
```

## 🚀 Como Executar

*(Nota: adapte os nomes dos scripts abaixo de acordo com os arquivos presentes na pasta `src/`.)*

### Passo a passo

1.  **Clone o repositório:**
```bash
    git clone https://github.com/yVinicin/Algoritmo-de-compressao-LZW.git
    cd Algoritmo-de-compressao-LZW
```

2.  **Para Comprimir um Arquivo:**
    Forneça o arquivo original como entrada para gerar o arquivo comprimido.
```bash
    # Terminal Windows
    python src/LZW_image.py <nome_do_arquivo_de_imagem>
```
```bash
    # Terminal Linux
    python3 src/LZW_image.py <nome_do_arquivo_de_imagem>
```

## 📈 Eficiência e Complexidade

O LZW é altamente eficiente para arquivos com muita repetição (como textos longos ou arquivos de log). A complexidade de tempo geralmente se aproxima de $O(N)$ em relação ao tamanho da entrada, contanto que a estrutura de dados utilizada para o dicionário (como Hash Maps ou Tries) seja bem otimizada.
