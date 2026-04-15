# implement a basic rule-based chatbot

print("Madmax: Hello!! Type 'bye' to exit the chat")

while True:
    user = input("You: ").lower()

    if user == "hii maddy":
        print("Madmax: Hii")
    elif user == "how are maddy?":
        print("Madmax: I'm good!!")
    elif user == "what is today's whether":
        print("Madmax: Its quite good")
    elif user == "bye":
        print("Madmax: BYEEE")
        break
    else:
        print("Madmax: Sorry I don't understand")