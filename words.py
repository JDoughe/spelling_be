from english_words import get_english_words_set

def print_words():
    print(f'The other words are')
    for word in final_aw:
        print(word)

all_words = list(get_english_words_set(['web2']))

#Set primary equal to required letter. There is always only 1.
primary = 'o'
#Set the below equal to the non-primary letters. There should always be 7.
all_spelling_bee = ['a','l','f','o','e','p','g']
all_spelling_bee.append(primary)


letters = ['a','b','c',
           'd','e','f',
           'g','h','i',
           'j','k','l',
           'n','m','o',
           'p','q','r',
           's','t','u',
           'v','w','x',
           'y','z','.','1','2','3','-','0']

for num in list(range(len(all_spelling_bee))):
    letters = [letter for letter in letters if all_spelling_bee[num] not in letter]
for item in letters:
    all_words = [word for word in all_words if item.lower() not in str(word).lower() and len(str(word))>3]
for word in all_words:
    aw = [word for word in all_words if False == word.isupper()]

final_aw = [word for word in aw if primary in word.lower()]
panny_word = [word for word in all_words if primary in str(word)]
pg = panny_word
for letter in all_spelling_bee:
    pg = [word for word in pg if str(letter) in str(word)]

counter = len(pg)
if len(pg) == 1:
    print(f'The panogram is {pg[0]}')
    print_words()
elif len(pg) > 1:
    print(f'The panograms are {pg}')
    print_words()
elif len(pg) == 0:
    print_words()
