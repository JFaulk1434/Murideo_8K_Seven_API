from map_key import murideo


def update_numeric_keys(d):
    updated_dict = {}
    for key, value in d.items():
        if isinstance(value, dict):
            value = update_numeric_keys(value)

        new_key = key - 1 if isinstance(key, int) else key
        updated_dict[new_key] = value

    return updated_dict


def generate_markdown(d, indent=0):
    markdown_str = ""
    first_item = True
    for key, value in d.items():
        if isinstance(value, dict):
            if "id" not in value and "tag" in value:
                markdown_str += "#" * indent + f" {value['tag']}\n\n"
                markdown_str += generate_markdown(value, indent=indent + 1)
            elif "id" in value and "tag" in value:
                if first_item:
                    markdown_str += (
                        "| Name                | ID  |\n| ------------------ | --- |\n"
                    )
                    first_item = False
                markdown_str += f"| {value['tag']} | {value['id']} |\n"
    markdown_str += "\n"
    return markdown_str


# Generate markdown string
markdown_str = "# Dictionary Markdown\n\n"
markdown_str += generate_markdown(murideo, indent=2)

# Write to a markdown file
with open("dictionary_markdown.md", "w") as f:
    f.write(markdown_str)
