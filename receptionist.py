from llama_cpp import Llama

# Initialize the Llama model
llm = Llama(model_path="../../model/Llama-2-70B-Orca-200k/model/llama-2-70b-orca-200k.Q3_K_S.gguf", n_gpu_layers=80, n_gqa=8, verbose=False, n_ctx=2048, reverse_prompt="User:")

# Read the initial context from a file
initial_context_file = "receptionist.txt"
with open(initial_context_file, 'r') as file:
    initial_context = file.read()

# Initialize conversation history with the initial context
conversation_history = initial_context

while True:
    # Generate a response from the model based on the conversation history
    response = llm(conversation_history, max_tokens=0)["choices"][0]["text"]

    # Append the model's response to the conversation history and display it
    conversation_history += "Fine Hair Salon:" + response
    print("Fine Hair Salon:", response)

    # Get user input
    user_input = input("User: ")

    # Append the user input to the conversation history
    conversation_history += "\nUser: " + user_input

