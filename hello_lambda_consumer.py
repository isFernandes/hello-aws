import json
import boto3 as bto
import time
import logging

logger = logging.getLogger()
logger.setLevel("INFO")

# REGION = "sqs.sa-east-1"
# ACCOUNT_ID = ""
# QUEUE_NAME = "hello-sqs.fifo"


def lambda_handler(event, context):
    # Codigo abaixo só é valido caso seja necessario consumir da fila
    # Criar um cliente SQS
    # sqs = bto.client("sqs")

    # query_url = f"""https://sqs.{REGION}.amazonaws.com/{ACCOUNT_ID}/{QUEUE_NAME}"""

    # logger.info("Iniciando consumo da fila")
    # logger.info(json.dumps(event))
    # #logger.info(json.dumps(context))
    # # Receber a mensagem da fila SQS

    # time.sleep(5)

    # response = sqs.receive_message(
    #     QueueUrl=query_url,
    #     MaxNumberOfMessages=1
    # )

    # logger.info("Fila consumida!")

    # logger.info(response)

    message = None
    # # Processar a mensagem
    # if "Messages" in response:
    #     logger.info(response["Messages"])
    #     message = json.loads(response["Messages"][0]["Body"])
    #     logger.info(f"""Mensagem recebida: {message['message']}""")

    # if message is None:
    #     logger.info("Message não foi preenchido!")
    #     message = "Nenhuma mensagem postada na fila"

    if "Records" in event:
        logger.info(event["Records"])
        message = json.loads(event["Records"][0]["body"])
        logger.info(f"""Mensagem recebida: {message}""")

    return {
        "statusCode": 200,
        "body": json.dumps(
            {"message": "Mensagem processada com sucesso!", "content": message}
        ),
    }
