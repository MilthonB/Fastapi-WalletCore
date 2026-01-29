# 🚀 Fastapi-WalletCore

![Estado del Proyecto](https://img.shields.io/badge/STATUS-BETA-yellow?style=for-the-badge&logo=fastapi&logoColor=white)
![Python Version](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)


# Nombre de tu Proyecto
**Fastapi-WalletCore** es un **core financiero (wallet/ledger)** diseñado para manejar balances, transacciones y movimientos de dinero de forma **segura, consistente y extensible**.

El proyecto está enfocado en **arquitectura limpia**, reglas de negocio sólidas y buenas prácticas de backend, más que en la interfaz o en un CRUD básico.

---

## 🎯 Objetivo del proyecto

El objetivo de **Fastapi-WalletCore** es construir un core financiero desacoplado, testeable y extensible que pueda ser reutilizado en distintos sistemas.

El enfoque principal es:

- Dominio rico en reglas de negocio
- Arquitectura limpia
- Seguridad financiera
- Escalabilidad a largo plazo


## 🧠 ¿Qué problema resuelve?

En muchos sistemas (pagos, marketplaces, delivery, suscripciones, etc.) el manejo de dinero suele hacerse de forma improvisada:

- Sumas y restas directas
- Sin historial confiable
- Sin reglas claras
- Sin protección contra errores

**Fastapi-WalletCore** propone un enfoque correcto:
- Ledger inmutable
- Reglas de negocio claras
- Separación total entre dominio e infraestructura
- Base sólida para sistemas financieros reales

---

## 🏗️ Arquitectura

El proyecto sigue **Clean Architecture**, manteniendo el dominio completamente independiente de frameworks, bases de datos o infraestructura externa.

```text
app/
├── api/              # Datos, dummy, DB, ORM, Supabase
├── core/             # Configuración, settings, seguridad
├── domain/           # Dominio puro (entidades y reglas)
├── application/      # Casos de uso
├── infrastructure/   # DB, ORM, repositorios (futuro)
├── shared/           # Utilidades compartidas
├── presentation/     # Controller / Routers (FastAPI)
└── main.py           # Configuracion de FastAPI app
```

---

## 🧠 Principios aplicados

- **SOLID**
- **Separation of Concerns**
- **Dependency Inversion**
- **Domain-Driven Design (enfoque práctico)**

---

## 💰 Conceptos principales del dominio

### Money (Value Object)
Representa una cantidad monetaria de forma segura e inmutable.

### Currency (Value Object)
Representa un tipo de moneda de forma segura e inmutable.

### Wallet
Entidad que mantiene un balance y un historial de movimientos.

### Transaction
Movimiento de tipo **crédito** o **débito**, con estados controlados.

### Ledger
Registro **inmutable** de todas las operaciones realizadas.

---

## 🧩 Patrones de diseño utilizados

- **Repository Pattern**
- **Unit of Work**
- **Factory**
- **Service Layer**
- **Dependency Injection (FastAPI)**

---



## 📦 Gestión de dependencias con Poetry

Este proyecto utiliza **Poetry** para la gestión de dependencias y entornos virtuales, de forma similar a cómo **npm** o **pnpm** funcionan en el ecosistema Node.js.

---

### 📥 Instalación de Poetry

#### Linux / macOS

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Agregar Poetry al PATH (si no se agregó automáticamente):
```
export PATH="$HOME/.local/bin:$PATH"

```
Verificar instalación
```
poetry --version
```

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/MilthonB/Fastapi-WalletCore.git
cd Fastapi-WalletCore

```

## 📦 Después de clonar el repositorio:
```
poetry install
```

### 📂 Entorno virtual y versionado

El entorno virtual (`.venv`) **NO se sube al repositorio**.

Poetry gestiona automáticamente el entorno por proyecto.

Archivos versionados:

- ✅ `pyproject.toml`
- ✅ `poetry.lock`

Archivos ignorados:

- ❌ `.venv/`
- ❌ `__pycache__/`

Esto permite que cualquier persona clone el proyecto y reproduzca el entorno exacto.



## 🧪 Testing

El proyecto incluye pruebas desde el inicio utilizando **pytest**, priorizando:

- Tests de dominio
- Reglas de negocio
- Casos de uso críticos

### Ejecutar tests

```bash
poetry run pytest
```
O tambien 
```bash
poetry run pytest --cov=app
```


### ▶️ Ejecutar comandos en desarrollo

Ejecutar el servidor:

```bash
poetry run fastapi dev app/main.py

```



## 🛠️ Stack tecnológico

```md
## 🛠️ Stack tecnológico

### Backend
- Python 3.11+
- FastAPI (`fastapi[standard]`)
- Pydantic v2
- Uvicorn

### Gestión de dependencias
- Poetry

### Testing
- Pytest
- Pytest-cov

### Calidad de código
- Black
- Isort
- Mypy
- Pre-commit

### Infraestructura (planeado)
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker / Docker Compose
```

---

## 🐘 Base de datos (estado actual)

```md
## 🐘 Base de datos (estado actual)

Actualmente el proyecto **NO depende de una base de datos**.

El dominio se desarrolla de forma pura y aislada, priorizando reglas de negocio.

En etapas posteriores se integrará:

- PostgreSQL
- SQLAlchemy
- Migraciones automáticas con Alembic
```
## 🚀 Deployment

El proyecto se encuentra desplegado en Railway para fines de demostración y pruebas técnicas.

🔗 https://fastapi-walletcore-production.up.railway.app

> ⚠️ Nota: Actualmente utiliza datasources en memoria.  
> El objetivo del despliegue es demostrar arquitectura, manejo de errores y testing.


## 🗺️ Roadmap

- [x] Setup inicial con FastAPI + Poetry
- [x] Arquitectura limpia
- [X] Dominio financiero (Wallet, Money, Transaction)
- [X] Casos de uso
- [ ] Persistencia con PostgreSQL
- [ ] Migraciones automáticas
- [ ] Dockerización
- [ ] CI/CD básico




## 🌐 Endpoints planeados

### 🏦 Wallet

#### Crear una wallet
`POST /api/v1/wallets/`

Crea una nueva wallet con balance inicial en cero.

#### Request Body - Ejemplo

```
{
  "currency": "MXN",
  "balance": 5000,
  "is_active": true
}
```

Reglas:
 - No permite balances negativos
 - Tipo de moneda restriguidas a las siguientes
 #### Tipos de monedas permitidas
```
"USD"
"EUR"
"GBP"
"MXN"
"AUD"
"CAD"
"CHF"
"CNY"
"SEK"
"NZD"
```

---

#### Obtener información de una wallet
`GET /api/v1/wallets/{wallet_id}`

Devuelve:
- balance actual
- moneda
- estado de la wallet

---

#### Obtener los wallets
`GET /api/v1/wallets/all?limit=10&offset=1`

Devuelve:
- Todos los wallets, activos o inactivos

---

#### Eliminacion de wallet
`DELETE /api/v1/wallets/{wallet_id}`

Elimina una **wallet**.

---

#### Débito (retirar dinero)
`PATCH /api/v1/wallets/{wallet_id}/currency?currency=MXN`

Modifica el tipo de **moneda** en la wallet.



### 🩺 Sistema

#### Health check
`GET /health`

Verifica que el servicio esté activo.

---

### 🔐 (Futuro) Seguridad

- Autenticación por token
- Roles de acceso
- Protección de endpoints críticos




## 🧠 Decisiones de diseño

- El balance NO se guarda directamente
- El ledger es la fuente de verdad
- Las operaciones son inmutables
- Todas las reglas viven en el dominio
- La API solo orquesta casos de uso



## 🧪 Filosofía de testing

El testing se enfoca principalmente en:

- Dominio financiero
- Casos de uso
- Reglas de negocio críticas

La infraestructura se testea solo cuando es necesario.


## ERD
# Estructura del Sistema de Billetera

Este diagrama representa la arquitectura de base de datos para el flujo de transacciones.

## Diagrama de Entidad-Relación

```text
+-----------------------+
|     WalletEntity      |
+-----------------------+
| id (PK)               |
| currency              |
| balance               |
| is_active             |
| created_at            |
| updated_at            |
+-----------------------+
            |
            | (1)
            |
          tiene
            |
            | (*)
+-----------------------+
|   TransactionEntity   |
+-----------------------+
| id (PK)               |
| wallet_id (FK)        |
| amount                |
| transaction_type      |
| status                |
| created_at            |
| updated_at            |
+-----------------------+
            |
            | (1)
            |
          genera
            |
            | (1)
+-----------------------+
|     LedgerEntity      |
+-----------------------+
| id (PK)               |
| wallet_id (FK)        |
| transaction_id (FK)   |
| amount                |
| direction             |
| created_at            |
| updated_at            |
+-----------------------+
```

## 👨‍💻 Autor

**Milthon**  
Backend / Full-Stack Developer

Este proyecto forma parte de un portafolio enfocado en:

- Backend profesional
- Arquitectura
- Sistemas reales
