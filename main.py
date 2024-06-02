import sys
import os

# Define the path to store responses
file_path = "./helpers/response.txt"

def main():
    round_no = int(sys.argv[1])
    prev_opponent_response = sys.argv[2]
    
    # Ensure the helper directory exists
    if not os.path.exists('./helpers'):
        os.makedirs('./helpers')
    
    # Check if the file exists, if not, create it
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write("NONE\nYES\n")  # Initial responses: None for opponent, Yes for self

    # Read the file to get the last opponent's and our responses
    with open(file_path, 'r') as f:
        lines = f.readlines()
        past_opponent_response = lines[0].strip()
        my_last_response = lines[1].strip()
    
    # Decide the current response based on the opponent's last response
    if round_no == 1 or prev_opponent_response == "NONE":
        my_response = "YES"
    else:
        my_response = prev_opponent_response

    # Write the current round's responses to the file
    with open(file_path, 'w') as f:
        f.write(f"{prev_opponent_response}\n{my_response}\n")
    
    # Output the current response
    print(my_response)

if __name__ == "__main__":
    main()
