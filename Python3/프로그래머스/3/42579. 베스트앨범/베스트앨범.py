def solution(genres, plays):
    from collections import defaultdict
    
    answer = []
    
    # 장르별 누적 재생수 계산
    genre_count = defaultdict(int)
    # 장르별 노래 저장
    genre_music = defaultdict(list)
    
    for i in range(len(plays)):
        genre_count[genres[i]] += plays[i]
        genre_music[genres[i]].append((plays[i], i))

    
    # 누적 조회수가 많은 순으로 장르 정렬
    genre_sorted = sorted(genre_count.items(), key=lambda x: x[1], reverse=True)
    
    for genre, _ in genre_sorted:
        # 장르에 해당하는 노래들을 조회수 내림차순 정렬
        music_sorted = sorted(genre_music[genre], key=lambda x: x[0], reverse=True)
        # 상위 2개의 노래만 앨범에 추가
        for play, idx in music_sorted[:2]:
            answer.append(idx)
    
    return answer
