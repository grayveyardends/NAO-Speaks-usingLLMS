  # STOPPED NAO IS SADLY UNOPERATIONAL I COULDN'T TRY THE THINKS MENTION JUST KEEPING THIS FOR FUTURE
  
  # NAO-Speaks-usingLLMS
This is a simple  program to add NLP and LLM through ( optional Deepseek-8b and locally run RAGS )  currently using ollama for simplicity (recommended llama.cpp for CPU Offloading.

##  Project Overview
Welcome to **Interactive NAO **— This enables the **NAO robot** to replicate human interactions to a degree **speech recognition and LLMS**.

This project integrates:
-  **Speech Recognition** using `speech_recognition`.
-  **Natural Language Processing** via `DeepSeek-R1-Distill-llama-8B`. this is optional you can also use any model i tried it with a 1.5b model with not so good result.
-  **Choreographed Movements** controlled through dynamic commands.
- **Ollama Backend** for lightweight execution. (It's easier for this purpose than say llama.cpp but  i will recomment looking into something else for CPU ofloading)

![NAO Robot in Action](image1.png)
 
---

##  Installation Guide (using CLI)

###  Install Dependencies
```sh
pip install speechrecognition  pyaudio ollama torch naoqi  
```

###  Pull the AI Model (DeepSeek or Custom)
```sh
ollama pull your-model-name
```


##  How It Works
 The system listens for a **voice command** (or text input).  
 If it’s a **motion command** (e.g., `dance`, `sit`), NAO executes it.  
 Otherwise, the system **responds using **.  
 Recognized text is processed by **DeepSeek AI** via `ollama.chat()`.  
