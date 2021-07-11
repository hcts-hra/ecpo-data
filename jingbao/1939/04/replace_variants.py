import json, os

def replace_variants(file_content, dict):
    for char,printed_variant in dict.items():
        file_content = file_content.replace(char,printed_variant)
    return file_content

if __name__ == "__main__":

    with open("variants.json") as f:
        variants = json.load(f)

    for file in os.listdir():
        if file.endswith(".xml"):
            with open(file, "r") as f:
                file_content = f.read()
            with open(file, "w") as f:
                f.write(replace_variants(file_content, variants))
