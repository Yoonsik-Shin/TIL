import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    Dict = {}
    lst = []
    for k in range(len(genres_list)):
        if genres_list[k]['id'] in movie['genre_ids']:
            lst.append(genres_list[k]['name'])
    Dict['genre_names'] = lst
    for i in ['id','overview','title','vote_average']:
        Dict[i] = movie[i]
    return Dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))