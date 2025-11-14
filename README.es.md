<div align="center">

![Agent Zero](/docs/res/header.png)

# `Agent Zero`

[![Gracias a los Patrocinadores](https://img.shields.io/badge/GitHub%20Sponsors-Gracias%20a%20los%20Patrocinadores-FF69B4?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/frdel) [![Únete a nuestra Comunidad Skool](https://img.shields.io/badge/Skool-Únete%20a%20nuestra%20Comunidad-4A90E2?style=for-the-badge&logo=skool&logoColor=white)](https://www.skool.com/agent-zero) [![Únete a nuestro Discord](https://img.shields.io/badge/Discord-Únete%20a%20nuestro%20servidor-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/B8KZKNsPpj) [![Suscríbete en YouTube](https://img.shields.io/badge/YouTube-Suscríbete-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@AgentZeroFW) [![Conecta en LinkedIn](https://img.shields.io/badge/LinkedIn-Conecta-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jan-tomasek/) [![Síguenos en Warpcast](https://img.shields.io/badge/Warpcast-Síguenos-5A32F3?style=for-the-badge)](https://warpcast.com/agent-zero)

> **Nota:** Agent Zero no utiliza Twitter/X. Cualquier cuenta de Twitter/X que afirme representar este proyecto es falsa.

[Instalación](./docs/installation.md) •
[Cómo actualizar](./docs/installation.md#how-to-update-agent-zero) •
[Documentación](./docs/README.md) •
[Uso](./docs/usage.md)

</div>



[![Presentación](/docs/res/showcase-thumb.png)](https://youtu.be/lazLNcEYsiQ)



Visita [www.agent-zero.ai](https://agent-zero.ai) para más información

[![Agente de Navegador](/docs/res/web_screenshot.jpg)](https://agent-zero.ai)



> [!NOTE]
> **🎉 Versión v0.8.1**: ¡Ahora incluye un agente de navegador capaz de usar Chromium para interacciones web! Esto permite que Agent Zero navegue por la web, recopile información e interactúe con contenido web de manera autónoma.


https://github.com/user-attachments/assets/c168759d-57d8-4b43-b62a-1026afcf52e6

## Un marco de agentes personal y orgánico que crece y aprende contigo

- Agent Zero no es un marco de agentes predefinido. Está diseñado para ser dinámico, creciendo orgánicamente y aprendiendo a medida que lo usas.
- Agent Zero es completamente transparente, legible, comprensible, personalizable e interactivo.
- Agent Zero utiliza la computadora como herramienta para lograr sus (tus) tareas.

# 💡 Características Principales

1. **Asistente de Propósito General**

- Agent Zero no está preprogramado para tareas específicas (pero puede serlo). Está destinado a ser un asistente personal de propósito general. Dale una tarea, y recopilará información, ejecutará comandos y código, cooperará con otras instancias de agentes, y hará lo mejor para lograrlo.
- Tiene una memoria persistente, permitiéndole memorizar soluciones anteriores, código, hechos, instrucciones, etc., para resolver tareas más rápido y de manera más confiable en el futuro.

![Agent 0 Working](/docs/res/ui-screen-2.png)

2. **Computadora como Herramienta**

- Agent Zero utiliza el sistema operativo como herramienta para lograr sus tareas. No tiene herramientas de propósito único preprogramadas. En su lugar, puede escribir su propio código y usar el terminal para crear y usar sus propias herramientas según sea necesario.
- Las únicas herramientas predeterminadas en su arsenal son búsqueda en línea, características de memoria, comunicación (con el usuario y otros agentes), y ejecución de código/terminal. Todo lo demás es creado por el agente mismo o puede ser extendido por el usuario.
- La funcionalidad de uso de herramientas ha sido desarrollada desde cero para ser la más compatible y confiable, incluso con modelos muy pequeños.
- **Herramientas Predeterminadas:** Agent Zero incluye herramientas como conocimiento, contenido de páginas web, ejecución de código y comunicación.
- **Creando Herramientas Personalizadas:** Extiende la funcionalidad de Agent Zero creando tus propias herramientas personalizadas.
- **Instrumentos:** Los instrumentos son un nuevo tipo de herramienta que te permiten crear funciones y procedimientos personalizados que pueden ser llamados por Agent Zero.

3. **Cooperación Multi-agente**

- Cada agente tiene un agente superior que le da tareas e instrucciones. Cada agente luego informa de vuelta a su superior.
- En el caso del primer agente en la cadena (Agent 0), el superior es el usuario humano; el agente no ve diferencia.
- Cada agente puede crear su agente subordinado para ayudar a desglosar y resolver subtareas. Esto ayuda a todos los agentes a mantener su contexto limpio y enfocado.

![Multi-agent](docs/res/physics.png)
![Multi-agent 2](docs/res/physics-2.png)

4. **Completamente Personalizable y Extensible**

- Casi nada en este marco está codificado de manera rígida. Nada está oculto. Todo puede ser extendido o cambiado por el usuario.
- Todo el comportamiento está definido por un prompt del sistema en el archivo **prompts/default/agent.system.md**. Cambia este prompt y cambia el marco dramáticamente.
- El marco no guía ni limita al agente de ninguna manera. No hay rieles codificados rígidamente que los agentes deban seguir.
- Cada prompt, cada pequeña plantilla de mensaje enviada al agente en su bucle de comunicación se puede encontrar en la carpeta **prompts/** y cambiar.
- Cada herramienta predeterminada se puede encontrar en la carpeta **python/tools/** y cambiar o copiar para crear nuevas herramientas predefinidas.

![Prompts](/docs/res/prompts.png)

5. **La Comunicación es Clave**

- Dale a tu agente un prompt del sistema apropiado e instrucciones, y puede hacer milagros.
- Los agentes pueden comunicarse con sus superiores y subordinados, haciendo preguntas, dando instrucciones y proporcionando guía. Instruye a tus agentes en el prompt del sistema sobre cómo comunicarse efectivamente.
- La interfaz de terminal es transmitida en tiempo real y es interactiva. Puedes detener e intervenir en cualquier punto. Si ves que tu agente se dirige en la dirección equivocada, simplemente detén y dile en el acto.
- Hay mucha libertad en este marco. Puedes instruir a tus agentes para que informen regularmente de vuelta a superiores pidiendo permiso para continuar. Puedes instruirlos a usar sistemas de puntuación cuando decidan cuándo delegar subtareas. Los superiores pueden verificar dos veces los resultados de subordinados y disputar. Las posibilidades son infinitas.

## 🚀 Cosas que puedes construir con Agent Zero

- **Proyectos de Desarrollo** - `"Crea un dashboard de React con visualización de datos en tiempo real"`

- **Análisis de Datos** - `"Analiza los datos de ventas del último trimestre de NVIDIA y crea informes de tendencias"`

- **Creación de Contenido** - `"Escribe un post de blog técnico sobre microservicios"`

- **Administración de Sistemas** - `"Configura un sistema de monitoreo para nuestros servidores web"`

- **Investigación** - `"Reúne y resume cinco artículos recientes de IA sobre prompting CoT"`

# ⚙️ Instalación

Haz clic para abrir un video y aprender cómo instalar Agent Zero:

[![Video de Prueba](/docs/res/new_vid.jpg)](https://www.youtube.com/watch?v=cHDCCSr1YRI&t=24s)

Una guía detallada de configuración para Windows, macOS y Linux con video se puede encontrar en la Documentación de Agent Zero en [esta página](./docs/installation.md).

### ⚡ Inicio Rápido

```bash
# Extrae y ejecuta con Docker

docker pull frdel/agent-zero-run
docker run -p 50001:80 frdel/agent-zero-run

# Visita http://localhost:50001 para comenzar
```

- Desarrolladores y contribuidores: descarga los binarios completos para tu sistema desde la [página de releases](https://github.com/frdel/agent-zero/releases) y luego sigue las instrucciones [proporcionadas aquí](./docs/installation.md#in-depth-guide-for-full-binaries-installation).

## 🐳 Completamente Dockerizado, con Voz-a-Texto y Texto-a-Voz

![Configuraciones](docs/res/settings-page-ui.png)

- Las configuraciones personalizables permiten a los usuarios adaptar el comportamiento y respuestas del agente a sus necesidades.
- La salida de la UI Web es muy limpia, fluida, colorida, legible e interactiva; nada está oculto.
- Puedes cargar o guardar chats directamente dentro de la UI Web.
- La misma salida que ves en el terminal se guarda automáticamente en un archivo HTML en la carpeta **logs/** para cada sesión.

![Ejemplo de tiempo](/docs/res/time_example.jpg)

- La salida del agente se transmite en tiempo real, permitiendo a los usuarios leer junto y intervenir en cualquier momento.
- No se requiere codificación; solo habilidades de prompting y comunicación son necesarias.
- Con un prompt del sistema sólido, el marco es confiable incluso con modelos pequeños, incluyendo uso preciso de herramientas.

## 👀 Ten en Cuenta

1. **¡Agent Zero Puede Ser Peligroso!**

- Con instrucción apropiada, Agent Zero es capaz de muchas cosas, incluso acciones potencialmente peligrosas relacionadas con tu computadora, datos o cuentas. Siempre ejecuta Agent Zero en un entorno aislado (como Docker) y ten cuidado con lo que deseas.

2. **Agent Zero Es Basado en Prompts.**

- Todo el marco está guiado por la carpeta **prompts/**. Directrices de agentes, instrucciones de herramientas, mensajes, funciones de IA utilitarias, todo está ahí.


## 📚 Lee la Documentación

| Página | Descripción |
|-------|-------------|
| [Instalación](./docs/installation.md) | Instalación, configuración y configuración |
| [Uso](./docs/usage.md) | Uso básico y avanzado |
| [Arquitectura](./docs/architecture.md) | Diseño del sistema y componentes |
| [Contribuyendo](./docs/contributing.md) | Cómo contribuir |
| [Solución de Problemas](./docs/troubleshooting.md) | Problemas comunes y sus soluciones |

## 🎯 Registro de Cambios

### Próximamente

- **Herramientas de Conocimiento y RAG**
- **Planificación y Programación**

> [!IMPORTANT]
>
>**Cambios a la imagen de Docker frdel/agent-zero desde v0.7:**
>
> La nueva imagen de Docker `frdel/agent-zero-run` proporciona el nuevo entorno unificado.

### v0.8.1
- **Agente de Navegador**
- **Mejoras de UX**

### v0.8

- **Entorno de Ejecución Docker**
- **Nuevo Sistema de Historial de Mensajes y Resumen**
- **Cambio y Gestión del Comportamiento del Agente**
- **Texto-a-Voz (TTS) y Voz-a-Texto (STT)**
- **Página de Configuraciones en UI Web**
- **Integración de SearXNG Reemplazando Perplexity + DuckDuckGo**
- **Funcionalidad de Navegador de Archivos**
- **Soporte de Visualización Matemática KaTeX**
- **Adjuntos de Archivos en el Chat**

### v0.7

- **Memoria Automática**
- **Mejoras de UI**
- **Instrumentos**
- **Marco de Extensiones**
- **Prompts de Reflexión**
- **Correcciones de Errores**

## 🤝 Comunidad y Soporte

- [Únete a nuestro Discord](https://discord.gg/B8KZKNsPpj) para discusiones en vivo o [visita nuestra Comunidad Skool](https://www.skool.com/agent-zero).
- [Sigue nuestro canal de YouTube](https://www.youtube.com/@AgentZeroFW) para explicaciones prácticas y tutoriales
- [Reporta Problemas](https://github.com/frdel/agent-zero/issues) para correcciones de errores y características