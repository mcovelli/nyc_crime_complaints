import ollama

prompt = "You are a data analyst for a portfolio project. " \
"Here are the key findings from analyzing 9.4 million NYC crime complaints from 2006 - 2024: " \
"Highest number of complaints in Brooklyn, lowest in State Island. " \
"Most crimes are REPORTED between noon and midnight. " \
"Kidnapping has the highest reporting delay. " \
"Top offenses where the suspect is male and the victim is female are Harrassment 2, Assault 3 & related offenses and Offenses Against Public Order and Sensibility." \
"Crimes against woman are highest regardless of suspect gender. " \
"More crimes with a male suspect are more than double than female suspects. " \
"The highest number of crimes are of suspects between 24-44 years old, regardless of gender. " \
"The lowest crime rate are offenses with a suspect 65+ years old." \
"Petit Larceny is most common reported offense across all boroughs, with highest occurrence in Manhattan" \
"Harrassment 2 is the second highest, most common in Brooklyn" \
"Murder rates are consistently highest in Brooklyn, peaking in 2010" \
"Murder rates spiked between 2020 and 2021 in Brooklyn and the Bronx" \
"Murder rates have been declining since 2021 across all boroughs" \
"An overwhelming amount of crime complaints involve a black suspect and a black victim" \
"Most crime complaints the victim and suspect are of the same race." \
"Approximately 40 - 49 percent of suspect information such as age, sex and race is missing which indicates the suspect wasn't found or no arrests had been made.  " \
"Write a professional 3 paragraph narrative summary suitable for a non-technical audience. Included a bulleted summary of all findings at the end."

response = ollama.chat (
    model = 'llama3.2',
    messages = [
        {'role': 'user', 'content': prompt}
    ]
)

with open('/Users/mike/nyc-crime-ai/narrative.md', 'w') as f:
    f.write(response['message']['content'])

print(response['message']['content'])