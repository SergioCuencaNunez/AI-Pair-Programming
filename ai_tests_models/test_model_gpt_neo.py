from transformers import pipeline
import time

t1 = round(time.time() * 1000)
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')
t2 = round(time.time() * 1000)

print(f"Tiempo en cargar el modelo: {t2-t1}")

file = open('./prompts.txt', 'r')
lines = file.readlines()

t3 = round(time.time() * 1000)
for line in lines:
    t5 = round(time.time() * 1000)
    res = generator(line, do_sample=True, max_length=200)
    print(res)
    t6 = round(time.time() * 1000)
    print(f"Tiempo en resolver un problema: {t6-t5}")
t4 = round(time.time() * 1000)
print(f"Tiempo en resolver todos los problemas: {t4-t3}")