from sys import argv
script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print("where do you live?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""Alright, so you said {likes} about liking me.
you live in {lives}. not sure where that is. And you have a {computer}
 computer. Nice.""")
