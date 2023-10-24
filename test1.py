#!/usr/bin/env python3

# load the large language model file
from llama_cpp import Llama
LLM = Llama(model_path="../../model/Llama-2-70B-Orca-200k/model/llama-2-70b-orca-200k.Q3_K_S.gguf", ngl=80)

# create a text prompt
prompt = "Q: What are the names of the days of the week? Respond politely A:"

# generate a response (takes several seconds)
output = LLM(prompt)

# display the response
print(output["choices"][0]["text"])
