def parser(input_string):
    words = input_string.split()
    first_word = words.pop(0)

    if first_word == "create_project":
        return parse_create_project(first_word, words)
    elif first_word == "project":
        pass 
    else:
        return (first_word, words[0:])

def parse_create_project(first_word, words):
    title = words.pop(0)
    max_grade = words.pop()
    description = ""
    for word in words:
        description += word + " "
    return (first_word, [title, description, max_grade])