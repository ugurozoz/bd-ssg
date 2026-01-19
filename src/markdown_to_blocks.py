md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here


# This is h1 header

## This is h2 header

### This is h3 header 

# Heading level 1

This is a simple paragraph with some text in it.
It has no special prefix and should be parsed as a paragraph.

## Heading level 2

This is a second paragraph, separated by a blank line.
It exists to ensure multiple <p> elements are generated.

### Heading level 3

> This is a quote line
> that continues on the next line.
> And even a third line to ensure grouping works.

#### Heading level 4

- First bullet
- Second bullet with some _inline_ formatting
- Third bullet with **bold** text

##### Heading level 5

1. First item
2. Second item with **bold** text
3. Third item with _italic_ text

###### Heading level 6

####### (this line is just normal text, not a heading)

```
This is text that should remain
the same even with inline stuff
and code markers
```

"""




def main():
    markdown_to_blocks(md)


def markdown_to_blocks(markdown):
    result = []
    splitted = markdown.split('\n\n')
    
    for split in splitted:
        #print('SPLIT',split)
        stripped = split.strip()
        #print('SPLITTED', stripped)
        if stripped != '':
            result.append(stripped)
    
    return result

def extract_code_text(block):
    block_lines = block.split('\n')
    block_lines.pop(0)
    block_lines.pop(-1)
    block_joined ='\n'.join(block_lines)
    return block_joined
    # split, drop first/last, join with "\n"
    
if __name__ == "__main__":
    main()
    