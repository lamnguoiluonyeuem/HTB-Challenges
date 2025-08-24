import re
import base64

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

def extract_initials_from_file(file_path: str) -> str:
    initials = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        words = content.split()
        for w in words:
            if w[0].isalpha():
                initials.append(w[0])
            else:
                initials.append(w[0])

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return "".join(initials)

def decode_base64(data: str) -> str:
    """Giải mã base64 thành text"""
    try:
        decoded_bytes = base64.b64decode(data)
        return decoded_bytes.decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"Base64 decode error: {e}")
        return ""

if __name__ == "__main__":
    html_path = r"C:\Users\nguye\Downloads\HTB\Fishy HTTP\3.html"
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()
    decoded = decode_data(html)
    print(decoded)
    txt_path = r"C:\Users\nguye\Downloads\HTB\Fishy HTTP\Yo.txt"
    initials = extract_initials_from_file(txt_path)
    print("Initials decoded (base64):", decode_base64(initials))

