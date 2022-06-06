from transformers import pipeline, set_seed
import json

generator = pipeline('text-generation', model='microsoft/CodeGPT-small-py', device=0)
generator_adapted = pipeline('text-generation', model='microsoft/CodeGPT-small-py-adaptedGPT2', device=0)

set_seed(42)
text = "def sum_tree(root): '''Given the root of a tree, return the sum of all its nodes'''"

response = generator(text, max_length=200, num_return_sequences=1)
responses_a = generator_adapted(text, max_length=200, num_return_sequences=10)

print(response)
for response_a in responses_a:
    print(response_a)