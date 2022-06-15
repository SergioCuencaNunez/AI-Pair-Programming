from transformers import pipeline, set_seed
import time

t1 = round(time.time() * 1000)
generator = pipeline('text-generation', model='microsoft/CodeGPT-small-py')
#generator_adapted = pipeline('text-generation', model='microsoft/CodeGPT-small-py-adaptedGPT2')
t2 = round(time.time() * 1000)

print(f"Tiempo en cargar el modelo: {t2-t1}")

set_seed(42)
file = open('./ai_tests_models/prompts.txt', 'r')
lines = file.readlines()

t3 = round(time.time() * 1000)
for line in lines:
    t5 = round(time.time() * 1000)
    res = generator(line, max_length=200, num_return_sequences=1)
    #res = generator_adapted(line, max_length=200, num_return_sequences=1)
    print(res)
    t6 = round(time.time() * 1000)
    print(f"Tiempo en resolver un problema: {t6-t5}")
t4 = round(time.time() * 1000)
print(f"Tiempo en resolver todos los problemas: {t4-t3}")
