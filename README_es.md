<div align="center">

![Agent Zero](/docs/res/header.png)

# `Agent Zero`

[![Gracias a los Patrocinadores](https://img.shields.io/badge/GitHub%20Sponsors-Gracias%20a%20los%20Patrocinadores-FF69B4?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/frdel) [![Únete a nuestra Comunidad Skool](https://img.shields.io/badge/Skool-Únete%20a%20nuestra%20Comunidad-4A90E2?style=for-the-badge&logo=skool&logoColor=white)](https://www.skool.com/agent-zero) [![Únete a nuestro Discord](https://img.shields.io/badge/Discord-Únete%20a%20nuestro%20servidor-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/B8KZKNsPpj) [![Suscríbete en YouTube](https://img.shields.io/badge/YouTube-Suscríbete-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@AgentZeroFW) [![Conéctate en LinkedIn](https://img.shields.io/badge/LinkedIn-Conéctate-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jan-tomasek/) [![Síguenos en Warpcast](https://img.shields.io/badge/Warpcast-Síguenos-5A32F3?style=for-the-badge)](https://warpcast.com/agent-zero)

> **Nota:** Agent Zero no usa Twitter/X. Cualquier cuenta de Twitter/X que afirme representar este proyecto es falsa.

[Instalación](./docs/installation.md) •
[Cómo actualizar](./docs/installation.md#how-to-update-agent-zero) •
[Documentación](./docs/README.md) •
[Uso](./docs/usage.md)

</div>


[![Demostración](/docs/res/showcase-thumb.png)](https://youtu.be/lazLNcEYsiQ)



Visita [www.agent-zero.ai](https://agent-zero.ai) para más información

[![Agente de Navegador](/docs/res/web_screenshot.jpg)](https://agent-zero.ai)



> [!NOTE]
> **🎉 Lanzamiento v0.8.1**: ¡Ahora con un agente de navegador capaz de usar Chromium para interacciones web! Esto permite a Agent Zero navegar por la web, recopilar información e interactuar con contenido web de forma autónoma.


https://github.com/user-attachments/assets/c168759d-57d8-4b43-b62a-1026afcf52e6

## Un framework agéntico personal y orgánico que crece y aprende contigo

- Agent Zero no es un framework agéntico predefinido. Está diseñado para ser dinámico, crecer orgánicamente y aprender a medida que lo usas.
- Agent Zero es completamente transparente, legible, comprensible, personalizable e interactivo.
- Agent Zero usa la computadora como una herramienta para lograr sus (tus) tareas.

# 💡 Características Principales

1. **Asistente de Propósito General**

- Agent Zero no está preprogramado para tareas específicas (pero puede estarlo). Está diseñado para ser un asistente personal de propósito general. Dale una tarea y recopilará información, ejecutará comandos y código, cooperará con otras instancias de agentes y hará todo lo posible para cumplirla.
- Tiene memoria persistente, lo que le permite memorizar soluciones previas, código, hechos, instrucciones, etc., para resolver tareas más rápido y de manera más confiable en el futuro.

![Agent 0 Trabajando](/docs/res/ui-screen-2.png)

2. **La Computadora como Herramienta**

- Agent Zero usa el sistema operativo como una herramienta para lograr sus tareas. No tiene herramientas de un solo propósito preprogramadas. En su lugar, puede escribir su propio código y usar la terminal para crear y usar sus propias herramientas según sea necesario.
- Las únicas herramientas predeterminadas en su arsenal son búsqueda en línea, funciones de memoria, comunicación (con el usuario y otros agentes) y ejecución de código/terminal. Todo lo demás es creado por el agente mismo o puede ser extendido por el usuario.
- La funcionalidad de uso de herramientas ha sido desarrollada desde cero para ser la más compatible y confiable, incluso con modelos muy pequeños.
- **Herramientas Predeterminadas:** Agent Zero incluye herramientas como conocimiento, contenido de páginas web, ejecución de código y comunicación.
- **Creación de Herramientas Personalizadas:** Extiende la funcionalidad de Agent Zero creando tus propias herramientas personalizadas.
- **Instrumentos:** Los instrumentos son un nuevo tipo de herramienta que te permite crear funciones y procedimientos personalizados que pueden ser llamados por Agent Zero.

3. **Cooperación Multi-agente**

- Cada agente tiene un agente superior que le da tareas e instrucciones. Cada agente luego reporta de vuelta a su superior.
- En el caso del primer agente en la cadena (Agent 0), el superior es el usuario humano; el agente no ve diferencia.
- Cada agente puede crear su agente subordinado para ayudar a desglosar y resolver subtareas. Esto ayuda a todos los agentes a mantener su contexto limpio y enfocado.

![Multi-agente](docs/res/physics.png)
![Multi-agente 2](docs/res/physics-2.png)

4. **Completamente Personalizable y Extensible**

- Casi nada en este framework está codificado de forma rígida. Nada está oculto. Todo puede ser extendido o cambiado por el usuario.
- Todo el comportamiento está definido por un prompt del sistema en el archivo **prompts/default/agent.system.md**. Cambia este prompt y cambia el framework dramáticamente.
- El framework no guía ni limita al agente de ninguna manera. No hay rieles codificados que los agentes tengan que seguir.
- Cada prompt, cada pequeña plantilla de mensaje enviada al agente en su bucle de comunicación se puede encontrar en la carpeta **prompts/** y cambiar.
- Cada herramienta predeterminada se puede encontrar en la carpeta **python/tools/** y cambiar o copiar para crear nuevas herramientas predefinidas.

![Prompts](/docs/res/prompts.png)

5. **La Comunicación es Clave**

- Dale a tu agente un prompt del sistema e instrucciones adecuadas, y puede hacer milagros.
- Los agentes pueden comunicarse con sus superiores y subordinados, haciendo preguntas, dando instrucciones y proporcionando orientación. Instruye a tus agentes en el prompt del sistema sobre cómo comunicarse efectivamente.
- La interfaz de terminal se transmite en tiempo real y es interactiva. Puedes detener e intervenir en cualquier momento. Si ves que tu agente va en la dirección equivocada, simplemente detente y díselo de inmediato.
- Hay mucha libertad en este framework. Puedes instruir a tus agentes para que reporten regularmente a sus superiores pidiendo permiso para continuar. Puedes instruirlos para que usen sistemas de puntuación al decidir cuándo delegar subtareas. Los superiores pueden verificar dos veces los resultados de los subordinados y disputar. Las posibilidades son infinitas.

## 🚀 Cosas que puedes construir con Agent Zero

- **Proyectos de Desarrollo** - `"Crea un dashboard de React con visualización de datos en tiempo real"`

- **Análisis de Datos** - `"Analiza los datos de ventas de NVIDIA del último trimestre y crea informes de tendencias"`

- **Creación de Contenido** - `"Escribe una publicación de blog técnica sobre microservicios"`

- **Administración de Sistemas** - `"Configura un sistema de monitoreo para nuestros servidores web"`

- **Investigación** - `"Recopila y resume cinco artículos recientes de IA sobre prompting CoT"`

# ⚙️ Instalación

Haz clic para abrir un video y aprender cómo instalar Agent Zero:

[![Video de Prueba](/docs/res/new_vid.jpg)](https://www.youtube.com/watch?v=cHDCCSr1YRI&t=24s)

Una guía de configuración detallada para Windows, macOS y Linux con un video se puede encontrar en la Documentación de Agent Zero en [esta página](./docs/installation.md).

### ⚡ Inicio Rápido

```bash
# Descargar y ejecutar con Docker

docker pull frdel/agent-zero-run
docker run -p 50001:80 frdel/agent-zero-run

# Visita http://localhost:50001 para comenzar
```

- Desarrolladores y colaboradores: descarga los binarios completos para tu sistema desde la [página de lanzamientos](https://github.com/frdel/agent-zero/releases) y luego sigue las instrucciones [proporcionadas aquí](./docs/installation.md#in-depth-guide-for-full-binaries-installation).

## 🐳 Completamente Dockerizado, con Speech-to-Text y TTS

![Configuración](docs/res/settings-page-ui.png)

- La configuración personalizable permite a los usuarios adaptar el comportamiento y las respuestas del agente a sus necesidades.
- La salida de la interfaz web es muy limpia, fluida, colorida, legible e interactiva; nada está oculto.
- Puedes cargar o guardar chats directamente dentro de la interfaz web.
- La misma salida que ves en la terminal se guarda automáticamente en un archivo HTML en la carpeta **logs/** para cada sesión.

![Ejemplo de tiempo](/docs/res/time_example.jpg)

- La salida del agente se transmite en tiempo real, permitiendo a los usuarios leer y intervenir en cualquier momento.
- No se requiere codificación; solo son necesarias habilidades de prompting y comunicación.
- Con un prompt del sistema sólido, el framework es confiable incluso con modelos pequeños, incluyendo uso preciso de herramientas.

## 👀 Ten en Cuenta

1. **¡Agent Zero Puede Ser Peligroso!**

- Con las instrucciones adecuadas, Agent Zero es capaz de muchas cosas, incluso acciones potencialmente peligrosas relacionadas con tu computadora, datos o cuentas. Siempre ejecuta Agent Zero en un entorno aislado (como Docker) y ten cuidado con lo que deseas.

2. **Agent Zero Está Basado en Prompts.**

- Todo el framework está guiado por la carpeta **prompts/**. Directrices del agente, instrucciones de herramientas, mensajes, funciones de IA de utilidad, todo está ahí.


## 📚 Lee la Documentación

| Página | Descripción |
|-------|-------------|
| [Instalación](./docs/installation.md) | Instalación, configuración y ajustes |
| [Uso](./docs/usage.md) | Uso básico y avanzado |
| [Arquitectura](./docs/architecture.md) | Diseño del sistema y componentes |
| [Contribuir](./docs/contributing.md) | Cómo contribuir |
| [Solución de Problemas](./docs/troubleshooting.md) | Problemas comunes y sus soluciones |

## 🎯 Registro de Cambios

### Próximamente

- **Herramientas de Conocimiento y RAG**
- **Planificación y Programación**

> [!IMPORTANT]
>
>**Cambios en la imagen Docker frdel/agent-zero desde v0.7:**
>
> La nueva imagen Docker `frdel/agent-zero-run` proporciona el nuevo entorno unificado.

### v0.8.1
- **Agente de Navegador**
- **Mejoras de UX**

### v0.8

- **Runtime de Docker**
- **Nuevo Sistema de Historial de Mensajes y Resumen**
- **Cambio y Gestión del Comportamiento del Agente**
- **Texto a Voz (TTS) y Voz a Texto (STT)**
- **Página de Configuración en la Interfaz Web**
- **Integración de SearXNG Reemplazando Perplexity + DuckDuckGo**
- **Funcionalidad de Explorador de Archivos**
- **Soporte de Visualización Matemática KaTeX**
- **Adjuntos de Archivos en el Chat**

### v0.7

- **Memoria Automática**
- **Mejoras de la Interfaz**
- **Instrumentos**
- **Framework de Extensiones**
- **Prompts de Reflexión**
- **Corrección de Errores**

## 🤝 Comunidad y Soporte

- [Únete a nuestro Discord](https://discord.gg/B8KZKNsPpj) para discusiones en vivo o [visita nuestra Comunidad Skool](https://www.skool.com/agent-zero).
- [Sigue nuestro canal de YouTube](https://www.youtube.com/@AgentZeroFW) para explicaciones prácticas y tutoriales
- [Reporta Problemas](https://github.com/frdel/agent-zero/issues) para correcciones de errores y características
