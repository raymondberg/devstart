# This script contains in it the instructions for a game and the game logic itself.
# Try to figure out how it works, then see if you can improve it!
chapters = []
chapters.append({
    0: {
        "text": "You wake up in a room, laying on a hard wooden floor.",
        "help": "Why are you still on the ground?",
        "commands" : [
            { "command": "stand up", "response": "You stand up.", "goto_step": 100},
            { "command": "look around", "response": "It's very dark. There's not much to see"},
            { "command": "go to sleep", "response": "NOW IS NO TIME TO SLEEP!"},
         ]
    },
    100: {
        "text": "You can see around the room now. There's a single lightbulb hanging from a string in the center of the room.",
        "commands": [
            { "command": "turn off the light", "response": "You turn the light off", "chapter_end": True }
        ]
    }
})

chapters.append({
    0: {
        "text": "You click the light back on and suddenly you realize you are on a frozen mountaintop. The light is swinging from a manmade arch over your head.",
        "help": "It's cold here; are you crazy! Lets get out of here!",
        "commands" : [
            { "command": "turn off the light", "response": "You turn the light off.", "chapter_end": True},
            { "command": "look around", "response": "You can see out to the ocean. It must be 70 miles of rough terrain."},
            { "command": "climb down", "response": "That was unwise. You do not survive the descent.", "chapter_end": True},
         ]
    }
})


for chapter in chapters:
    step = chapter[0]
    while True:
        print(step["text"])
        user_command = input(" > ");
        picked_command = None

        for command in step["commands"]:
            if command["command"] == user_command:
                picked_command = command
                break

        if picked_command is None:
            print("I'm not sure what you mean.")
        else:
            print(picked_command["response"])
            if "chapter_end" in picked_command: break
            if "goto_step" in picked_command: step = chapter[command["goto_step"]]
        print("")

print("The End.")



## Ideas to improve the game:
# More steps and chapters? Change the start of the story or continue it on!
# Add the ability to ask for help in EVERY step, which will list the available commands
# Add the ability to quit in every step
# Really hard: Is it possible to move the questions to another file? Check out YAML.
