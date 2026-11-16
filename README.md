# E1-2 컴퓨터에게 명령 내리는 말(파이썬) 처음 배우기

# 🎬 영화 퀴즈 게임

## 📚 목차

| 번호 | 항목 | 확인 내용 |
|---|---|---|
| 1 | [프로젝트 개요](#-프로젝트-개요) | 영화 퀴즈 게임의 목적과 전체 설명 |
| 2 | [퀴즈 주제와 선정 이유](#-퀴즈-주제와-선정-이유) | 영화 퀴즈를 선택한 이유 |
| 3 | [개발 환경](#️-개발-환경) | 운영체제, 에디터, Python, Git 환경 |
| 4 | [실행 방법](#️-실행-방법) | `main.py`를 이용한 프로그램 실행 방법 |
| 5 | [기능 목록](#-기능-목록) | 기본 기능과 보너스 기능 정리 |
| 6 | [파일 구조](#-파일-구조) | `main.py`와 `game` 패키지 구성 |
| 7 | [데이터 파일 설명](#️-데이터-파일-설명) | `state.json`, `history.json`의 역할과 저장 구조 |
| 8 | [실행 화면](#-실행-화면) | 로고, 메뉴, 퀴즈 실행 화면 캡처 |
| 9 | [보너스 과제 구현 내용](#-보너스-과제-구현-내용) | 랜덤 출제, 문제 수 선택, 힌트, 삭제, 점수 히스토리 |
| 10 | [GitHub 저장소 URL](#-github-저장소-url) | 프로젝트 원격 저장소 주소 |
| 11 | [Git 커밋 기록](#-git-커밋-기록) | `git log`를 통한 커밋 내역 확인 |
| 12 | [Git 저장소 복제 및 pull 실습](#git-저장소-복제-및-pull-실습) | `git clone`, `git pull` 실습 과정 |
| 13 | [Git 기초 명령어 사용 증빙](#️-git-기초-명령어-사용-증빙) | Git 기초 명령어 7종 사용 기록 |

## 📌 프로젝트 개요

터미널에서 즐기는 영화 퀴즈 게임입니다.  
사용자는 영화와 관련된 객관식 퀴즈를 풀고 점수를 확인할 수 있습니다.

퀴즈 목록과 최고 점수는 `state.json` 파일에 저장되며, 점수 기록 히스토리는 `history.json` 파일에 저장됩니다.  
프로그램을 종료한 뒤에도 저장된 퀴즈, 최고 점수, 점수 기록을 다시 불러올 수 있습니다.

또한 사용자가 직접 새로운 퀴즈를 추가하거나 기존 퀴즈를 삭제할 수 있습니다.  
보너스 기능으로 랜덤 출제, 문제 수 선택, 힌트 보기, 힌트 사용 시 점수 차감, 점수 기록 히스토리 기능을 구현했습니다.

## 🎯 퀴즈 주제와 선정 이유
**주제**: 영화

**선정 이유**: 한 번쯤 영화를 본 기억이 있는 사람들이 많다고 생각했습니다. 영화는 여러 사람에게 친숙한 주제라서 누구나 쉽게 즐길 수 있을 것 같아 선택했습니다. 저도 평소에 영화를 좋아하는 편입니다.

## 🖥️ 개발 환경

- 운영체제: Linux
- 에디터: Visual Studio Code
- 언어: Python 3.14.4
- 버전 관리: Git 2.53.0, GitHub

![개발 환경 및 원격 저장소 확인](docs/screenshots/vscode_env.png)

## ▶️ 실행 방법
```bash
python3 main.py
```
> Python 3.10 이상 환경에서 실행 가능하며, 개발은 Python 3.14.4 환경에서 진행했습니다.

## ✨ 기능 목록

### 기본 기능

- 퀴즈 풀기
- 정답 확인 및 점수 계산
- 최고 점수 기록 및 갱신
- 새 퀴즈 추가
- 퀴즈 목록 확인
- 게임 데이터 저장 / 불러오기
- JSON 파일 없음·손상 시 예외 처리

### 보너스 기능

- 퀴즈 풀기 시 문제 순서 랜덤 섞기
- 사용자가 풀 문제 수 선택
- 힌트 보기 기능
- 힌트 사용 시 점수 차감
- 등록된 퀴즈 삭제 기능
- 삭제 후 `state.json` 파일에 반영
- 날짜/시간, 푼 문제 수, 점수를 포함한 점수 기록 `history.json` 파일에 저장

## 📁 파일 구조
```
프로젝트/
├── main.py            # 프로그램 진입점, 메뉴 루프
├── state.json         # 게임 데이터 저장 파일
├── history.json       # 날짜/시간, 문제 수, 점수 저장 파일
├── docs/
│   └── screenshots/   # 실행 화면 캡처 이미지
└── game/
    ├── __init__.py    # 패키지 초기화
    ├── util.py        # 공용 유틸 함수
    ├── quiz.py        # Quiz 클래스
    └── quizgame.py    # QuizGame 클래스 (핵심 로직)
```

## 🗂️ 데이터 파일 설명
### 1. state.json
- **경로**: 프로젝트 루트 (`state.json`)
- **역할**: 최고 점수와 퀴즈 목록을 저장/불러오기
- **인코딩**: UTF-8
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
#### 항목 설명

| 항목 | 설명 |
|---|---|
| `quizzes` | 저장된 퀴즈 목록 |
| `question` | 퀴즈 문제 내용 |
| `choices` | 객관식 보기 목록 |
| `answer` | 정답 번호 |
| `hint` | 문제 풀이 중 볼 수 있는 힌트 |
| `best_score.correct` | 최고 점수에서 맞힌 문제 수 |
| `best_score.total` | 최고 점수 당시 푼 문제 수 |

### 2. history.json
- **경로**: 프로젝트 루트 (`history.json`)
- **역할**: 날짜/시간, 푼 문제 수, 점수 기록 저장/불러오기
- **인코딩**: UTF-8
- **스키마**:
```text
{
    "datetime": string,
    "question_count": int,
    "score": int
}
```

#### 항목 설명

| 항목 | 설명 |
|---|---|
| `datetime` | 퀴즈를 푼 날짜와 시간 |
| `question_count` | 해당 게임에서 푼 문제 수 |
| `score` | 해당 게임에서 얻은 점수 |



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

---
### 문제 수 선택
![문제 수 선택](docs/screenshots/question_count.png)

### 힌트 보기
![힌트 보기](docs/screenshots/hint.png)

### 퀴즈 삭제
![퀴즈 삭제](docs/screenshots/delete_quiz.png)

### 점수 기록 히스토리
![점수 기록 히스토리](docs/screenshots/score_history.png)



## ⭐ 보너스 과제 구현 내용

### 1. 랜덤 출제

퀴즈를 풀 때 문제 순서가 항상 같으면 반복 플레이 시 쉽게 정답을 외울 수 있습니다.  
이를 방지하기 위해 `random` 모듈을 사용하여 퀴즈 순서를 무작위로 섞었습니다.

```python
random.sample(self.quizzes, count)
```

이를 통해 게임을 실행할 때마다 다른 순서로 문제가 출제되도록 구현했습니다.

---

### 2. 문제 수 선택

사용자가 전체 문제를 모두 풀지 않고, 원하는 문제 수만 선택해서 풀 수 있도록 구현했습니다.

예를 들어 저장된 퀴즈가 10개라면 사용자는 3문제, 5문제, 10문제처럼 원하는 개수를 선택할 수 있습니다.  
입력한 문제 수가 전체 퀴즈 수보다 많을 경우에는 잘못된 입력으로 처리하거나 전체 문제 수 범위 안에서 선택하도록 안내합니다.

이를 통해 사용자가 상황에 따라 짧게 또는 길게 퀴즈를 풀 수 있습니다.

---

### 3. 힌트 기능

`Quiz` 클래스에 `hint` 속성을 추가하여 각 문제마다 힌트를 저장할 수 있도록 했습니다.

```python
class Quiz:
    def __init__(self, question, choices, answer, hint=""):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint
```

퀴즈를 푸는 중 사용자가 힌트를 요청하면 해당 문제의 힌트를 보여줍니다.

힌트를 사용하면 정답을 맞히더라도 점수가 차감되도록 구현했습니다.  
이를 통해 힌트는 도움을 주지만, 점수에는 영향을 주는 방식으로 게임성을 추가했습니다.

---

### 4. 퀴즈 삭제 기능

등록된 퀴즈 목록을 확인한 뒤, 사용자가 원하는 퀴즈를 삭제할 수 있도록 구현했습니다.

퀴즈 삭제 후에는 변경된 퀴즈 목록을 다시 `state.json` 파일에 저장합니다.  
따라서 프로그램을 종료한 뒤 다시 실행해도 삭제된 퀴즈는 목록에 나타나지 않습니다.

---

### 5. 점수 기록 히스토리

기존 최고 점수 저장 기능에 더해, 모든 게임 기록을 저장하는 점수 기록 히스토리 기능을 구현했습니다.

각 기록에는 다음 정보가 저장됩니다.

| 저장 항목 | 설명 |
|---|---|
| 날짜/시간 | 퀴즈를 푼 시점 |
| 푼 문제 수 | 해당 게임에서 출제된 문제 수 |
| 점수 | 맞힌 문제 수 |

예시는 다음과 같습니다.

```text
1. 날짜/시간: 2026-11-16 14:30:21 | 푼 문제 수: 5 | 점수: 4/5
2. 날짜/시간: 2026-11-16 15:10:08 | 푼 문제 수: 3 | 점수: 3/3
```

이를 통해 사용자가 이전에 푼 기록을 확인하고, 자신의 점수 변화를 볼 수 있도록 했습니다.

---

### 6. 최고 점수 비교 방식

문제 수 선택 기능이 추가되면서 단순히 맞힌 문제 수만 비교하면 공정하지 않을 수 있습니다.

예를 들어 3문제 중 3문제를 맞힌 기록과 10문제 중 5문제를 맞힌 기록은 다음과 같이 비교할 수 있습니다.

```text
3 / 3 = 100%
5 / 10 = 50%
```

따라서 이 프로젝트에서는 최고 점수를 갱신할 때 다음 기준을 사용했습니다.

```text
1. 정답률이 더 높은 기록을 최고 점수로 저장
2. 정답률이 같다면 맞힌 문제 수가 더 많은 기록을 최고 점수로 저장
```

이 기준을 사용하면 사용자가 선택한 문제 수가 달라도 더 공정하게 최고 점수를 비교할 수 있습니다.



## 💾 GitHub 저장소 URL

`https://github.com/kyu99-dev/E1-2`


## 🧾 Git 커밋 기록

```bash
git log --oneline --graph
```
![git_log](docs/screenshots/git-log.png)


## 📍Git 저장소 복제 및 pull 실습

퀴즈 게임 개발 완료 후, `clone`과 `pull` 명령어를 실습하였다.

### 1. 저장소 복제

원격 저장소를 별도의 로컬 디렉터리에 복제하였다.

```bash
git clone git@github.com:kyu99-dev/E1-2.git
```

실행 결과:

```text
Cloning into 'E1-2'... 
remote: Enumerating objects: 59, done.
remote: Counting objects: 100% (59/59), done.
remote: Compressing objects: 100% (41/41), done.
remote: Total 59 (delta 24), reused 48 (delta 16), pack-reused 0 (from 0)
Receiving objects: 100% (59/59), 461.54 KiB | 816.00 KiB/s, done.
Resolving deltas: 100% (24/24), done.
```

### 2. 복제된 저장소에서 변경 후 push

복제된 저장소에서 README.md에 git clone 로그를 추가한 뒤 commit 후 push하였다.

```bash
git add .
git commit -m "docs: clone 실습 문구 추가"
git push
```

### 3. 기존 로컬 작업 디렉터리에서 pull

기존 로컬 작업 디렉터리에서 원격 저장소의 변경사항을 가져왔다.

```bash
git pull
```

실행 결과:

```text
Updating 7baed6a..e3afa59
Fast-forward
 README.md | 16 +++++++++++++++-
 1 file changed, 15 insertions(+), 1 deletion(-)
```

### 4. 실습 결과

`git pull` 실행 결과 변경사항이 정상 반영되었다.  
이를 통해 clone한 저장소에서 push한 README.md 변경사항이 기존 로컬 작업 디렉터리에 성공적으로 적용되었음을 확인하였다.

## 🛠️ Git 기초 명령어 사용 증빙

프로젝트 진행 과정에서 Git 기초 명령어 7종을 각각 한 번 이상 사용하였다.

| 명령어 | 사용 내용 | 증빙 |
|---|---|---|
| `git init` | 프로젝트 폴더를 Git 저장소로 초기화 | 초기 커밋 및 Git 저장소 생성 |
| `git add` | 변경 파일을 스테이징 영역에 추가 | 여러 커밋 생성 과정에서 사용 |
| `git commit` | 변경 사항을 커밋으로 저장 | `git log --oneline --graph` 결과 |
| `git push` | 로컬 커밋을 GitHub 원격 저장소에 업로드 | `origin/main`이 `HEAD -> main`과 동일 |
| `git pull` | 원격 저장소 변경 사항을 로컬에 반영 | Fast-forward 실행 결과 기록 |
| `git checkout` | 브랜치 이동 및 작업 브랜치 사용 | `feature/quiz-play` 브랜치에서 `main` 브랜치로 이동한 기록 |
| `git clone` | 원격 저장소를 별도 폴더에 복제 | clone 실행 결과 기록 |

### git checkout 실행 결과
---
```bash
git branch
```
```text
* feature/quiz-play
  main
```
---
```bash
git checkout main
```

```text
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
```