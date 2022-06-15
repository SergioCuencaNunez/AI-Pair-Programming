from transformers import AutoTokenizer, AutoModelForCausalLM
import time

t1 = round(time.time() * 1000)
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6B")
t2 = round(time.time() * 1000)

file = open('./prompts.txt', 'r')
lines = file.readlines()

t3 = round(time.time() * 1000)
for line in lines:
    t5 = round(time.time() * 1000)
    input_ids = tokenizer(line, return_tensors="pt").input_ids
    output = model.generate(input_ids)
    print(tokenizer.decode(output[0], skip_special_tokens=True))
    t6 = round(time.time() * 1000)
    print(f"Tiempo en resolver un problema: {t6-t5}")
t4 = round(time.time() * 1000)
print(f"Tiempo en resolver todos los problemas: {t4-t3}")
