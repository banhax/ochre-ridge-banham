import ollama

MODEL = "llama3.1:8b"
PROMPT = "Say hello."

print("test run XD")
print(ollama.generate(model=MODEL, prompt="Do nothing, xD lolcat xD", stream=False))
print("")

print("Hot Start")
print(ollama.generate(model=MODEL, prompt=PROMPT, stream=False, keep_alive=False))
print("")

print("Cold Start")
print(ollama.generate(model=MODEL, prompt=PROMPT, stream=False))
print("")
