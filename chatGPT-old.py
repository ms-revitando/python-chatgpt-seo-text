import openai

openai.api_key = "OPEN_AI_KEY"

name = "Max Mustermann GmbH"
adress = "Musterstraße 123, 12345 Musterstadt"
phone = "+49 176 1234567"
email = "max.muster@muster.de"
website = "www.muster.de"
socialmedia = "www.instagram.com/maxmuster"
opening_hours = "Montag bis Freitag, 08:00 Uhr bis 17:00 Uhr"
seo_categories = "Gesundheit, Gesellschaft, Soziales"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "system", "content": "Du bist ein SEO Profi und schreibst unique SEO-Texte auf deutsch. Schreibe einen einzigartigen suchmaschinenoptimierten Unternehmenstext für eine Webseite über folgendes Unternehmen, ohne direkte Ansprache des Lesers. Bitte verwede mindestens 500 Zeichen. Verzichte auf die Begrüßung. Keine Plagiate. Verwende als keywords zur Optimierung die angegebenen Daten.\n"
                                          "Firma: " + name + "\n"
                                          "Branche: " + seo_categories + "\n"
                                          "Adresse: " + adress + "\n"
                                          "Telefonnummer: " + phone + "\n"
                                          "E-Mail-Adresse: " + email + "\n"
                                          "Internetseite: " + website + "\n"
                                          "Links zu sozialen Medien: " + socialmedia + "\n"
                                          "Öffnungszeiten: " + opening_hours + "\n"
             },
]
)
text_to_save = completion['choices'][0]['message']['content']

with open('seo_text.txt', 'w', encoding='utf-8') as file:
    file.write(text_to_save)
