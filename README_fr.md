<div align="center">

![Agent Zero](/docs/res/header.png)

# `Agent Zero`

[![Merci aux sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Merci%20aux%20sponsors-FF69B4?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/frdel) [![Rejoignez notre communauté Skool](https://img.shields.io/badge/Skool-Rejoignez%20notre%20communauté-4A90E2?style=for-the-badge&logo=skool&logoColor=white)](https://www.skool.com/agent-zero) [![Rejoignez notre Discord](https://img.shields.io/badge/Discord-Rejoignez%20notre%20serveur-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/B8KZKNsPpj) [![Abonnez-vous sur YouTube](https://img.shields.io/badge/YouTube-Abonnez--vous-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@AgentZeroFW) [![Connectez-vous sur LinkedIn](https://img.shields.io/badge/LinkedIn-Connectez--vous-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jan-tomasek/) [![Suivez sur Warpcast](https://img.shields.io/badge/Warpcast-Suivez-5A32F3?style=for-the-badge)](https://warpcast.com/agent-zero)

> **Note :** Agent Zero n'utilise pas Twitter/X. Tout compte Twitter/X prétendant représenter ce projet est frauduleux.

[Installation](./docs/installation.md) •
[Comment mettre à jour](./docs/installation.md#how-to-update-agent-zero) •
[Documentation](./docs/README.md) •
[Utilisation](./docs/usage.md)

</div>


[![Démonstration](/docs/res/showcase-thumb.png)](https://youtu.be/lazLNcEYsiQ)



Visitez [www.agent-zero.ai](https://agent-zero.ai) pour plus d'informations

[![Agent navigateur](/docs/res/web_screenshot.jpg)](https://agent-zero.ai)



> [!NOTE]
> **🎉 Version 0.8.1** : Désormais doté d'un agent navigateur capable d'utiliser Chromium pour les interactions web ! Cela permet à Agent Zero de naviguer sur le web, de collecter des informations et d'interagir avec le contenu web de manière autonome.


https://github.com/user-attachments/assets/c168759d-57d8-4b43-b62a-1026afcf52e6

## Un framework agentique personnel et organique qui grandit et apprend avec vous

- Agent Zero n'est pas un framework agentique prédéfini. Il est conçu pour être dynamique, croître de manière organique et apprendre au fur et à mesure que vous l'utilisez.
- Agent Zero est entièrement transparent, lisible, compréhensible, personnalisable et interactif.
- Agent Zero utilise l'ordinateur comme un outil pour accomplir ses (vos) tâches.

# 💡 Fonctionnalités clés

1. **Assistant polyvalent**

- Agent Zero n'est pas préprogrammé pour des tâches spécifiques (mais peut l'être). Il est conçu pour être un assistant personnel polyvalent. Donnez-lui une tâche, et il collectera des informations, exécutera des commandes et du code, coopérera avec d'autres instances d'agents, et fera de son mieux pour l'accomplir.
- Il dispose d'une mémoire persistante, lui permettant de mémoriser les solutions précédentes, le code, les faits, les instructions, etc., pour résoudre les tâches plus rapidement et de manière plus fiable à l'avenir.

![Agent 0 en action](/docs/res/ui-screen-2.png)

2. **L'ordinateur comme outil**

- Agent Zero utilise le système d'exploitation comme un outil pour accomplir ses tâches. Il n'a pas d'outils à usage unique préprogrammés. Au lieu de cela, il peut écrire son propre code et utiliser le terminal pour créer et utiliser ses propres outils selon les besoins.
- Les seuls outils par défaut dans son arsenal sont la recherche en ligne, les fonctionnalités de mémoire, la communication (avec l'utilisateur et d'autres agents), et l'exécution de code/terminal. Tout le reste est créé par l'agent lui-même ou peut être étendu par l'utilisateur.
- La fonctionnalité d'utilisation des outils a été développée à partir de zéro pour être la plus compatible et fiable, même avec de très petits modèles.
- **Outils par défaut :** Agent Zero inclut des outils comme la connaissance, le contenu de pages web, l'exécution de code et la communication.
- **Création d'outils personnalisés :** Étendez les fonctionnalités d'Agent Zero en créant vos propres outils personnalisés.
- **Instruments :** Les instruments sont un nouveau type d'outil qui vous permet de créer des fonctions et procédures personnalisées pouvant être appelées par Agent Zero.

3. **Coopération multi-agents**

- Chaque agent a un agent supérieur qui lui donne des tâches et des instructions. Chaque agent rend ensuite compte à son supérieur.
- Dans le cas du premier agent de la chaîne (Agent 0), le supérieur est l'utilisateur humain ; l'agent ne voit aucune différence.
- Chaque agent peut créer son agent subordonné pour aider à décomposer et résoudre des sous-tâches. Cela aide tous les agents à garder leur contexte propre et concentré.

![Multi-agent](docs/res/physics.png)
![Multi-agent 2](docs/res/physics-2.png)

4. **Entièrement personnalisable et extensible**

- Presque rien dans ce framework n'est codé en dur. Rien n'est caché. Tout peut être étendu ou modifié par l'utilisateur.
- Le comportement entier est défini par un prompt système dans le fichier **prompts/default/agent.system.md**. Changez ce prompt et changez radicalement le framework.
- Le framework ne guide ni ne limite l'agent d'aucune manière. Il n'y a pas de rails codés en dur que les agents doivent suivre.
- Chaque prompt, chaque petit modèle de message envoyé à l'agent dans sa boucle de communication peut être trouvé dans le dossier **prompts/** et modifié.
- Chaque outil par défaut peut être trouvé dans le dossier **python/tools/** et modifié ou copié pour créer de nouveaux outils prédéfinis.

![Prompts](/docs/res/prompts.png)

5. **La communication est essentielle**

- Donnez à votre agent un prompt système et des instructions appropriés, et il peut faire des miracles.
- Les agents peuvent communiquer avec leurs supérieurs et subordonnés, poser des questions, donner des instructions et fournir des conseils. Instruisez vos agents dans le prompt système sur la façon de communiquer efficacement.
- L'interface terminal est diffusée en temps réel et interactive. Vous pouvez arrêter et intervenir à tout moment. Si vous voyez votre agent partir dans la mauvaise direction, arrêtez-le et dites-le-lui immédiatement.
- Il y a beaucoup de liberté dans ce framework. Vous pouvez instruire vos agents de faire régulièrement des rapports à leurs supérieurs en demandant la permission de continuer. Vous pouvez les instruire d'utiliser des systèmes de notation par points pour décider quand déléguer des sous-tâches. Les supérieurs peuvent vérifier les résultats des subordonnés et contester. Les possibilités sont infinies.

## 🚀 Ce que vous pouvez construire avec Agent Zero

- **Projets de développement** - `"Créer un tableau de bord React avec visualisation de données en temps réel"`

- **Analyse de données** - `"Analyser les données de ventes NVIDIA du dernier trimestre et créer des rapports de tendances"`

- **Création de contenu** - `"Écrire un article de blog technique sur les microservices"`

- **Administration système** - `"Configurer un système de surveillance pour nos serveurs web"`

- **Recherche** - `"Rassembler et résumer cinq articles récents sur l'IA concernant le prompting CoT"`

# ⚙️ Installation

Cliquez pour ouvrir une vidéo pour apprendre comment installer Agent Zero :

[![Vidéo de test](/docs/res/new_vid.jpg)](https://www.youtube.com/watch?v=cHDCCSr1YRI&t=24s)

Un guide d'installation détaillé pour Windows, macOS et Linux avec une vidéo peut être trouvé dans la documentation d'Agent Zero sur [cette page](./docs/installation.md).

### ⚡ Démarrage rapide

```bash
# Télécharger et exécuter avec Docker

docker pull frdel/agent-zero-run
docker run -p 50001:80 frdel/agent-zero-run

# Visitez http://localhost:50001 pour commencer
```

- Développeurs et contributeurs : téléchargez les binaires complets pour votre système depuis la [page des versions](https://github.com/frdel/agent-zero/releases) puis suivez les instructions [fournies ici](./docs/installation.md#in-depth-guide-for-full-binaries-installation).

## 🐳 Entièrement dockerisé, avec reconnaissance vocale et synthèse vocale

![Paramètres](docs/res/settings-page-ui.png)

- Les paramètres personnalisables permettent aux utilisateurs d'adapter le comportement et les réponses de l'agent à leurs besoins.
- La sortie de l'interface web est très propre, fluide, colorée, lisible et interactive ; rien n'est caché.
- Vous pouvez charger ou sauvegarder des conversations directement dans l'interface web.
- La même sortie que vous voyez dans le terminal est automatiquement sauvegardée dans un fichier HTML dans le dossier **logs/** pour chaque session.

![Exemple de temps](/docs/res/time_example.jpg)

- La sortie de l'agent est diffusée en temps réel, permettant aux utilisateurs de lire en même temps et d'intervenir à tout moment.
- Aucun codage n'est requis ; seules des compétences en prompting et en communication sont nécessaires.
- Avec un prompt système solide, le framework est fiable même avec de petits modèles, y compris l'utilisation précise des outils.

## 👀 Gardez à l'esprit

1. **Agent Zero peut être dangereux !**

- Avec des instructions appropriées, Agent Zero est capable de beaucoup de choses, même d'actions potentiellement dangereuses concernant votre ordinateur, vos données ou vos comptes. Exécutez toujours Agent Zero dans un environnement isolé (comme Docker) et faites attention à ce que vous souhaitez.

2. **Agent Zero est basé sur des prompts.**

- L'ensemble du framework est guidé par le dossier **prompts/**. Les directives de l'agent, les instructions des outils, les messages, les fonctions d'IA utilitaires, tout est là.


## 📚 Lire la documentation

| Page | Description |
|-------|-------------|
| [Installation](./docs/installation.md) | Installation, configuration et paramétrage |
| [Utilisation](./docs/usage.md) | Utilisation basique et avancée |
| [Architecture](./docs/architecture.md) | Conception du système et composants |
| [Contribution](./docs/contributing.md) | Comment contribuer |
| [Dépannage](./docs/troubleshooting.md) | Problèmes courants et leurs solutions |

## 🎯 Journal des modifications

### Prochainement

- **Outils de connaissance et RAG**
- **Planification et ordonnancement**

> [!IMPORTANT]
>
>**Modifications de l'image Docker frdel/agent-zero depuis la v0.7 :**
>
> La nouvelle image Docker `frdel/agent-zero-run` fournit le nouvel environnement unifié.

### v0.8.1
- **Agent navigateur**
- **Améliorations de l'expérience utilisateur**

### v0.8

- **Runtime Docker**
- **Nouveau système d'historique et de résumé des messages**
- **Changement et gestion du comportement de l'agent**
- **Synthèse vocale (TTS) et reconnaissance vocale (STT)**
- **Page de paramètres dans l'interface web**
- **Intégration SearXNG remplaçant Perplexity + DuckDuckGo**
- **Fonctionnalité de navigateur de fichiers**
- **Support de visualisation mathématique KaTeX**
- **Pièces jointes dans le chat**

### v0.7

- **Mémoire automatique**
- **Améliorations de l'interface utilisateur**
- **Instruments**
- **Framework d'extensions**
- **Prompts de réflexion**
- **Corrections de bugs**

## 🤝 Communauté et support

- [Rejoignez notre Discord](https://discord.gg/B8KZKNsPpj) pour des discussions en direct ou [visitez notre communauté Skool](https://www.skool.com/agent-zero).
- [Suivez notre chaîne YouTube](https://www.youtube.com/@AgentZeroFW) pour des explications pratiques et des tutoriels
- [Signaler des problèmes](https://github.com/frdel/agent-zero/issues) pour les corrections de bugs et les fonctionnalités
