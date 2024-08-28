# E-commerce Reservation System

Este projeto é um sistema de reservas para uma plataforma de e-commerce onde os clientes podem reservar produtos que estão temporariamente indisponíveis ou em alta demanda.

## Requisitos

- Python 3.12+
- Virtualenv (recomendado)

## Configuração do Projeto

### 1. Clone o Repositório.

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Criando ambiente virtual.

```bash
python3 -m venv venv
source venv/bin/activate # no Windows: venv\Scripts\activate
```

### 3. Instalando as dependências.
```bash
pip install -r requirements.txt
```

### 4. migrações.
```bash
python manage.py migrate
```

### 5. Criando o seu usuario no Admin.
```bash
python manage.py createsuperuser --username "seu_usuario" --email "seu_email"
```

### 6. Script para popular o banco com produtos e clientes.
```bash
python base_init.py
```

### 7. Startando o projeto.
```bash
python manage.py runserver
```

## Testando Projeto

### 1. Listar todos os produtos
```bash
curl -X GET "http://localhost:8000/api/products/"
```

### 2. Reservar produto com cliente
```bash
curl -X POST "http://localhost:8000/api/products/9/reserve/" \
-H "Content-Type: application/json" \
-d '{"customer_id": 1}'
```

### 3. Reservar produto sem cliente
```bash
curl -X POST "http://localhost:8000/api/products/6/reserve/" \
-H "Content-Type: application/json"
```

### 7. Listar reservas do cliente
```bash
curl -X GET "http://localhost:8000/api/customer/1/reservations/"
```