from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Nom du modèle Hugging Face (remplace si tu changes)
model_id = "mistralai/Mistral-7B-Instruct-v0.2"

# Ton token Hugging Face
HF_TOKEN = "hf_xxx_REPLACE_ME_xxx"

# Charger tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    model_id,
    token=HF_TOKEN
)

# Charger modèle
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    token=HF_TOKEN
)

def get_response(prompt: str) -> str:
    system_message = (
        "Tu es un chatbot professionnel, spécialisé en réponses claires et courtes. "
        "Si la question n'est pas claire, demande des précisions. "
        "Voici la question de l'utilisateur : "
    )
    full_prompt = system_message + prompt

    inputs = tokenizer(full_prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        do_sample=True,
        top_p=0.9,
        temperature=0.7
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

