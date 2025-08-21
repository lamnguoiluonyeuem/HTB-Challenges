import re

tag_hex = {
    "cite": "0",
    "h1": "1",
    "p": "2",
    "a": "3",
    "img": "4",
    "ul": "5",
    "ol": "6",
    "button": "7",
    "div": "8",
    "span": "9",
    "label": "a",
    "textarea": "b",
    "nav": "c",
    "b": "d",
    "i": "e",
    "blockquote": "f",
}

def hex_string_to_bytes(hex_str: str) -> str:
    if len(hex_str) % 2 != 0:
        hex_str = hex_str[:-1]
    num_array = bytes(int(hex_str[i:i+2], 16) for i in range(0, len(hex_str), 2))
    return num_array.decode("ascii", errors="ignore")

def decode_data(data: str) -> str:
    body_match = re.search(r"<body>(.*?)</body>", data, re.DOTALL | re.IGNORECASE)
    if not body_match:
        return ""

    body_content = body_match.group(1)
    matches = re.findall(r"<(\w+)[\s>]", body_content)

    hex_builder = []
    for tag in matches:
        t = tag.lower()
        if t != "li" and t in tag_hex:
            hex_builder.append(tag_hex[t])

    hex_str = "".join(hex_builder)
    return hex_string_to_bytes(hex_str)


if __name__ == "__main__":
    with open(r"C:\Users\nguye\Downloads\HTB\Fishy HTTP\4.html", "r", encoding="utf-8") as f:
        html = f.read()

    result = decode_data(html)
    print("Decoded:", result)
