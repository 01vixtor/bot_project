# Painel de Controle do Bot Telegram

Este projeto contém:
- Painel com Flask (login + configs)
- Bot do Telegram lendo essas configs
- Sistema de mensagens automáticas personalizadas

## Como usar

1. Clone o projeto
2. Crie virtualenv
3. Instale dependências
4. Crie banco e usuário admin
5. Rode `app.py` e `bot.py`

## Banco inicial
```bash
flask shell
>>> from models import db, User
>>> db.create_all()
>>> db.session.add(User(username="admin", password="1234"))
>>> db.session.commit()
