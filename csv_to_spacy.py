import pandas
import spacy

def reset(all_cats):
    default_dict = {}
    for cat in all_cats:
        default_dict[cat] = False
    return default_dict
    
# Loads the English language "model"
nlp = spacy.load('en_core_web_sm') # <-- nlp program: language analysis

# Opens our spreadsheet
fh = open("classify.csv","r")
data = fh.read()

# Loading all possible categories for the 
# purposes of providing "negative"
all_cats = open("data/cats.list","r")
all_cats = [line.strip() for line in all_cats]

data = data.split("\n")
data = [d for d in data if d != ""]
db = spacy.tokens.DocBin()

# Defines all classifications ("classes") as
# negative examples

train_pct = int(.8 * len(data))

for row in data:
    cats_dict = reset(all_cats)
    fields = row.split(",")
    doc = nlp.make_doc(fields[0])
    cats_list = [field for field in fields[1:] if field != ""]
    # For every category associated with a term, turn negative
    # to positive examples
    for cat in cats_list:
        cats_dict[cat] = True
    doc.cats = cats_dict
    db.add(doc)

db.to_disk("train.spacy") # spaCy dataset (training/testing set)

db = spacy.tokens.DocBin()

# for row in data[train_pct:]:
#     cats_dict = reset(all_cats)
#     fields = row.split(",")
#     doc = nlp.make_doc(fields[0])
#     cats_list = [field for field in fields[1:] if field != ""]
#     # For every category associated with a term, turn negative
#     # to positive examples
#     for cat in cats_list:
#         cats_dict[cat] = True
#     doc.cats = cats_dict
#     db.add(doc)
    
# db.to_disk("eval.spacy")