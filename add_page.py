template = """# TITLE

[EN]({path}.md) | [UA]({path}_ua.md) | [RU]({path}_ru.md)"""


def create_page_files(path):
    for suffix in [".md", "_ua.md", "_ru.md"]:
        filename = "{path}{suffix}".format(path=path, suffix=suffix)
        with open(filename, "w") as f:
            f.write(template.format(path=path))


if __name__ == "__main__":
    path = input("Enter basic path to new file:")
    create_page_files(path)
