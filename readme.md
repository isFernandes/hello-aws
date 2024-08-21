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

- AWS API Gateway
- AWS Lambda
- AWS SQS
- Python 3.8
- IAM
- CloudWatch
