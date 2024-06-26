#fill in the blanks
import sys
import json
import os

fn = sys.argv[1]
base_path = os.getcwd()
relative_path = f"kodigo\\game\\python\\temp\\{fn}.json"
fp = os.path.join(base_path, relative_path)#r"D:\renpy-8.1.3-sdk\Kodigo\game\python\docs\Quiz 1.json"#

#read the json file
with open(fp, 'r') as file:
    quiz = json.load(file)

answers = quiz["answers"]
sentences = quiz["sentences"].copy()
with_comma = False

for i in range(len(sentences)):
    if len(answers[i].split(' ')) == 1: 
        sentence = sentences[i].split(' ')
        sentence[-1] = sentence[-1][:-1] #remove the perior from the last word of the sentence
        blank_space = len(answers[i]) * '_'
        item = []
        found = False
        for word in sentence:
            if word.endswith(','):
                print(word)
                word = word[:-1] 
                with_comma = True
            if answers[i] == word.lower() and not found:
                if with_comma:
                    blank_space += ","
                    with_comma = False
                item.append(blank_space)
                found = True
            else:
                if with_comma:
                    word += ","
                    with_comma = False
                item.append(word)
        sentences[i] = ' '.join(item) + '.'
    else:
        answer = answers[i].split(' ')
        
        for w in answer:
            sentence = sentences[i].split(' ')
            sentence[-1] = sentence[-1][:-1] #remove the perior from the last word of the sentence
            blank_space = len(w) * '_'
            item = []
            found = False
            for word in sentence:
                if word.endswith(','):
                    word = word[:-1] 
                    with_comma = True
                if w == word.lower() and not found:
                    if with_comma and w == answer[-1]:
                        blank_space += ","
                        with_comma = False
                    item.append(blank_space)
                    found = True
                else:
                    if with_comma:
                        word += ","
                        with_comma = False
                    item.append(word)
            sentences[i] = ' '.join(item) + '.'

quiz["questions"] = sentences
for i in range(len(sentences)):
    print(f"{sentences[i]}: {answers[i]}")

#save the updated data back to json
with open(fp, 'w') as file:
    json.dump(quiz, file)
    
print("done")
#next task
#in order to have better keywords, store the ranked sentences back to the json 
#okay if we're doing a counted _ we need to edit distractors to have the same word length as the answer
#but for now let's just have a default five length for mcqs and for identification then it's the length of the word
