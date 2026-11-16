# E1-2 컴퓨터에게 명령 내리는 말(파이썬) 처음 배우기

# 🎬 영화 퀴즈 게임

## 📌 프로젝트 개요
터미널에서 즐기는 영화 퀴즈 게임입니다.
사용자가 퀴즈를 풀고 점수를 기록하며, 최고 점수가 저장됩니다.
새로운 퀴즈를 직접 추가할 수도 있습니다.

## 🎯 퀴즈 주제와 선정 이유
- **주제**: 영화
- **선정 이유**: 한 번쯤 영화를 본 기억이 있는 사람들이 많다고 생각했습니다. 영화는 여러 사람에게 친숙한 주제라서 누구나 쉽게 즐길 수 있을 것 같아 선택했습니다. 저도 평소에 영화를 좋아하는 편입니다.

## 🖥️ 개발 환경

- 운영체제: Linux
- 에디터: Visual Studio Code
- 언어: Python 3.14.4
- 버전 관리: Git 2.53.0, GitHub


## ▶️ 실행 방법
```bash
python3 main.py
```
> > Python 3.10 이상 환경에서 실행 가능하며, 개발은 Python 3.14.4 환경에서 진행했습니다.

## ✨ 기능 목록
- 퀴즈 풀기 (정답 확인 및 점수 계산)
- 최고 점수 기록 및 갱신
- 새 퀴즈 추가
- 게임 데이터 저장 / 불러오기 (JSON)
- 파일 없음·손상 시 예외 처리

## 📁 파일 구조
```
프로젝트/
├── main.py            # 프로그램 진입점, 메뉴 루프
├── state.json         # 게임 데이터 저장 파일
├── docs/
│   └── screenshots/   # 실행 화면 캡처 이미지
└── game/
    ├── __init__.py    # 패키지 초기화
    ├── util.py        # 공용 유틸 함수
    ├── quiz.py        # Quiz 클래스
    └── quizgame.py    # QuizGame 클래스 (핵심 로직)
```

## 🗂️ 데이터 파일 설명 (state.json)
- **경로**: 프로젝트 루트 (`./state.json`)
- **역할**: 최고 점수와 퀴즈 목록을 저장/불러오기
- **인코딩**: UTF-8
- **스키마**:
- **스키마**:

```text
{
  "quizzes": [
    {
      "question": string,
      "choices": string[],
      "answer": int
    }
  ],
  "best_score": {
    "correct": int,
    "total": int
  }
}
```
- `question`: 퀴즈 문제 내용
- `choices`: 객관식 보기 목록
- `answer`: 정답 번호
- `best_score.correct`: 최고 점수에서 맞힌 문제 수
- `best_score.total`: 최고 점수 당시 전체 문제 수

## 📷 실행 화면

### 로고 
![로고](docs/screenshots/logo.png)

### 메인 메뉴
![메인 메뉴](docs/screenshots/menu.png)

### 퀴즈 풀기
![퀴즈 풀기](docs/screenshots/play.png)

### 퀴즈 추가
![퀴즈 추가](docs/screenshots/add_quiz.png)

### 점수 확인
![점수 확인](docs/screenshots/score.png)

### 퀴즈 목록
![퀴즈 목록](docs/screenshots/list.png)


## 🧾 Git 커밋 기록

```bash
git log --oneline --graph
```
![git_log](docs/screenshots/git-log.png)