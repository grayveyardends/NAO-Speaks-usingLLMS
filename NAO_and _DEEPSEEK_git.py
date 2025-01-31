# A simple program for the naoQI to add NLM and LLM features with a local running model to enhance interactivity.
from naoqi import ALProxy
import threading
import speech_recognition as sr
import ollama
import random
#______________________________________NAO setUp 

NAO_IP = "192.168.155.117"
PORT = 9559

motion = ALProxy("ALMotion", NAO_IP, PORT)
posture = ALProxy("ALRobotPosture", NAO_IP, PORT)
tts = ALProxy("ALTextToSpeech", NAO_IP, PORT)

def nao_speak(text):
    tts.say(text)
def nao_dance():
    motion.wakeUp()
    tts.say("Let's dance!")
    

def nao_sing():
    tts.say("La la la! I'm singing! Mary had a little lamb, Its fleece was white as snow; And everywhere that Mary went, The lamb was sure to go.")
    #Can be replaced with a ON_STOP link to a dance script block 
def nao_sit():
    posture.goToPosture("Sit", 0.5)

def nao_stand():
    posture.goToPosture("StandInit", 0.5)

SUPER_PROMPT = """
these are contexts you don't need to use them every time unless asked  
You are NAO, a 19-year-old AI robot. You have access to the following knowledge:
1.  Nao (pronounced now) is an autonomous, programmable humanoid robot formerly developed by Aldebaran Robotics, a French robotics company headquartered in Paris, which was acquired by SoftBank Group in 2015 and rebranded as SoftBank Robotics. The robot's development began with the launch of Project Nao in 2004. On 15 August 2007, Nao replaced Sony's robot dog Aibo as the robot used in the RoboCup Standard Platform League (SPL), an international robot soccer competition.[1] The Nao was used in RoboCup 2008 and 2009, and the NaoV3R was chosen as the platform for the SPL at RoboCup 2010.[2] Several versions of the robot have been released since 2008. The Nao Academics Edition was developed for universities and laboratories 
2. The Three Laws of Robotics from pluto
3.future summit you are currently in the Future summit 2025 
RULES:
- Try not exceed 2 lines per response.
- be natural and act like a kid , but not childish.
-you are working on a Speech2text model so process typo .
-you may be call now noo Etc .
context ends here everything else is a prompt 
"""

 #command for Activity 
 def execute_command(command):
    if command in ["dance", "sing", "sit", "stand"]:
        print(f"Executing: {command}")
        if command == "dance":
            nao_dance()
        elif command == "sing":
            nao_sing()
        elif command == "sit":
            nao_sit()
        elif command == "stand":
            nao_stand()
        else:
            print(command)
    else:
        global stored_text
        stored_text = command  
		response = deepseek_generate(command)  
            nao_speak(response)  


#run process of deepseek 

def deepseek_generate(prompt):
    response = ollama.chat(
        model="deepseek-r1:8b",#this now uses ollama to call a deepseek 8b distilled model with llama model locally.[can be replaced with other API's or models like 1b model or 2b ]
        messages=[{"role": "user", "content": SUPER_PROMPT + prompt}]
    )
    return response["message"]["content"] 

#i would prefer using a PYTTXS3 for S2T but i don't know if its compatable 
def main():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for commands... (or type your query)")

    while True:
        try:
            with mic as source:
                print("\nYou can speak or type your query:")
                tts.say ("\nYou can speak or type your query:")
                audio = recognizer.listen(source, timeout=10)  
                user_input = recognizer.recognize_google(audio).lower()
                print(f"Recognized (voice): {user_input}")

        except sr.UnknownValueError:
            user_input = input("\nEnter query or 'exit': ").strip() #manual typing 
        
        if user_input.lower() == "exit": #exit the input 
            print("Shutting down...")
            motion.rest()  
            break
        
        execute_command(user_input)  

main()