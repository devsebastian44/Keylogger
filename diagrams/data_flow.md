# Diagramas de Flujo del Proyecto

## Pipeline CI/CD (GitHub Actions)

```mermaid
graph LR
    A[Push al Repo] --> B[Stage: Lint]
    B --> C[Stage: Security Scan (Bandit)]
    C --> D[Stage: Test]
    D --> E{Exitoso?}
    E -- Sí --> F[Feedback Visual]
    E -- No --> G[Notificación de Fallo]
```

## Ciclo de Vida del Evento (Modo Activo)

```mermaid
sequenceDiagram
    participant User as Usuario
    participant OS as Sistema Operativo
    participant Hook as Listener (pynput)
    participant Engine as Engine Core
    participant Log as Log File / Remote

    User->>OS: Presiona Tecla
    OS->>Hook: Evento de Teclado
    Hook->>Engine: Captura Key
    Engine->>Log: Escribe en Log
    Note over Engine,Log: Formateo y Offsetting
```
