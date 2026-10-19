import time
import requests
import redis
import os
from prometheus_client import start_http_server, Gauge

redis_host = os.getenv("REDIS_HOST", "localhost")
cache = redis.Redis(host=redis_host, port=6379, decode_responses=True)

cotacao_dolar = Gauge('usd_brl_cotacao', 'Cotação atual do Dólar em Reais')

start_http_server(8000)
print("Iniciando o Monitor de Câmbio...")

while True:
    try:
        resposta = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
        valor_atual = float(resposta.json()['USDBRL']['bid'])
        
        cache.set("dolar_atual", valor_atual)
        
        cotacao_dolar.set(valor_atual)
        
        print(f"Cotação salva: R$ {valor_atual}")
    except Exception as e:
        print(f"Erro: {e}")
        
    time.sleep(30)