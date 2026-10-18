# RentAI API

Пример REST API на FastAPI с Bearer JWT: объекты недвижимости (`Property`) и арендаторы (`Tenant`).

## Быстрый старт

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

Документация: http://127.0.0.1:8000/docs

## Демо-пользователь

| Поле | Значение |
|------|----------|
| Email | `admin@rentai.local` |
| Password | `admin123` |

Логин (`username` = email):

```bash
curl -X POST http://127.0.0.1:8000/auth/login -d "username=admin@rentai.local&password=admin123"
```

Дальше передавайте заголовок:

```http
Authorization: Bearer <access_token>
```

## Эндпоинты

### Auth
- `POST /auth/register` — регистрация
- `POST /auth/login` — получить JWT
- `GET /auth/me` — текущий пользователь

### Properties
- `GET /properties` — список (фильтры: `city`, `minPrice`, `maxPrice`, `available`)
- `GET /properties/{id}`
- `POST /properties`
- `PUT /properties/{id}`
- `DELETE /properties/{id}`

### Tenants
- `GET /tenants`
- `GET /tenants/{id}`
- `POST /tenants`
- `PUT /tenants/{id}`
- `DELETE /tenants/{id}`
- `POST /tenants/{id}/assign` — назначить объект (`{"propertyId": 1}`)
- `POST /tenants/{id}/unassign` — снять назначение

## Примеры тел запросов

Property:

```json
{
  "title": "Cozy Flat",
  "address": "10 Oak Street",
  "city": "Berlin",
  "pricePerMonth": 1200,
  "bedrooms": 2,
  "available": true
}
```

Tenant:

```json
{
  "firstName": "Ivan",
  "lastName": "Petrov",
  "email": "ivan.petrov@example.com",
  "phone": "+49123456789",
  "propertyId": null
}
```
