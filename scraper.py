"""Series of functions defined to scrape the abc.net.au news site to get latest stories"""

import urllib.request
from bs4 import BeautifulSoup as Soup

def open_and_get_site_html():
    site = urllib.request.urlopen("https://www.abc.net.au/news/")
    html = site.read()

    parsed = Soup(html, 'html.parser')

    return parsed

def parse_site_html():
    info_dict = {}
    parsed = open_and_get_site_html()

    list_of_stories = parsed.find_all('ul', class_='ccxVO')[0]

    #getting the top story of the day

    top_story = list_of_stories.find_all('li')[0].div

    top_story_title = top_story.find('div', class_='X-n8k').h3.span.text

    top_story_link = top_story.find('div', class_='wAZpb NzNRI').a['href']

    top_story_excerpt = top_story.find('div', class_='YtLlr EMYbI +5k3g JceSC fm7dv _8teMo _5pKBM').text

    info_dict['top'] = [top_story_title, top_story_excerpt, top_story_link]
    
    #proccessing next three stories

    c = 1
    for i in list_of_stories.find_all('li')[1:3]:
        story = i.div

        story_title = story.find('div', class_='X-n8k').h3.span.text

        story_link = story.find('div', class_='wAZpb').a['href']

        story_excerpt = story.find('div', class_='YtLlr EMYbI +5k3g JceSC fm7dv _8teMo _5pKBM').text

        info_dict[f'Story {c}'] = [story_title, story_excerpt, story_link]

        c += 1
    
    return info_dict