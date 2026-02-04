import torch
from transformers import AutoTokenizer , AutoModelForCausalLM

Model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(Model_name)
model = AutoModelForCausalLM.from_pretrained(Model_name,
                                             device_map = "auto")


print("Chatbot hazır . Çıkmak için 'exit' yazınız")

system_prompt = (
    "You are helpful assistant."
    "You can answer factual questions and also compare fictional characters."
)

chat_history = [
    {"role": "system" , "content": system_prompt}
]

while True:
    user_input = input("Sen :")

    if user_input.lower() == "exit":
        break

    chat_history.append({"role":"user" , "content": user_input})

    prompt = tokenizer.apply_chat_template(
        chat_history,
        tokenize = False,
        add_generation_prompt = True
    )

    inputs = tokenizer(prompt , return_tensors = "pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens = 256,
        temperature = 0.7,
        top_p = 0.9,
        do_sample = True
    )

    response = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[-1]:]
    )

    print("Chatbot :" , response)
    chat_history.append({"role": "assistant" , "content" : response})
    
