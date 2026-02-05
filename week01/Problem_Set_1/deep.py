def main():
    user_answer = str(input("Great Question of Life, the Universe and Everything. Your answer --> "))
    match user_answer:
        case "42" | "forty-two" | "forty two" :
            print("Yes")
        case _:
            print("No")

main()