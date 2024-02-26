import webbrowser as wb
import talk


def open_site(link):
    talk.say(f'Opening {link}')
    wb.open(f'https://{link}')
