# Tradutor com OpenAI - Aplicação Web

Este é um projeto que utiliza a API da OpenAI para criar um tradutor web. A aplicação permite que os usuários insiram um texto e selecionem um idioma de destino para realizar a tradução. O modelo "text-davinci-003" da OpenAI é utilizado para executar as traduções.

## Configuração

Antes de executar o projeto, siga as etapas de configuração abaixo:

1. Crie um arquivo `.env` na raiz do projeto.
2. Adicione as seguintes linhas ao arquivo `.env`:

    OPENAI_API_KEY=`SUA_CHAVE_DA_API`

    Substitua `SUA_CHAVE_DA_API` pela sua chave de API da OpenAI.

3. Instale as dependências necessárias executando o seguinte comando:

```shell
pip install Flask openai python-dotenv
```
## Uso
Para executar a aplicação, siga as etapas abaixo:

1. Execute o seguinte comando no terminal:
```shell
python app.py
```
2. Acesse a aplicação web no navegador utilizando o seguinte URL:
```shell
http://localhost:5000
```
3. No formulário, insira o texto que deseja traduzir e selecione o idioma de destino.
4. Clique no botão "Traduzir" para obter a tradução. O resultado será exibido abaixo do formulário.

## Observações
Certifique-se de ter uma conta na OpenAI e de que sua chave de API esteja ativa.

Verifique sua cota de uso na OpenAI para garantir que você não exceda os limites permitidos.

Personalize o projeto de acordo com suas necessidades, como estilos CSS adicionais, melhorias na interface, tratamento de erros, etc.
