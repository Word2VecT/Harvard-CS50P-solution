def main():
    word = input("Input: ")
    print(shorten(word), end="")


def shorten(word):
    return ''.join(
        (
            alpha
            for alpha in word
            if alpha not in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        )
    )


if __name__ == "__main__":
    main()