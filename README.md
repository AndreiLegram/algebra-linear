# algebra-linear
Projeto de Álgebra Linear e Cálculo Numérico.

## Funções

Neste projeto foi utilizada a linguagem de programação Python e a biblioteca de álgebra linear NumPy. Atualmente,
estão disponíveis as seguintes funções:

- Resolução de sistemas de equações lineares pelo método iterativo de Jacobi;
- Resolução de sistemas de equações lineares pelo método iterativo de Gauss-Seidel;
- Inversão de matrizes.

## Testando

Para testar a aplicação, basta seguir os passos abaixo.

### 1. Requisitos

Primeiramente, em sua máquina devem estar instalados os seguintes aplicativos:

- Git
- Python

### 2. Instalação

Atendendo os requisitos, abra um terminal e execute as linhas de comando abaixo. Lembre de executar os comandos que 
estejam de acordo com o seu sistema operacional e com o interpretador de linha de comando (shell) escolhido.

**2.1. Clone do repositório e acesso ao diretório**
```sh
git clone https://github.com/AndreiLegram/algebra-linear.git
cd algebra-linear
```

**2.2. Criação e ativação do ambiente virtual (opcional)**

- Linux/macOS:
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`

- Windows (CMD)
  - `python -m venv .venv`
  - `.venv\Scripts\activate`

- Windows (PowerShell)
  - `python -m venv .venv`
  - `.\.venv\Scripts\Activate.ps1`

**2.3. Instalação da biblioteca NumPy**
```sh
pip install numpy
```

### 3. Teste

Agora que o seu ambiente está configurado, teste a aplicação executando o seguinte comando:

```sh
python main.py
```

**3.1. Primeiro argumento**

O primeiro argumento é obrigatório, nele você deve informar o nome de um dos arquivos de dados disponíveis,
sendo dois deles o padrão: *exemplos.json* e *trabalho.json*

Exemplos:
- `python main.py exemplos.json`
- `python main.py trabalho.json`
- `python main.py sistema1.json`

**3.2. Segundo argumento (opcional)**

O segundo argumento é opcional, nele você pode fazer um filtro no que será calculado, escolhendo uma das matrizes
do arquivo de dados (exemplo_1, exemplo_2, etc) ou uma das funções implementadas no projeto (jacobi, seidel, invert)

Exemplos:
- `python main.py exemplos.json exemplo_2`
- `python main.py exemplos.json jacobi`
- `python main.py trabalho.json questao_1`
- `python main.py trabalho.json questao_extra`
- `python main.py trabalho.json invert`

### 4. Dados

Este projeto disponibiliza dois arquivos de dados no formato JSON para a execução do programa:
- *exemplos.json*
- *trabalho.json*

Você pode criar o seu próprio arquivo de dados e inserí-lo na pasta `data`, o programa irá reconhecer o arquivo
automaticamente. No entanto, para que o arquivo seja processado pelo sistema de forma correta, ele deve seguir as
regras listadas abaixo:

- O arquivo deve estar no formato JSON
- Chaves
  - Cada chave deve corresponder ao nome do sistema (e.g. sistema1, matriz_identidade, etc)
  - O nome deve ser diferente das funções disponíveis (jacobi, seidel, invert)
- Valores
  - **A:** Matriz dos coeficientes;
  - **b (opcional):** Vetor dos termos constantes;
    - Padrão: vetor nulo
  - **x (opcional):** Vetor da solução ou chute inicial;
    - Padrão: vetor nulo
  - **N (opcional):** Número máximo de iterações;
    - Padrão: 100
  - **t (opcional):** Tolerância ou precisão.
    - Padrão: 0.001

## Trabalho

Este projeto foi desenvolvido como resolução do trabalho da disciplina de Álgebra Linear e Cálculo Numérico do IFRS - 
Campus Bento Gonçalves.

### Questão 1

![questao_1](https://github.com/AndreiLegram/algebra-linear/blob/master/public/questao_1.png?raw=true)
![questao_1_input](https://github.com/AndreiLegram/algebra-linear/blob/master/public/questao_1_input.png?raw=true)
![questao_1_output](https://github.com/AndreiLegram/algebra-linear/blob/master/public/questao_1_output.png?raw=true)

### Questão 2

![questao_2](https://github.com/AndreiLegram/algebra-linear/blob/master/public/questao_2.png?raw=true)
![questao_2_input](https://github.com/AndreiLegram/algebra-linear/blob/master/public/questao_2_input.png?raw=true)
![questao_2_output](https://github.com/AndreiLegram/algebra-linear/blob/master/public/questao_2_output.png?raw=true)

### Questão Extra

![questao_extra](https://github.com/AndreiLegram/algebra-linear/blob/master/public/questao_extra.png?raw=true)
![questao_extra_input](https://github.com/AndreiLegram/algebra-linear/blob/master/public/questao_extra_input.png?raw=true)
![questao_extra_output](https://github.com/AndreiLegram/algebra-linear/blob/master/public/questao_extra_output.png?raw=true)

As prints foram tiradas da CLI do Visual Studio Code após rodar o comando `python main.py trabalho.json`

## Referências

- **Repositório:** algebra-linear - [GitHub](https://github.com/AndreiLegram/algebra-linear)
- **Autor:** Andrei Legramante - [@AndreiLegram](https://github.com/AndreiLegram)
