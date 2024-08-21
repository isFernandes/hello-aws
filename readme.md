# Documentação:

## Integração AWS com API Gateway, Lambda e SQS

### Visão Geral

Este projeto utiliza o AWS API Gateway, Lambda Functions e SQS para processar e consumir mensagens de forma eficiente.

## Processo

### Recepção e Redirecionamento:

Este projeto integra o AWS API Gateway, Lambda Functions e SQS para processar e consumir mensagens de forma eficiente. O fluxo básico é o seguinte:

API Gateway recebe uma requisição HTTP e a direciona para uma Lambda Function, esta por sua vez, valida o JSON recebido no corpo da requisição e envia a mensagem para uma fila SQS FIFO (First In, First Out).
Após o envio da mensagem, está lambda já retorna para o usuario o sucesso da entrada da operação.

### Consumo da Mensagem:

O recebimento da mensagem na fila, dispara (Trigger) o funcionamento da segunda Lambda Function, que consome a mensagem diretamente da fila SQS por meio de um evento, validamos o formato recebido e geramos logs para monitoramento no CloudWatch.
Houve alguns empecilhos até chegarmos neste resultado, devido a função ter sido criada para realizar o consumo da fila como um serviço, descartando as informações de evento, quando o evento foi levado em consideração e consegui reduzir o seu tempo de processamento para apenas 3 milissegundos, o consumo sem ser por evento, nunca apresentou sucesso, causando sempre timeout no processamento da lambda.

### Configuração de Permissões

Para garantir que a Lambda Function consumidora tenha apenas as permissões necessárias, configurei seu permissionamento por meio do IAM, para restringir o acesso exclusivamente à leitura da fila SQS.

### Monitoramento

Os logs gerados pela Lambda Function de consumo são monitorados via CloudWatch para facilitar a análise e depuração. Como apresentado desta etapa de monitoramento, a utilização do python necessita que seja inserido codigos para que os logs sejam apresentados devidamente na plataforma.

### Tempo de Configuração

Configuração Inicial: Aproximadamente 1h30 para configurar o ambiente, criar filas e configurar a API Gateway e Lambda Function.
Solução de Problemas: Aproximadamente 5h para integrar o ecossistema, especialmente resolvendo problemas com o consumo de mensagens da fila SQS.

Fora a escrita desta documentação, todo o processo durou aproximadamente 7 horas, o que se reflete para mim como um grande aprendizado.

## Tecnologias utilizadas:
#### Api gategway:
![image](https://github.com/user-attachments/assets/b1f955aa-85a5-4f10-9977-db9130a93fc5)
- Realizei seu deploy e pude realizar as chamadas por meio da rota disponivel.
- Rota POST para o recebimento da mensagem que pode ser qualquer uma dentro de um objeto 'body'

#### Lambda Functions (Python 3.12):
![image](https://github.com/user-attachments/assets/069b66ea-6841-4ad5-86d7-13d145296189)
- Funções lambdas criadas, a primeira da lista é responsavel pelo consumo e a segunda da lista é responsavel pela publicação
- Codigo disponivel nos arquivos pythons do repositorio

#### IAM:
![image](https://github.com/user-attachments/assets/d9a59694-d212-4ed4-8d86-c9b44e2f8e88)
- Permissão criada, como o nome informa, foi a segunda tentativa de criação para que a lambda pudesse ler as mensagens da fila

#### SQS:
![image](https://github.com/user-attachments/assets/04258390-38d0-4f0c-a5ad-b6c561f23cbd)
- Fila criada para trafego das mensagens entre ambas funções
- Criada como FIFO, para forçar a leitura sequencial e permitir rastreio facilitado de todas as mensagens submetidas

#### CloudWatch:
![image](https://github.com/user-attachments/assets/8a59cd9a-5fb3-4bf1-bbfa-d07d00e051fc)
![image](https://github.com/user-attachments/assets/d31ddc85-13b4-4799-af9b-6899a33a257c)
- Apesar de diferentes das cargas do GCP, o cloudWatch me pareceu mais intuitivo a primeiro momento, pelo menos para o entendimento de logs
- Python não consegue logar utilizando simplesmente o print, foi necessário configurar o permissionamento com a biblioteca logging 
