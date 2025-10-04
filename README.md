# FCCPD 

Trabalho da disciplina **Fundamentos de Computação Concorrente, Paralela e Distribuída (FCCPD)**, implementando um sistema **cliente-servidor** simples para estudar comunicação entre processos e concorrência.

## 👥 Integrantes
- Clara Machado — <cma3@cesar.school>
- Gabriel Landim — <gqsl@cesar.school>
- Larissa Sobrinho — <lss2@cesar.school>
- Pedro Sampaio — <pssa@cesar.school>

> Professor(a): Jorge Farias  
> Período: 2025.2

---

##  Descrição rápida
Este projeto implementa um **servidor** que aguarda conexões e um **cliente** que se conecta e troca mensagens/solicitações.  
O foco é demonstrar **concorrência** (múltiplos clientes atendidos pelo servidor) e **comunicação via rede**.

---

##  Como Rodar
Para Rodar basta so rodar primeiro o arquivo python do Servidor e logo depois o do Cliente em terminais separados

---

##  Contexto
Nossa conexão simula uma lanchonete que tem clientes, uma fila de pedidos e os cozinheiros Nela temos:
- Cliente que atua como o cliente da lanchonete
- Servidor que atua como a fila de pedidos
- Threads locais no servidor atuam como cozinheiros
  
