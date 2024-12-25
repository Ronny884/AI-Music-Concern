from jinja2 import Environment, FileSystemLoader, Template
import base64


def wrap_paragraphs(text):
    paragraphs = text.split('\n\n')
    wrapped_paragraphs = [f'<p>{paragraph.strip()}</p>' for paragraph in paragraphs if paragraph.strip()]
    return '\n'.join(wrapped_paragraphs)


def build_html(
        heading,
        upper_text,
        video_link,
        img_link,
        song_name,
        lower_text,
        double_rending_data: dict = None
):
    file_loader = FileSystemLoader('path/to/template')
    env = Environment(loader=file_loader)
    template = env.get_template('your_template.html')

    data = {
        'heading': heading,
        'text_1': wrap_paragraphs(upper_text),
        'video_link': video_link,
        'img_link': img_link,
        'song_name': song_name,
        'text_2': wrap_paragraphs(lower_text),
    }
    output = template.render(data)

    # двойной рендеринг, если требуется
    if double_rending_data:
        template = Template(output)
        output = template.render(double_rending_data)

    return output


