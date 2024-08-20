import json
import boto3 as bto

sqs = bto.client("sqs")


def lambda_handler(evt, ctx):
    # Pegando conteudo da requisição
    message = evt["body"]

    # Enviando a mensagem para a fila
    sqsReturn = sqs.send_message(
        QueueUrl="https://sqs.{region}.amazonaws.com/{account_id}/{queue_name}",
        MessageBody=message,
    )

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Hello World sent to SQS!",
                "sqsMessageId": sqsReturn["MessageId"],
            }
        ),
    }
