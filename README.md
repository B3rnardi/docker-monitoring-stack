**Monitoramento de Câmbio**
Stack de orquestração e monitoramento em tempo real utilizando Python, Redis, Prometheus e Grafana.


Subindo a Infraestrutura

Certifique-se de ter o Docker instalado na sua máquina e execute o comando abaixo na raiz do projeto:

docker compose up -d
(Dica: Se você alterar o código Python no main.py, utilize docker compose up -d --build para forçar a atualização da imagem).


Portas de Acesso
- Aplicação Python (API/Métricas): http://localhost:8000

- Prometheus (Coleta): http://localhost:9090

- Grafana (Dashboards): http://localhost:3000