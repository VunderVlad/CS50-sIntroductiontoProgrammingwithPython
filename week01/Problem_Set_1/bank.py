def main():
    greeting = str(input("Greeting: "))
    if "hello" in greeting.lower():
        print("$0")
    elif greeting.lower()[0] == "h":
        print("$20")
    else:
        print("$100")

main()