from pymonad.tools import curry


# 3.1.
@curry(2)
def tag(html_tag: str, value: str):
    return f'<{html_tag}>{value}</{html_tag}>'


bold = tag('b')
italic = tag('i')

bold = bold('value bold')
italic = italic('value italic')

print(bold)
print(italic)


# 3.2.
@curry(3)
def tag2(html_tag: str, attr: dict, name: str):
    params = ' '.join(f'{key}="{value}"' for key, value in attr.items())
    return f'<{html_tag} {params}>{name}</{html_tag}>'


final_string = tag2('li')({'class': 'list-group', 'div': 'mb-3'})('item 23')

print(final_string)


