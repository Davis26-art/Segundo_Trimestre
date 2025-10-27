# Diagrama de Casos de Uso – Sistema AgroSmart 

```mermaid
%%{init: {"theme":"default"}}%%
graph TD
    A[Agricultor] -->|Usa| B(Iniciar sesión)
    A -->|Usa| C(Registrar cultivo)
    A -->|Usa| D(Ver estado de sensores)
    A -->|Usa| E(Recibir alertas de humedad)
    A -->|Usa| F(Generar reporte de rendimiento)

    Admin[Administrador] -->|Gestiona| G(Gestionar usuarios)
    Sensor[Sensor IoT] -->|Envía| H(Enviar lectura)
    H -->|Actualiza datos| D

```

# Diagrama de Clases UML – Sistema AgroSmart

```mermaid
classDiagram
    class Usuario {
        +int id
        +String nombre
        +String correo
        -String contraseña
        +iniciar_sesion()
        +cerrar_sesion()
    }

    class Agricultor {
        +String finca
        +String telefono
        +registrar_cultivo()
        +consultar_reportes()
    }

    class Cultivo {
        +int id
        +String nombre
        +String tipo
        +Date fecha_siembra
        +calcular_promedio_humedad()
    }

    class Sensor {
        +int id
        +String tipo
        +float valor
        +String estado
        +enviar_dato()
        +verificar_estado()
    }

    class Reporte {
        +int id
        +Date fecha
        +float humedad_promedio
        +String recomendacion
        +generar_pdf()
    }

    Usuario <|-- Agricultor
    Agricultor "1" -- "*" Cultivo : posee
    Cultivo "1" -- "*" Sensor : tiene
    Cultivo "1" -- "*" Reporte : genera

```

# Diagrama de Componentes – Arquitectura del Sistema AgroSmart

```mermaid
graph TD
    subgraph Cliente
        WebApp["Aplicación Web (HTML, JS, CSS)"]
    end

    subgraph Servidor
        API["API Flask (Lógica de Negocio)"]
        DB["Base de Datos MySQL"]
    end

    subgraph IoT
        IoTModule["Módulo IoT (ESP32 + Sensor DHT11)"]
    end

    WebApp -->|Solicita datos| API
    API -->|Devuelve JSON| WebApp
    API -->|Consulta y actualiza| DB
    IoTModule -->|Envía lecturas| API


```

# Diagrama de Despliegue – Infraestructura del Sistema AgroSmart

```mermaid
flowchart TB
    subgraph Campo
        IoTDevice["Dispositivo IoT (ESP32 + Sensor)"]
    end

    subgraph Nube
        LB["Balanceador de Carga"]
        AppServer["Servidor Web (Flask + API REST)"]
        DBServer["Base de Datos MySQL (RDS)"]
        Storage["Almacenamiento de archivos (S3)"]
    end

    Browser["Navegador del Agricultor"]

    IoTDevice -->|HTTP/MQTT| LB
    LB --> AppServer
    AppServer --> DBServer
    AppServer --> Storage
    Browser -->|HTTPS| LB


```

# Modelo Entidad–Relación (ER) – Base de Datos AgroSmart

```mermaid
erDiagram
    USUARIOS {
        int id_usuario PK
        varchar nombre
        varchar correo
        varchar contraseña
    }
    AGRICULTORES {
        int id_agricultor PK
        varchar finca
        varchar telefono
        int id_usuario FK
    }
    CULTIVOS {
        int id_cultivo PK
        varchar nombre
        varchar tipo
        date fecha_siembra
        int id_agricultor FK
    }
    SENSORES {
        int id_sensor PK
        varchar tipo
        float valor
        varchar estado
        datetime fecha_lectura
        int id_cultivo FK
    }
    REPORTES {
        int id_reporte PK
        date fecha
        float humedad_promedio
        varchar recomendacion
        int id_cultivo FK
    }

    USUARIOS ||--o{ AGRICULTORES : tiene
    AGRICULTORES ||--o{ CULTIVOS : posee
    CULTIVOS ||--o{ SENSORES : contiene
    CULTIVOS ||--o{ REPORTES : genera

```