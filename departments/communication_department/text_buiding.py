from jinja2 import Template


def build_text(
        heading,
        upper_text,
        video_link,
        lower_text=None,
        double_rending_data: dict = None
):
    footer_text = \
    """
The GoodAI Team
    """
    upper_text = upper_text.replace('\n', '')

    # Формирование текста с разделением на абзацы
    if lower_text is None:
        text = f"{heading}\n{upper_text}\n\n👉 {video_link}\n\n{footer_text}"
    else:
        text = f"{heading}\n{upper_text}\n\n👉 {video_link}\n{lower_text}\n\n{footer_text}"

    # Двойной рендеринг, если требуется
    if double_rending_data:
        template = Template(text)
        text = template.render(double_rending_data)

    return text














# t = build_text(
#     heading='Hello {{company_name}}!',
#     upper_text=\
#     """
# I am a fully autonomous AI agent made and executed by HappyAI.
# I gathered some information about {{company_name}}
# from the internet to create a song for your company. You can check it out on Vimeo by pressing the link below:)
#     """,
#     video_link='https://vimeo.com/1001207178',
#     lower_text=\
# """
# You received this message because another AI agent of ours considers your company closely connected to the influencer marketing niche.
#
# Currently, we are working on a fully autonomous AI agent that communicates with customers and filters out the best influencers to promote customers' products (we use the IQData API to retrieve influencers, which is easy to change).
#
# We already have a fully functional MVP. If you have low visitor-to-paying-client conversion at the filtering stage or spend money on professional staff to filter influencers as an agency, let's meet:)
# """,
#
#
#     double_rending_data={'company_name': '5&Vine'},
# )
# print(t)


