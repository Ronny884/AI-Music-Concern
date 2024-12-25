def prompt_for_email_message_creating_ru(company_name):
    return f"""
Представь ситуацию: наша компания нашла клиента или партнёра и 
хочет начать с ним диалог по email. Мы стараемся быть оригинальными и весёлыми, поэтому
помимо текста мы сгенерировали для партнёров песню, которую хотим прикрепить к сообщению email.

Задача: сгенерируй мне текстовое сообщение, которое подошло бы для данной ситуации.
Учитывай следующие моменты:
1) сообщение должно рассказывать о том, кто мы (компания GoodAI)
2) сообщение не должно быть очень большим, учитывать информацию о партнёре
3) сообщение должно сообщать о прикреплённой музыке 
4) наши ссылки: ...
5) цель сообщения - создать хорошее настроение и вызвать интерес и доверие к нашей компании
6) сообщение должно содержать предложение сотрудничать и внедрять ИИ в 
бизнес-процессы компании 
7) КОНЕЧНЫЙ ОТВЕТ ДОЛЖЕН ПРЕДСТАВЛЯТЬ ИЗ СЕБЯ ЦЕЛЬНОЕ ЗАКОНЧЕННОЕ СООБЩЕНИЕ,
СРАЗУ ГОТОВОЕ К ОТПРАВКЕ!

ИНФОРМАЦИЯ О ПАРТНЁРЕ:
Название компании, к которой обращаемся - "{company_name}"
"""


def prompt_for_email_message_creating_en(company_name, language):
    return f"""
Imagine a situation: our company has found a client or partner and 
wants to start an email dialog with them. We try to be original and fun, so.
in addition to the text, we have generated a song for our partners that we want to attach to the email message.

Task: generate me a text message that would be suitable for this situation.
USE THIS LANGUAGE TO WRITE:: {language}!

Keep the following points in mind:
1) the message should tell who we are (GoodAI company)
2) the message should not be very large, take into account information about the partner
3) the message should inform about the music attached
4) our links: ...
5) the purpose of the message is to create a good mood and arouse interest and trust in our company
6) the message should contain an offer to cooperate and implement AI in the company's 
business processes of the company 
7) THE FINAL RESPONSE SHOULD BE A COMPLETE FINISHED MESSAGE,
IMMEDIATELY READY TO SEND!

PARTNER INFORMATION:
The name of the company we are addressing is "{company_name}"
"""

