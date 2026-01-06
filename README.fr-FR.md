<div align="center">

![Agent Zero](/docs/res/header.png)

# `Agent Zero`

[![Thanks to Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Thanks%20to%20Sponsors-FF69B4?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/frdel) [![Join our Skool Community](https://img.shields.io/badge/Skool-Join%20our%20Community-4A90E2?style=for-the-badge&logo=skool&logoColor=white)](https://www.skool.com/agent-zero) [![Join our Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/B8KZKNsPpj) [![Subscribe on YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@AgentZeroFW) [![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jan-tomasek/) [![Follow on Warpcast](https://img.shields.io/badge/Warpcast-Follow-5A32F3?style=for-the-badge)](https://warpcast.com/agent-zero)

> **Note:** Agent Zero n'utilise pas Twitter/X. Tout compte Twitter/X prétendant représenter ce projet est faux.

[Installation](./docs/installation.md) •
[Comment mettre à jour](./docs/installation.md#how-to-update-agent-zero) •
[Documentation](./docs/README.md) •
[Utilisation](./docs/usage.md)

</div>


[![Showcase](/docs/res/showcase-thumb.png)](https://youtu.be/lazLNcEYsiQ)



Voir [www.agent-zero.ai](https://agent-zero.ai) pour plus d'informations

[![Browser Agent](/docs/res/web_screenshot.jpg)](https://agent-zero.ai)



> [!NOTE]
> **🎉 Sortie v0.8.1** : Propose désormais un agent de navigation capable d'utiliser Chromium pour les interactions web ! Cela permet à Agent Zero de naviguer sur le web, de collecter des informations et d'interagir avec le contenu web de manière autonome.


https://github.com/user-attachments/assets/c168759d-57d8-4b43-b62a-1026afcf52e6

## Un cadre agentique personnel et organique qui grandit et apprend avec vous

- Agent Zero n'est pas un cadre agentique prédéfini. Il est conçu pour être dynamique, évoluant de manière organique et apprenant à mesure que vous l'utilisez.
- Agent Zero est entièrement transparent, lisible, compréhensible, personnalisable et interactif.
- Agent Zero utilise l'ordinateur comme un outil pour accomplir ses (vos) tâches.

# 💡 Fonctionnalités clés

1. **Assistant polyvalent**

- Agent Zero n'est pas préprogrammé pour des tâches spécifiques (mais peut l'être). Il est destiné à être un assistant personnel polyvalent. Donnez-lui une tâche, et il recueillera des informations, exécutera des commandes et du code, coopérera avec d'autres instances d'agents, et fera de son mieux pour l'accomplir.
- Il dispose d'une mémoire persistante, lui permettant de mémoriser les solutions, le code, les faits, les instructions, etc. précédents, afin de résoudre les tâches plus rapidement et plus fiablement à l'avenir.

![Agent 0 Working](/docs/res/ui-screen-2.png)

2. **L'ordinateur comme outil**

- Agent Zero utilise le système d'exploitation comme un outil pour accomplir ses tâches. Il n'a pas d'outils à usage unique préprogrammés. Au lieu de cela, il peut écrire son propre code et utiliser le terminal pour créer et utiliser ses propres outils selon ses besoins.
- Les seuls outils par défaut de son arsenal sont la recherche en ligne, les fonctions de mémoire, la communication (avec l'utilisateur et d'autres agents) et l'exécution de code/terminal. Tout le reste est créé par l'agent lui-même ou peut être étendu par l'utilisateur.
- La fonctionnalité d'utilisation des outils a été développée à partir de zéro pour être la plus compatible et fiable, même avec de très petits modèles.
- **Outils par défaut :** Agent Zero comprend des outils tels que la connaissance, le contenu de la page web, l'exécution de code et la communication.
- **Création d'outils personnalisés :** Étendez les fonctionnalités d'Agent Zero en créant vos propres outils personnalisés.
- **Instruments :** Les instruments sont un nouveau type d'outil qui vous permet de créer des fonctions et des procédures personnalisées qui peuvent être appelées par Agent Zero.

3. **Coopération multi-agents**

- Chaque agent a un agent supérieur qui lui donne des tâches et des instructions. Chaque agent rend ensuite compte à son supérieur.
- Dans le cas du premier agent de la chaîne (Agent 0), le supérieur est l'utilisateur humain ; l'agent ne voit aucune différence.
- Chaque agent peut créer son agent subordonné pour aider à décomposer et à résoudre les sous-tâches. Cela aide tous les agents à garder leur contexte clair et ciblé.

![Multi-agent](docs/res/physics.png)
![Multi-agent 2](docs/res/physics-2.png)

4. **Entièrement personnalisable et extensible**

- Presque rien dans ce cadre n'est codé en dur. Rien n'est caché. Tout peut être étendu ou modifié par l'utilisateur.
- Le comportement global est défini par une invite système dans le fichier **prompts/default/agent.system.md**. Modifiez cette invite et changez considérablement le cadre.
- Le cadre ne guide ni ne limite l'agent d'aucune manière. Il n'y a pas de rails codés en dur que les agents doivent suivre.
- Chaque invite, chaque petit modèle de message envoyé à l'agent dans sa boucle de communication peut être trouvé dans le dossier **prompts/** et modifié.
- Chaque outil par défaut peut être trouvé dans le dossier **python/tools/** et modifié ou copié pour créer de nouveaux outils prédéfinis.

![Prompts](/docs/res/prompts.png)

5. **La communication est la clé**

- Donnez à votre agent une invite système et des instructions appropriées, et il peut faire des miracles.
- Les agents peuvent communiquer avec leurs supérieurs et leurs subordonnés, poser des questions, donner des instructions et fournir des conseils. Expliquez à vos agents dans l'invite système comment communiquer efficacement.
- L'interface du terminal est diffusée en temps réel et interactive. Vous pouvez l'arrêter et intervenir à tout moment. Si vous voyez votre agent se diriger dans la mauvaise direction, arrêtez-le et dites-le-lui immédiatement.
- Il y a beaucoup de liberté dans ce cadre. Vous pouvez demander à vos agents de faire régulièrement rapport à leurs supérieurs pour obtenir la permission de continuer. Vous pouvez leur demander d'utiliser des systèmes de points lorsqu'ils décident de déléguer des sous-tâches. Les supérieurs peuvent vérifier les résultats de leurs subordonnés et contester. Les possibilités sont infinies.

## 🚀 Ce que vous pouvez construire avec Agent Zero

- **Projets de développement** - `"Créer un tableau de bord React avec visualisation de données en temps réel"`

- **Analyse de données** - `"Analyser les données de ventes de NVIDIA du dernier trimestre et créer des rapports de tendances"`

- **Création de contenu** - `"Écrire un article de blog technique sur les microservices"`

- **Administration système** - `"Mettre en place un système de surveillance pour nos serveurs web"`

- **Recherche** - `"Recueillir et résumer cinq articles récents sur l'IA concernant le prompting CoT"`

# ⚙️ Installation

Cliquez pour ouvrir une vidéo pour apprendre à installer Agent Zero :

[![Testing Video](/docs/res/new_vid.jpg)](https://www.youtube.com/watch?v=cHDCCSr1YRI&t=24s)

Un guide de configuration détaillé pour Windows, macOS et Linux avec une vidéo peut être trouvé dans la documentation d'Agent Zero à [cette page](./docs/installation.md).

### ⚡ Démarrage rapide

```bash
# Télécharger et exécuter avec Docker

docker pull frdel/agent-zero-run
docker run -p 50001:80 frdel/agent-zero-run

# Visiter http://localhost:50001 pour démarrer
```

- Développeurs et contributeurs : téléchargez les binaires complets pour votre système depuis la [page des versions](https://github.com/frdel/agent-zero/releases), puis suivez les instructions [fournies ici](./docs/installation.md#in-depth-guide-for-full-binaries-installation).

## 🐳 Entièrement Dockerisé, avec synthèse vocale et reconnaissance vocale

![Settings](docs/res/settings-page-ui.png)

- Les paramètres personnalisables permettent aux utilisateurs d'adapter le comportement et les réponses de l'agent à leurs besoins.
- La sortie de l'interface utilisateur Web est très propre, fluide, colorée, lisible et interactive ; rien n'est caché.
- Vous pouvez charger ou enregistrer des discussions directement dans l'interface utilisateur Web.
- La même sortie que vous voyez dans le terminal est automatiquement enregistrée dans un fichier HTML dans le dossier **logs/** pour chaque session.

![Time example](/docs/res/time_example.jpg)

- La sortie de l'agent est diffusée en temps réel, permettant aux utilisateurs de lire et d'intervenir à tout moment.
- Aucun codage n'est requis ; seules des compétences en matière de sollicitation et de communication sont nécessaires.
- Avec une invite système solide, le cadre est fiable même avec de petits modèles, y compris l'utilisation précise des outils.

## 👀 Gardez à l'esprit

1. **Agent Zero peut être dangereux !**

- Avec des instructions appropriées, Agent Zero est capable de nombreuses choses, même des actions potentiellement dangereuses concernant votre ordinateur, vos données ou vos comptes. Exécutez toujours Agent Zero dans un environnement isolé (comme Docker) et faites attention à ce que vous souhaitez.

2. **Agent Zero est basé sur les invites.**

- L'ensemble du cadre est guidé par le dossier **prompts/**. Les directives de l'agent, les instructions d'outils, les messages, les fonctions d'IA utilitaires, tout est là.


## 📚 Lire la documentation

| Page | Description |
|-------|-------------|
| [Installation](./docs/installation.md) | Installation, configuration et paramétrage |
| [Utilisation](./docs/usage.md) | Utilisation de base et avancée |
| [Architecture](./docs/architecture.md) | Conception du système et composants |
| [Contribuer](./docs/contributing.md) | Comment contribuer |
| [Dépannage](./docs/troubleshooting.md) | Problèmes courants et leurs solutions |

## 🎯 Journal des modifications

### Bientôt disponible

- **Outils de connaissance et RAG**
- **Planification et ordonnancement**

> [!IMPORTANT]
>
>**Modifications de l'image Docker frdel/agent-zero depuis v0.7 :**
>
> La nouvelle image Docker `frdel/agent-zero-run` fournit le nouvel environnement unifié.

### v0.8.1
- **Agent de navigation**
- **Améliorations de l'UX**

### v0.8

- **Exécution Docker**
- **Nouveau système d'historique et de résumé des messages**
- **Changement et gestion du comportement de l'agent**
- **Synthèse vocale (TTS) et reconnaissance vocale (STT)**
- **Page de paramètres dans l'interface utilisateur Web**
- **Intégration de SearXNG remplaçant Perplexity + DuckDuckGo**
- **Fonctionnalité de navigateur de fichiers**
- **Prise en charge de la visualisation mathématique KaTeX**
- **Pièces jointes de fichiers dans le chat**

### v0.7

- **Mémoire automatique**
- **Améliorations de l'interface utilisateur**
- **Instruments**
- **Cadre d'extensions**
- **Invites de réflexion**
- **Corrections de bogues**

## 🤝 Communauté et support

- [Rejoignez notre Discord](https://discord.gg/B8KZKNsPpj) pour des discussions en direct ou [visitez notre communauté Skool](https://www.skool.com/agent-zero).
- [Suivez notre chaîne YouTube](https://www.youtube.com/@AgentZeroFW) pour des explications pratiques et des tutoriels
- [Signalez les problèmes](https://github.com/frdel/agent-zero/issues) pour les corrections de bogues et les fonctionnalités
