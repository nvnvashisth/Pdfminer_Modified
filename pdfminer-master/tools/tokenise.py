import re
import string
frequency = {}
document_text = open(r'C:\Users\vnitin\OneDrive - NetApp Inc\IDP\studysmarter-ml\Test_Code\filteredtext.txt', 'r',encoding="utf8")
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{4,15}\b', text_string)
#print(text_string)
#print(match_pattern)

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print(words, frequency[words])