# RentAI API {#mainpage}

Internal code documentation for the **RentAI** rental management API.

## Overview

RentAI is a FastAPI service with Bearer JWT authentication and CRUD for:

- **Property** — rental listings (title, address, city, price, bedrooms, availability)
- **Tenant** — renters with optional assignment to a property

## Modules

| Package | Description |
|---------|-------------|
| `app.main` | Application entry point and health check |
| `app.auth` | Password hashing, JWT creation, current-user dependency |
| `app.config` | Environment-based settings |
| `app.database` | SQLAlchemy engine and session dependency |
| `app.models` | ORM models: User, Property, Tenant |
| `app.schemas` | Pydantic request/response schemas |
| `app.seed` | Demo data seeding |
| `app.routers.auth` | `/auth` endpoints |
| `app.routers.properties` | `/properties` CRUD and filters |
| `app.routers.tenants` | `/tenants` CRUD, assign/unassign |

## Generating this documentation

```bash
doxygen Doxyfile
```

Open `docs/doxygen/html/index.html` in a browser.
