from llama_cpp import Llama
import os

# Initialize the Llama model
llm = Llama(model_path="../../model/Llama-2-70B-Orca-200k/model/llama-2-70b-orca-200k.Q3_K_S.gguf", n_gpu_layers=80, n_gqa=8, verbose=False, n_ctx=2048, reverse_prompt="User:")

# Directory to save appointment files
appointment_dir = "./appointments"

# Check if the appointment directory exists, and create it if not
if not os.path.exists(appointment_dir):
    os.makedirs(appointment_dir)

# Read the initial context from a file
initial_context_file = "receptionist.txt"
with open(initial_context_file, 'r') as file:
    initial_context = file.read()

# Initialize conversation history with the initial context
conversation_history = initial_context
while True:
    # Generate a response from the model based on the conversation history
    response = None
    while not response:  # Keep querying until a non-empty response is generated
        # Generate a response from the model based on the conversation history
        response = llm(conversation_history, max_tokens=250)["choices"][0]["text"]
      # Find the first occurrence of "User:"
    user_index = response.find("User:")

    # If "User:" is found, update response to include text up to but not including it
    if user_index != -1:
        response = response[:user_index]
    
    if "JSON COMPLETE" in response:
        # Replace "JSON COMPLETE" with the closing message
        response = "Thank you for using Salon Chat, we'll see you soon!"

        print(response)

        conversation_history += "Create the JSON and only the JSON for the appointment: \n "

        json_response = llm(conversation_history, max_tokens=250)["choices"][0]["text"]

        file_path = os.path.join(appointment_dir, f"appointment.txt")
        with open(file_path, 'w') as txt_file:
            txt_file.write(json_response)

        #Exit program
        break


    response_stripped = response.lstrip("\n").strip()
    # Check if the response starts with "Fine Hair Salon:"
    if response_stripped.startswith("Fine Hair Salon:"):
        # If it does, just print the response
        print(response)
        conversation_history += response
    else:
        # If it doesn't, prepend "Fine Hair Salon:" and then print it
        response_with_prefix = "Fine Hair Salon: " + response
        print(response_with_prefix)
        # Save it to conversation_history with the prefix
        conversation_history += response_with_prefix


   # Prompt the user for input
    user_input = input("User: ")

    # Append the user input to the conversation history
    conversation_history += "User: " + user_input + "\nFine Hair Salon: "

