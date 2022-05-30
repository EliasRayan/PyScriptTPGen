import json
import pandas as pd
from pandas import json_normalize

def preprocessing(s):
    s = s.replace('\n', '<br>').replace('\t', '&emsp;')
    return s

def sep_env(s):
    s = s.replace(' ', '')
    env = s.split(",")
    return env

def set_env(env):
    res = ""
    for e in env:
        res = res + f"- {e}\n"
    return res


filename = input("Nom du fichier HTML à générer (avec extension) : ")
q_input = input("JSON des questions : ")
with open(q_input, 'r') as f:
    raw = json.load(f)
questions = pd.DataFrame(raw['questions'])
d_input = input("JSON des détails : ")
with open(d_input, 'r') as g:
    det_raw = json.load(g)
details = pd.DataFrame(det_raw)

def init_content():
    x = ""
    for i in range(len(questions)):
        tips_n = i
        answer_n = i
        num1 = preprocessing(questions['num'][i])
        question1 = preprocessing(questions['question'][i][0])
        tips1 = preprocessing(questions['tips'][i][0])
        answer1 = preprocessing(questions['answer'][i][0])
        x = x + f"<p class=\"repl_question_p\"><b>Question {num1}</b>:<br> {question1}</p>\n<div>\n<py-repl auto-generate=\"false\"></py-repl>\n</div>\n<button class=\"btn btn-info\" onclick=\"show_hidden_p('tips{tips_n}')\"> Show tips </button>\n<p class=\"repl_tips_p\" id=\"tips{tips_n}\" hidden>{tips1}</p>\n<button class=\"btn btn-info\" onclick=\"show_hidden_p('answer{answer_n}')\"> Show answer</button><br>\n<p class=\"repl_answer_p\" id=\"answer{answer_n}\" hidden>{answer1}</p>\n<br>"
    return x

nl = '\n'
nt = '\t'
acc1 ='{'
acc2 = '}'
env = set_env(sep_env(details['env'][0]))
page_title = details['page_title'][0]
doc_title = details['doc_title'][0]
credits = details['credits'][0]
doc_description = details['doc_description'][0]
content = init_content()
#Long html page converted to a correct f-string
html = f"<!DOCTYPE html>{nl}<html lang=\"fr\">{nl}<head>{nl}<title>{page_title}</title>{nl}<meta charset=\"UTF-8\" />{nl}<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css\"/>{nl}<style>{nl}#hidden{acc1}visibility: hidden;{acc2}{nl}.repl_tips_p{acc1}background-color: rgba(173, 216, 230, 0.3);{acc2}{nl}.repl_answer_p{acc1}background-color: rgba(171, 246, 58, 0.3);{acc2}{nl}</style>{nl}<link rel=\"stylesheet\" href=\"https://pyscript.net/alpha/pyscript.css\" />{nl}<script defer src=\"https://pyscript.net/alpha/pyscript.js\"></script>{nl}<script>{nl}{nt}function show_hidden_p(id){acc1}{nl}{nt}{nt}let p = document.getElementById(id);{nl}{nt}{nt}p.removeAttribute(\"hidden\");{nl}{acc2}{nl}</script>{nl}</head>{nl}<body style=\"font-size: 20px; background: black;\">{nl}<!-- ENV here-->{nl}<py-env>{nl}{env}{nl}</py-env>{nl}<div class=\"jumbotron\" id=\"repl_question_div\">{nl}<div class=\"container\">{nl}<h1 id=\"doc_title\">{doc_title}</h1><br>{nl}<h3 id=\"credits\" style=\"color:blue\">{credits}</h3><br>{nl}<h2 id=\"doc_description\">{doc_description}</h2><br>{nl}<!-- REPL here-->{nl}{content}</div>{nl}</div>{nl}</body>{nl}</html>{nl}"
with open(filename, 'x') as f:
    f.write(html)
