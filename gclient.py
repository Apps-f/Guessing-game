import socket
import json

host = "localhost" 
port = 1111
name = input("Enter your name: ")

s = socket.socket()
s.connect((host, port))

data = s.recv(1024)
print(data.decode().strip())

while True:
    difficulty = int(input("Enter difficulty (1-3): "))
    s.sendall(json.dumps({"difficulty": difficulty}).encode())

    data = json.loads(s.recv(1024).decode())
    
    
    if "guessme" in data:
        guessme = data["guessme"]
        score = 0
        
        while True:
            guess = int(input("Enter guess: "))
            s.sendall(json.dumps({"guess": guess, "name": name, "score": score, "difficulty": difficulty}).encode())
            reply = json.loads(s.recv(1024).decode())
            
            if reply["status"] == "win":
                print(reply["message"])
                break
            elif reply["status"] == "incorrect":
                print(reply["message"])

            score += 1
    else:
        print("Error: Invalid response from server. Please try again.")
        continue

    if not input("Play again? (y/n): ").lower().startswith('y'):
        break

s.close()
