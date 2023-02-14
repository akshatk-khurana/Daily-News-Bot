from scraper import parse_site_html
from to_pdf import generate_pdf

if __name__ == '__main__':
    green = '\u001b[32m'

    print(green+'Parsing site...')
    info = parse_site_html()

    print(green+'Generating PDF...')
    generate_pdf(info)

    print(green+'Complete saved as news.pdf!')