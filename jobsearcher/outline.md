# Job Searcher 
1. 검색어를 입력받아 해당하는 구인구직 정보를 스크래핑
- 1-1. 스크래핑할 사이트: 1) 링크드인 2) 인디드 3) 스택오버플로우 
- 1-2. 페이징은 페이징 형식으로, 스크롤 다운은 스크롤 다운 형식으로 끝까지 가져오기.
    1) 스크롤 방식: google_movie_scroll 참조 (prev_height == curr_height 일 때까지 반복)
    2) 페이징 방식: next 화살표가 없을 때까지 반복

2. 가져온 정보를 WEB으로 보여주기 (flask)
- 2-1. 검색어 입력 후 조회 시 동작
- 2-2. 가져온 정보 한번에 보여주기 => 스크롤 다운 시 불러오기
- 2-3. csv 파일로 저장


title,company,location,link

## 사이트 주소
https://www.linkedin.com/jobs/search?keywords=Python&location=worldwide&geoId=&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0

https://www.indeed.com/jobs?q=python&limit=50

https://stackoverflow.com/jobs?q=python