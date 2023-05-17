contents = ["Ignorance is a bliss!", "BeLIEve kNOw MORE", "What is the purpose of your life?"]

filenames = ["Exclamation.txt", "Affirmative.txt", "Question.txt"]

file_path = "../files/"

for content, filename in zip(contents, filenames):
    with open(f"{file_path}{filename}", 'w') as f:
        f.write(content)
