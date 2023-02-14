"""Utility functions to turn information from the scraper functions into a readable PDF"""

from fpdf import FPDF
import datetime

def generate_pdf(info):
    #setup pdf
    p = FPDF(orientation = 'P', unit = 'mm', format='A4')
    p.add_page()

    #prepare HTML content for pdf
    date_and_time = datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')

    html = f"""
    <h1>Today's News ------------------- {date_and_time}</h1>
    <br>
    """

    for k in info:
        story_div = f"""
        <h2>{info[k][0]}</h2>
        <br>
        <div>{info[k][1]}</div>
        <br><br>
        <span>View full story at: https://www.abc.net.au{info[k][2]}</span>
        <br><br><br>
        """
        html = html + story_div

    #write HTML to the pdf
    p.write_html(html)

    #save pdf
    p.output('news.pdf')