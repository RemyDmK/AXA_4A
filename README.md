# AXA Teams Chatbot

Projet pour construire un chatbot intégré à Microsoft Teams, capable d’utiliser un modèle pour répondre aux questions des utilisateurs en temps réel pendant une réunion teams.

---

## 🚀 Objectif du projet

✅ Un bot dans Teams
✅ Capable d’écouter des conversations pendant une réunion et de répondre à des messages écrits
✅ Spécialisé dans un domaine
✅ Fonctionnant en temps réel

---

## ⚙️ Architecture


## 🧩 Composants

### FastAPI (`main.py`)

**Responsabilité :**

- Expose l’API `/process-text/`
- Gère la logique d’envoi du texte au modèle LLM

**Libs utilisées :**

- FastAPI
- Transformers (Hugging Face)
- Torch

---

### LLM Hugging Face (`gpt.py`)

**Responsabilité :**

- Charger le modèle Hugging Face (Mistral ou autre)
- Générer une réponse à partir d’un texte

**Atouts :**

- Possibilité de changer le modèle facilement
- Modèle chargé une seule fois en mémoire, performant pour plusieurs requêtes

**Paramètres que tu contrôles :**

- `max_new_tokens`
- `temperature`
- `top_p`

---

### Bot Framework Adapter (`app.py`, `bot_logic.py`)

**Responsabilité :**

- Se connecter à Teams (ou Bot Framework Emulator)
- Recevoir les messages texte des utilisateurs
- Poster la réponse du bot dans Teams

**Workflow :**

1. Bot reçoit un message d’un utilisateur
2. Bot appelle FastAPI avec le texte
3. Bot récupère la réponse
4. Bot renvoie la réponse à l’utilisateur Teams
