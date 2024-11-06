# algebra-linear
Projeto de Álgebra Linear e Cálculo Numérico.

## Funções

Este projeto é feito com a linguagem de programação Python e faz o uso da biblioteca NumPy. Atualmente, estão 
disponíveis as seguintes funções:

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

**2.2. Criação e ativação do ambiente virtual**

- Linux/macOS:
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`

- Windows (CMD)
  - `python -m venv .venv`
  - `.venv\Scripts\activate`

- Windows (PowerShell)
  - `python -m venv .venv`
  - `.\.venv\Scripts\Activate.ps1`

**2.3. Instalação do NumPy.**
```sh
pip install numpy
```

### 3. Teste

Agora que o seu ambiente está configurado, teste a aplicação executando o seguinte comando:

```sh
python main.py
```

### 4. Dados

Este projeto disponibiliza dois arquivos de dados no formato JSON para a execução do programa:
- exemplos.json
- trabalho.json

Você pode criar o seu próprio arquivo de dados e inserí-lo na pasta `data`, o programa irá reconhecer o arquivo
automaticamente. No entanto, para que o arquivo seja processado pelo sistema de forma correta, ele deve seguir as
regras listadas abaixo:

- O arquivo deve estar no formato JSON
- Chaves
  - Cada chave deve corresponder ao nome do sistema (e.g. sistema1, matriz_identidade, etc)
  - O nome deve ser diferente dos métodos disponíveis (jacobi, seidel, invert)
- Valores
  - Cada valor deve corresponder à forma matricial do sistema
  - O número de colunas deve ser igual ao número de linhas mais um
  - O número de colunas deve ser o mesmo em cada uma das linhas

## Imagens

- #TODO

## Autor

- Andrei Legramante - [@AndreiLegram](https://github.com/AndreiLegram)
