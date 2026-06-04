class DarkButton:
    label = "dark-button"


class DarkCheckbox:
    label = "dark-checkbox"


class DarkFactory:
    def button(self):
        return DarkButton()

    def checkbox(self):
        return DarkCheckbox()


def main():
    factory = DarkFactory()
    button = factory.button()
    checkbox = factory.checkbox()
    print(button.label, checkbox.label)


if __name__ == "__main__":
    main()
