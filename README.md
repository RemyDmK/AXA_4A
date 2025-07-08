# Teams Chatbot

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
- Gère la logique d’envoi du texte au modèle

**Libs utilisées :**

- FastAPI
- Transformers (Hugging Face)
---

### LLM Hugging Face (`gpt.py`)

**Responsabilité :**

- Charger le modèle Hugging Face (Mistral ou autre, pour le moment : "mistralai/Mistral-7B-Instruct-v0.2" car le modèle tourne sur une RTX 3060)
- Générer une réponse à partir d’un texte

---

### Bot Framework Adapter (`app.py`, `bot_logic.py`)

**Responsabilité :**

- Se connecter à Teams (ou Bot Framework Emulator)
- Recevoir les messages texte des utilisateurs
- Poster la réponse du bot dans Teams
