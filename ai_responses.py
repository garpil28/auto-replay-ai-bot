import random

responses = [
    "Hmm, menarik banget nih 😄",
    "Aku lagi mikir... kayaknya jawabannya kompleks!",
    "Bisa jelasin lebih detail gak?",
    "Aku rasa itu hal yang keren banget 😎",
    "Haha iya juga ya 😂",
    "Sepertinya kamu pintar juga!",
    "Aku setuju sama kamu.",
    "Itu pertanyaan bagus banget, aku suka!",
    "Wah, aku jadi penasaran nih...",
    "Hehehe, kamu lucu deh 😁",
]

def get_random_response():
    return random.choice(responses)
