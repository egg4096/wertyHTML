input_file = open("input.txt", mode="r", encoding="utf-8")
output_file = open("output.html", mode="w", encoding="utf-8")

level = 0
lines = input_file.readlines()
tags = []

output_file.write("<!doctype html>\n\n<html>\n")

def add(text):
    output_file.write(f"\t{text}")

for line in lines:
    line_stripped = line.strip()

    if line_stripped.endswith("]"):
        if "[" in line:
            partition = line.partition("[")

            try:
                text = partition[0].strip()
                spaces = partition[0].partition(text[0])[0]
                text_cut = text.partition(" ")[0]
                add(f"{spaces}<{text}>{partition[2][:-2]}</{text_cut}>\n")
            except Exception:
                pass
        else:
            level -= 1

            try:
                spaces = tags[level].partition(tags[level].strip()[0])[0]
                text_cut = tags[level].strip().partition(" ")[0]
                add(f"{spaces}</{text_cut}>\n")
                tags.pop(level)
            except Exception:
                pass
    elif line_stripped.endswith("[") and line_stripped != "[":
        bit = line.partition("[")[0]
        bit_stripped = bit.strip()

        try:
            spaces = bit.partition(bit_stripped[0])[0]
        except Exception:
            pass

        if bit_stripped[0] == "]":
            bit = bit_stripped[1:]
            add(f"{spaces}</{bit.strip()}>\n")
            tags.pop(level - 1)
        else:
            level += 1

        bit_stripped = bit.strip()
        tags.append(f"{spaces}{bit_stripped}")
        add(f"{spaces}<{bit_stripped}>\n")
    elif lines[lines.index(line) + 1 if lines.index(line) + 1 < len(lines) else len(lines) - 1].strip() == "[":
        level += 1
        tags.append(f"{spaces}{line_stripped}")
        add(f"<{line_stripped}>\n")
    elif line_stripped != "[" and not line_stripped.startswith("#"):
        add(line)

output_file.write("</html>\n");

input_file.close()
output_file.close()
