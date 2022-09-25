import requests,openpyexcel
from bs4 import BeautifulSoup
try:
    response = requests.get('https://www.imdb.com/search/title/?genres=adventure&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=TDPF6P29ZKAYSZ37BYA5&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_2')
    soup = BeautifulSoup(response.text,'html.parser')
    print(soup)
    movies = soup.find('div',class_ = "lister-list").find_all("div")
    for movie in movies:
        print(movie)
        sno = movie.find('div', class_="lister-item-content").span.text
        print(sno)
        movie_name = movie.find('div',class_ = "lister-item-content").a.text
        print(movie_name)
        year = movie.find('span', class_="lister-item-year").text
        print(year)
        story =movie.find('p',class_ = "text-muted").text
        print(story)
        director = movie.find('p').find_Next('p').find_Next('p').a.text
        print(director)
        break
except Exception as e:
    print(e)

