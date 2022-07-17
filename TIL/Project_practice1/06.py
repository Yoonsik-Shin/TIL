import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    ans = []
    for j in range(len(movies_list)):
        Dict = {}
        lst = []
        for k in range(len(genres_list)):
            if genres_list[k]['id'] in movies_list[j]['genre_ids']:
                lst.append(genres_list[k]['name'])
        Dict['genre_names'] = lst
        for i in ['id','overview','title','vote_average']:
            Dict[i] = movies_list[j][i]
        ans.append(Dict)
    return ans
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))