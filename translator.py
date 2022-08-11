def menu():
    global choice
    print("1. Add")
    print("2. English to Persian")
    print("3. Persian to English")
    print("0. Exit")
    choice = input("Menu: ")

def add():
    english_word = input("English: ")
    persian_word = input("Persian: ")
    if find(english_word) != -1 or find(persian_word) != -1: print('Word already exist')
    else:
        new_dict = {'english': english_word, 'persian': persian_word}
        words.append(new_dict)
        print('SUCCEED')

def translate(output_language):
    input_sentences = input().split('.')
    output_sentences = []
    for j in range(len(input_sentences)):
        input_words = input_sentences[j].split(' ')
        output_words = []
        for k in range(len(input_words)):
            i = find(input_words[k])
            if i != -1: output_words.append(words[i][output_language])
            else: output_words.append(input_words[k])
        output_sentences.append(output_words)
    output(output_sentences)

def save_and_exit():
    try:
        new_file = open('database.txt', 'w')
        new_text = ''
        for i in range(len(words)):
            new_text += words[i]['english'] + ','
            new_text += str(words[i]['persian'])
            if i < len(words)-1: new_text += '\n'
        new_file.write(new_text)
    except Exception as e:
        print(str(e))
    exit()

def output(sentences):
    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            print(sentences[i][j], end=' ')
        print('')

def find(key):
    found = False
    for i in range(len(words)):
        if key in [words[i]['english'], words[i]['persian']]:
            found = True
            break
    if found: return i
    else: return -1

try:
    myfile = open('database.txt', 'r')
    database = myfile.read()
    rows = database.split('\n')
    words = []
    for i in range(len(rows)):
        row = rows[i].split(',')
        mydict = {'english': row[0], 'persian': row[1]}
        words.append(mydict)
except Exception as e:
    print(str(e))
    exit()

choice = 0
while True:
    menu()
    if choice == '1': add()
    if choice == '2': translate('persian')
    if choice == '3': translate('english')
    if choice == '0': save_and_exit()
