md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
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
    #print(result)
    return result
    
if __name__ == "__main__":
    main()
    