# Faxtec API

A **Faxtec API** é uma API pública que permite o envio e a consulta de mensagens de forma anônima. Ela foi desenvolvida para ser utilizada pela aplicação **Faxtec**.

## Endpoints

### `/messages`

A API oferece os seguintes métodos:

- **GET**: Retorna todas as mensagens armazenadas.  
- **POST**: Envia uma nova mensagem anônima.

#### Método GET

Retorna uma lista de todas as mensagens enviadas. Não requer parâmetros.

**Exemplo de requisição:**
```bash
curl https://faxtec-api.vercel.app/messages
```

#### Método POST

Envia uma nova mensagem. Requer um corpo de solicitação com os seguintes parâmetros:

- **addressee** (string): Nome do destinatário.
- **message** (string): O conteúdo da mensagem.

**Exemplo de requisição:**
```bash
curl -X POST https://faxtec-api.vercel.app/messages \
     -H "Content-Type: application/json" \
     -d '{"addressee": "Fulano", "message": "Olá, como vai?"}'
```

## Características

- **Sem autenticação necessária**: Não requer chave de API.
- **Métodos suportados**: Apenas GET e POST no endpoint `/messages`.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [`LICENSE`](LICENSE) para mais detalhes.
