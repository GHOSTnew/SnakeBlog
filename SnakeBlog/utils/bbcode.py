from django.utils.html import strip_tags
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import re


def parse(text):
    text = strip_tags(text)  # on clean le text
    text = re.compile(r'\[h([1-6])\](.*?)\[\/h([1-6])\]').sub("<h\g<1>>\g<2></h\g<1>>", text)
    text = re.compile(r'\[b\](.*?)\[\/b\]').sub("<strong>\g<1></strong>", text)
    text = re.compile(r'\[i\](.*?)\[\/i\]').sub("<em>\g<1></em>", text)
    text = re.compile(r'\[u\](.*?)\[\/u\]').sub("<u>\g<1></u>", text)
    text = re.compile(r'\[s\](.*?)\[\/s\]').sub("<strike>\g<1></strike>", text)
    text = re.compile(r'\[sup\](.*?)\[\/sup\]').sub("<sub>\g<1></sub>", text)
    text = re.compile(r'\[sub\](.*?)\[\/sub\]').sub("<sup>\g<1></sup>", text)
    text = re.compile(r'\[code\](.*?)\[\/code\]', re.DOTALL).sub(synthaxdefault, text)
    text = re.compile(r'\[code=([a-zA-z0-9\-]+)\](.*?)\[\/code\]', re.DOTALL).sub(synthaxspecific, text)
    text = re.compile(r'\[url\](.*?)\[\/url\]').sub("<a href=\"\g<1>\">\g<1></a>", text)
    text = re.compile(r'\[url=(.*?)\](.*?)\[\/url\]').sub("<a href=\"\g<1>\">\g<2></a>", text)
    text = re.compile(r'\[img\](.*?)\[\/img\]').sub("<img src=\"\g<1>\"/>", text)
    text = re.compile(r'\[color=(.*?)\](.*?)\[\/color\]').sub("<font color=\"\g<1>\">\g<2></font>", text)
    text = re.compile(r'\[ul\](.*?)\[\/ul\]').sub("<ul>\g<1></ul>", text)
    text = re.compile(r'\[li\](.*?)\[\/li\]').sub("<li>\g<1></li>", text)
    text = re.compile(r'\[ol\](.*?)\[\/ol\]').sub("<ol>\g<1></ol>", text)
    text = re.compile(r'\[hr\]').sub("<hr/>", text)
    text = re.compile(r'\[br\]').sub("<br/>", text)
    return text


def synthaxdefault(code):
    code = code.group(1)
    lexer = get_lexer_by_name("python", stripall=True)
    formatter = HtmlFormatter(linenos=False, cssclass="source")
    return highlight(code, lexer, formatter)


def synthaxspecific(data):
    code = data.group(2)
    lang = data.group(1)
    lexer = get_lexer_by_name(lang, stripall=True)
    formatter = HtmlFormatter(linenos=False, cssclass="source")
    return highlight(code, lexer, formatter)
