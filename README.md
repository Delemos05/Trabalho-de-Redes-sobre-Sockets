# Projeto de Comunicação em Rede: TCP e UDP

Este projeto de portfólio tem como objetivo demonstrar a comunicação entre cliente e servidor utilizando os protocolos **TCP (Transmission Control Protocol)** e **UDP (User Datagram Protocol)** com a linguagem Python. É voltado para fins educacionais, com foco na compreensão prática do funcionamento da camada de transporte do modelo OSI e a manipulação de sockets com IPv4.

---

# 💻 Comunicação em Rede com TCP e UDP em Python

Este projeto demonstra o uso dos protocolos **TCP** e **UDP** em aplicações de rede utilizando **Python** e a biblioteca `socket`. Foi desenvolvido com fins educacionais para ilustrar a troca de mensagens entre cliente e servidor, uso correto de **IPv4**, **portas de rede**, e **tratamento de erros** comuns.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Biblioteca `socket` (nativa)
- Ambiente local (rede doméstica ou localhost)

---

## 🧠 Conceitos Abordados

- Diferenças entre TCP e UDP
- Criação e gerenciamento de sockets
- Medição de tempo de resposta (latência)
- Tratamento de exceções (timeout, conexão recusada)
- Uso correto de IPs e portas

---

## 📁 Estrutura do Projeto

📂 /
├── cliente_tcp.py
├── servidor_tcp.py
├── cliente_udp.py
├── servidor_udp.py
└── README.md


---

## 🌐 Orientações sobre IPv4 e Portas

✅ **IP (IPv4)**
- Use IPs válidos dentro da sua rede local, como `192.168.x.x`, ou `127.0.0.1` para testes no mesmo computador.
- Verifique o IP do servidor com `ipconfig` (Windows) ou `ifconfig` / `ip a` (Linux/Mac).

✅ **Portas**
- Use portas **acima de 1024**, preferencialmente entre `1025` e `65535`.
- Certifique-se de que a porta está **livre e acessível**.
- Exemplos válidos: `12000`, `15000`, `50001`.

