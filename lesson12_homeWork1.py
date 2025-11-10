import re

def clean_html(input_filename, output_filename="cleaned.txt"):
    with open(input_filename, "r", encoding="utf-8") as infile:
        text = infile.read()

    cleaned_text = re.sub(r"<.*?>", "", text)

    lines = [line.strip() for line in cleaned_text.splitlines() if line.strip()]

    with open(output_filename, "w", encoding="utf-8") as outfile:
        outfile.write("\n".join(lines))

