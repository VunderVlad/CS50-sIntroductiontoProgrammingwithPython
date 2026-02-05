def main():
    file_type = str(input("Write full file name here --> "))

    if file_type.__contains__(".gif"):
        print("image/gif")
    elif file_type.__contains__(".jpg") and file_type.__contains__(".jpeg") :
        print("image/jpeg")
    elif file_type.__contains__(".png"):
        print("image/png")
    elif file_type.__contains__(".pdf"):
        print("application/pdf")
    elif file_type.__contains__(".txt"):
        print("text/plain")
    elif file_type.__contains__(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")
        return


main()