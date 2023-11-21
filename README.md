
## Resumo

  


O Indexer é um programa que realiza a contagem de palavras em documentos de texto, possibilitando a busca por palavras específicas e a identificação de documentos relevantes para um termo de busca. Durante o processo, todas as letras são convertidas para minúsculas, e caracteres como números e pontuações são desconsiderados.

  

## Opções

  

-  `--freq N ARQUIVO`: Exibe o número de ocorrências das N palavras mais frequentes em ARQUIVO, em ordem decrescente de ocorrência.

-  `--freq-word PALAVRA ARQUIVO`: Exibe o número de ocorrências de PALAVRA em ARQUIVO.

-  `--search TERMO ARQUIVO [ARQUIVO ...]`: Exibe uma listagem dos ARQUIVOS mais relevantes para o TERMO, em ordem descrescente de relevância. TERMO pode conter mais de uma palavra, indicada entre àspas.

  

> **Importante:**

>> **Não é necessário passar junto ao nome do arquivo a sua extensão!**

>> **Os arquivos que serão analisados deverão ser salvos dentro da pasta `assets`.**

>>  ***O programa é somente compatível com arquivos .txt.***

  

## Como Usar

  

### Requisitos

  

- Python 3.10+

  
  

#### Windows:

  

1.  **Baixar o Instalador:**

- Acesse o site oficial do Python em [python.org](https://www.python.org/);

- Vá para a seção de downloads e clique em "Downloads for Windows";

- Escolha a versão mais recente do Python.

2.  **Executar o Instalador:**

- Execute o arquivo baixado;

- Certifique-se de marcar a opção "Add Python to PATH" durante a instalação.

3.  **Concluir a Instalação:**

- Siga as instruções do instalador;

- Para verificar se o Python foi instalado corretamente, abra o prompt de comando e digite:

`python --version`

 
 
#### Linux (Ubuntu/Debian):

  

1.  **Verificar a Existência do Python:**

- Muitas distribuições Linux já incluem o Python. Verifique se você já o possui digitando:

`python3 --version`

2.  **Atualizar os Pacotes do Sistema:**

- Se o Python não estiver instalado, atualize os pacotes do sistema:

`sudo apt update`

3.  **Instalar o Python:**

- Instale o Python usando o gerenciador de pacotes. Utilize o seguinte comando:

`sudo apt install python3`

4.  **Verificar a Instalação:**

- Após a instalação, verifique se o Python foi instalado corretamente:

`python3 --version`

  

>  **Essas instruções são baseadas em sistemas Windows e Ubuntu/Debian. Se estiver usando outra distribuição Linux, os comandos podem variar. Consulte a documentação da sua distribuição para informações mais específicas.**

  

### Execução

Acesse a pasta raiz (que possui o arquivo `indexer.py`) pelo terminal e utilize o comando:

  

- Windows: `py indexer.py` + args

- Linux: `python3 indexer.py` + args

>**Observações:**

  

>>- Certifique-se de ter as permissões necessárias para executar o arquivo. Se não tiver, você pode usar o comando `chmod` para conceder permissões de execução:

  

>>`sudo chmod +x indexer.py`

  

## Exemplos de Uso

  

### Contagem de palavras mais frequentes

  

- Windows: `py indexer.py --freq 10 nome_do_arquivo `

- Linux: `python3 indexer.py --freq 10 nome_do_arquivo `

  

### Contagem de frequência de uma palavra

  

- Windows: `py indexer.py --freq-word palavra nome_do_arquivo `

- Linux: `python3 indexer.py --freq-word palavra nome_do_arquivo `

  

### Busca arquivos mais relevantes para um termo

  

- Windows: `py indexer.py --search "termo1 termo2 termo3" nome_do_arquivo_1 nome_do_arquivo_2 `

- Linux: `python3 indexer.py --search "termo1 termo2 termo3" nome_do_arquivo_1 nome_do_arquivo_2`
