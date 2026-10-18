# 📈 Chart-GPT

Faça **perguntas em linguagem natural sobre um arquivo CSV** e receba a resposta em tabela. A aplicação (Streamlit) envia o cabeçalho do CSV e a sua pergunta ao modelo da OpenAI, que devolve uma consulta SQL; o SQL é executado localmente com **DuckDB** sobre o próprio arquivo.

## Como funciona

1. Informe sua chave da OpenAI (digitada na interface, não é armazenada)
2. Envie um CSV — há um exemplo em [`Samples/TabelaHUT.csv`](Samples/TabelaHUT.csv)
3. Pergunte algo sobre os dados
4. O app mostra a query gerada e o resultado em um DataFrame

## Tecnologias

Python 3.10 · Streamlit · OpenAI API · DuckDB · pandas · matplotlib

## Como rodar

```bash
pipenv install
pipenv run streamlit run main.py
```

> ⚠️ O código usa a Completions API com o modelo `text-davinci-003`, hoje descontinuado. Para voltar a funcionar, troque pelo modelo/endpoint de chat atual da OpenAI.

## Autor

Feito por [Amós Magalhães](https://github.com/amslimaa).
