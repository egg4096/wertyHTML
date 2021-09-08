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
            split = line.partition("[")
            try:
                spaces = split[0].partition(split[0].strip()[0])[0]
                text = split[0].strip()
                textCut = text.partition(" ")[0]
                add(f"{spaces}<{text}>{split[2][:-2]}</{textCut}>\n")
            except:
                pass
        else:
            level -= 1
            try:
                spaces = tags[level].split(tags[level].strip()[0])[0]
                textCut = tags[level].strip().partition(" ")[0]
                add(f"{spaces}</{textCut}>\n")
                tags.pop(level)
            except Exception:
                pass
    elif line_stripped.endswith("[") and line_stripped != "[":
        level += 1
        bit = line.partition("[")[0]
        try:
            spaces = bit.partition(bit.strip()[0])[0]
        except Exception:
            pass
        tags.append(bit)
        add(f"{spaces}<{bit.strip()}>\n")
    elif lines[lines.index(line) + 1 if lines.index(line) + 1 < len(lines) else len(lines) - 1].strip() == "[":
        level += 1
        tags.append(line_stripped)
        add(f"<{line_stripped}>\n")
    elif line_stripped != "[" and not line_stripped.startswith("#"):
        add(line)

output_file.write("</html>\n");

input_file.close()
output_file.close()
