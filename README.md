# 🐍 TCP Chat Simulator🔌

Este é um projeto prático onde apresenta um protótipo funcional de chat peer-to-peer (P2P) em `Python`, utilizando **sockets TCP e threads**, com **registro de logs** e interface de console amigável.

Foi desenvolvido com o apoio do professor Ms. Alex Cabral de Brito, durante às aulas da disciplina de Protocolos e Interconexão de Redes de Computadores.

## 🎯 Objetivos

O principal objetivo deste projeto é demonstrar os conceitos de programação de redes, **comunicação entre peers e multithreading**, servindo como base para projetos maiores e mais complexos.

## ⚙️ Funcionalidades

 - Envio e recebimento de mensagens em tempo real.
 - Conexão entre múltiplos peers.
 - Registros de logs e do principais eventos (conexão de usuário, saída de usuário ...)
 - Validação de portas e entrada de usuários simultâneos.
 - Threads para comunicação simultânea.

## 🛠️ Tecnologias Utilizadas

- `Python` (linguagem principal do projeto).
- `Socket` (via biblioteca `Socket`).
- `Threads` (para envio e recebimento de mensagens simultâneos).
- `Datetime` (módulo utilizado para **registro das horas no arquivo de log**).
- `OS` (módulo para obter **informações do diretório e arquivo de log**).
- `Time` (módulo utilizado para **realizar pausas no programa, para o usuário**).
- `Armazenamento de Logs` (onde é realizado **o registro dos principais eventos do programa**).

## 📂 Estrutura do projeto

```
TCP_CHAT_SIMULATOR/
│── src/                # Código-fonte
│   └── main.py         # Script principal do chat
│── .gitignore          # Arquivos a serem ignorados pelo Git
└── README.md           # Documentação do projeto
```

## ▶️ Como executar
 
 1️⃣ Clone o repositório (ou **baixe o projeto**):

```
git clone https://github.com/robertifpb/tcp_chat_simulator.git
```

```
cd tcp_chat_simulator
```
 2️⃣ Execute o script principal:
``` 
 python main.py
```
 3️⃣ Informe os dados de conexão para o usuário:

 - `Nome de usuário`.
 - Porta disponível para a conexão (`5000, 5001, 5002, 5003 ou 5004`)
 
 4️⃣ Utilize o chat para enviar às mensagens:

 - Digite mensagens e aperter `Enter` para realizar o envio.
 - Para sair basta digitar no chat `sair`.

 5️⃣ Verifique os logs:

 - Todas as conexões e mensagens são registradas em `logs_chat.txt` no arquivo local do seu computador.

## ⚠️ Observações importantes

 - Necessário ter Python 3.x instalado no seu pc.
 - Sistema operacional compatível (`Windows, Linux ou macOS`).
 - O chat roda localmente em `localhost`.
 - Cada usuário deve escolher uma porta diferente da lista disponível.
 - O sistema conecta automaticamente a todos os peers ativos.
