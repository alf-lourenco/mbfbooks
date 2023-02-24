import requests
import json

menssagem = {"text": "valor: Teste integracao hoje"}

weebhook = "https://hooks.slack.com/services/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"

requests.post(weebhook, data=json.dumps(menssagem))