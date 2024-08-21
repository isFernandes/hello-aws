import json
import boto3 as bto
import logging

logger = logging.getLogger()
logger.setLevel("INFO")

sqs = bto.client("sqs")


REGION = "sqs.sa-east-1"
ACCOUNT_ID = ""
QUEUE_NAME = "hello-sqs.fifo"


def lambda_handler(evt, ctx):
    logger.info("Iniciando processamento")
    message_to_sent = json.dumps({"message": evt["body"]["message"]})

    query_url = f"""https://sqs.{REGION}.amazonaws.com/{ACCOUNT_ID}/{QUEUE_NAME}"""
    # Enviando a mensagem para a fila
    # Filas FIFO como está precisam do parametro MessageGroupId
    logger.info("Enviando para a fila")

    logger.info(message_to_sent)
    sqsReturn = sqs.send_message(
        QueueUrl=query_url,
        MessageBody=message_to_sent,
        MessageGroupId="default",
    )

    logger.info("Envio para fila realizado com sucesso!")

    return {
        "statusCode": 200,
        "body": {
            "message": "Mensagem enviada para a fila com sucesso!",
            "sqsMessageId": sqsReturn["MessageId"],
        },
    }
