from googlesearch import search
import webbrowser as wb

domains = []
duplicate = []


def search_google(query):
    query = query.replace('aida search ', '')
    for i in search(query, 5, 'en'):
        y = i.split('/')[2]
        if y in duplicate:
            pass
        else:
            domains.append(i)
            duplicate.append(y)
    for x in domains:
        wb.open(x)
    x = len(domains)
    domains.clear()
    duplicate.clear()
    return f"opening {x} results"
