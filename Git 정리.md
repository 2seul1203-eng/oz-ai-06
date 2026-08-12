# Git & GitHub

## 버전 관리의 필요성

### 버전 관리(Version Control)란
파일이나 코드의 변경 이력을 체계적으로 기록하고 관리하는 것. 언제, 누가, 무엇을 바꿨는지 알 수 있고 필요하면 과거 상태로 되돌릴 수 있음.

필요한 이유: 변경 이력 추적, 실수 복구, 여러 사람이 충돌 없이 협업.

활용 예시
- 기능 추가 후 버그 발생 시 이전 정상 버전으로 바로 복구 가능
- 여러 명이 동시에 같은 파일을 수정해도 누가 뭘 바꿨는지 확인하고 충돌 해결 가능
- "최종_진짜최종_v3" 같은 파일명 없이 변경 과정을 관리 가능

### Git vs 파일 복사
파일 복사 방식: final.py, final_v2.py 식으로 파일이 계속 늘어남. 변경 이유와 내용이 남지 않고, 협업 시 최신 파일 구분이 어려움.

Git 방식: 변경 내용이 커밋 단위로 기록됨. 특정 시점으로 되돌릴 수 있고, 동시 작업이 가능하며 변경 이력과 책임이 명확함.

### Git vs GitHub
Git: 버전 관리 도구(프로그램). 내 컴퓨터에서 동작.

GitHub: Git 저장소를 올려두는 웹 서비스. 코드 공유 및 협업 플랫폼. Pull Request, Issue, Review 기능 제공.

Git은 버전 관리 엔진, GitHub는 협업과 공유를 위한 서비스.

## Git 기본 개념

### Repository(레포지토리)
파일과 변경 이력을 함께 관리하는 저장소. 프로젝트 전체와 모든 버전 기록이 들어 있음.

- 로컬 저장소: 내 컴퓨터에 있는 저장소. 프로젝트 폴더에서 `git init` 실행 시 생성됨.
- 원격 저장소: GitHub 같은 서버에 있는 저장소. GitHub에서 새 Repository 생성 후 `git clone`으로 로컬에 복사.

### Commit(커밋)
변경 사항을 하나의 기록으로 저장하는 단위(= 하나의 버전). 무엇을 왜 바꿨는지 메시지로 남기고, 특정 시점의 프로젝트 상태를 저장. 되돌아갈 수 있는 기준점 역할.

생성: `git commit -m "메시지"`

### Branch(브랜치)
독립적으로 작업할 수 있는 작업 공간. 기존 코드를 건드리지 않고 기능 개발 가능하며, 여러 기능을 동시에 개발 가능. 작업 종료 후 병합(merge).

생성: `git branch feature/login`
전환: `git switch feature/login`

### HEAD(헤드)
현재 작업 중인 위치를 가리키는 포인터. 보통 현재 브랜치의 최신 커밋을 가리킴. HEAD가 이동한다는 것은 작업 기준이 바뀐다는 의미.

### Working Directory / Staging Area / Repository
- Working Directory: 실제로 파일을 수정하고 작업하는 공간. 아직 Git에 기록되지 않은 변경 사항이 있는 상태.
- Staging Area: 다음 커밋에 포함할 변경 사항을 미리 모아두는 공간.
- 흐름: working directory → (`git add`) → staging area → (`git commit`) → repository

## Git 초기 설정

### git config
Git의 기본 동작을 설정하는 명령어.

- 전역 설정(모든 저장소 적용): `git config --global user.name "이름"`, `git config --global user.email "이메일"`
- 로컬 설정(특정 저장소만 적용, 프로젝트별로 다른 계정/역할 필요 시 사용): `git config user.name "이름"`, `git config user.email "이메일"`

## 로컬에서 Git 사용하기

### git init
현재 폴더를 Git 레포지토리로 초기화. `.git` 폴더가 생성되고, 그 폴더를 기준으로 버전 관리 시작.

### git status
현재 레포지토리 상태 확인. 수정된 파일, 스테이징 여부, 커밋 가능한 변경 사항을 보여줌.

### git add
변경된 파일을 Staging Area로 올리는 명령어. `git add 파일명` 또는 `git add .`. 커밋에 포함할 변경 사항을 선택하는 단계이며 아직 커밋이 생성된 것은 아님.

### git commit
Staging Area에 있는 변경 사항을 하나의 버전으로 기록. `git commit -m "커밋 메시지"`. 커밋은 되돌릴 수 있는 기준점 역할.

### 커밋 메시지 작성 규칙
좋은 커밋 메시지는 무엇을 했는지 한눈에 알 수 있어야 함.

권장: 명확하고 간결하게 작성, 동사로 시작, 한 커밋 = 한 작업.
예시: Add login API / Fix password validation bug / Refactor user service

### .gitignore
버전 관리에서 제외할 파일을 지정하는 설정 파일. 불필요한 파일이 커밋되는 것을 방지.

예시: `.env`, `__pycache__/`, `*.log`

주의: 이미 커밋된 파일은 Git이 계속 추적하므로 `.gitignore`에 추가해도 제외되지 않음. `git rm --cached 파일명`으로 추적을 해제해야 함.

## 브랜치 이해하기

### Branch
기존 작업과 분리된 독립적인 작업 흐름. 기능 개발, 실험, 수정 작업을 안전하게 진행 가능. 협업과 안정적인 배포를 위해 브랜치 관리가 중요.

주요 명령어
- 목록 확인: `git branch`
- 생성: `git branch feature/ui`
- 전환: `git switch feature/ui`

### 브랜치 관리 전략
어떻게 브랜치를 나누고 합칠지에 대한 약속.

- main: 배포 가능한 안정 버전
- dev: 개발 중인 기능을 테스트하는 버전
- feature/*: 기능 개발
- hotfix/*: 긴급 수정

### 브랜치 병합(git merge)
다른 브랜치의 작업 내용을 현재 브랜치로 합치는 명령어. `git merge feature/ui`

### Fast-forward vs 3-way merge
- Fast-forward merge: 브랜치가 직선으로 이어질 때. 단순히 커밋 포인터만 이동.
- 3-way merge: 브랜치가 갈라졌다가 다시 합쳐질 때. 병합 커밋이 생성됨.

분기가 없으면 Fast-forward, 분기가 있으면 3-way merge.

### Merge conflict
같은 파일의 같은 부분을 서로 다르게 수정하면 발생.

해결 방법: 충돌 파일 확인 → 충돌 코드 직접 수정 → 새로운 커밋 생성.

Git은 자동 병합을 시도하고, 판단이 필요한 경우만 충돌로 알려줌.

## GitHub

### GitHub 계정과 저장소 생성
Git 저장소를 호스팅하는 서비스. 계정 생성 후 새 Repository를 만들면 원격 저장소 주소(URL) 발급.

원격 저장소: 인터넷에 있는 Git 저장소. 여러 사람이 같은 코드 공유, 백업 역할, 협업의 기준점.

`git remote add origin 원격주소`
`git remote -v`

### git push / git pull
로컬과 원격 저장소를 동기화하는 명령어.

- `git push`: 로컬 커밋을 원격 저장소로 올림. `git push -u origin main`
- `git pull`: 원격 변경 사항을 내려받아 로컬에 반영.

## 실습

### Clone vs Fork
- Clone: 원격 저장소를 그대로 내 로컬로 복사. 같은 저장소에 push 권한이 있을 때 사용. 팀 내부 협업에 주로 사용.
- Fork: 다른 사람의 저장소를 내 GitHub 계정으로 복사. 원본 저장소에 직접 push 권한이 없을 때 사용. 오픈소스 기여 방식.

### Pull Request
변경 사항을 원본 저장소에 반영해달라고 요청하는 것. 변경 내용 설명, 리뷰 요청, 병합 전 검증 단계 역할.

### Code Review 기본
코드를 병합하기 전 함께 확인하는 과정. 버그 예방, 코드 품질 유지, 팀 규칙 공유가 목적.

기본 원칙: 코드 중심으로 리뷰, 이유를 남긴 코멘트, 승인 후 병합.

### Issue
할 일, 버그 리포트, 기능 요청 등을 관리하는 기능. PR과 Issue를 연결해 작업 관리.

### 협업 흐름(Fork & Clone)
1. Issue 생성
2. 내 GitHub 계정으로 Fork
3. `git clone 내_포크_저장소_URL`
4. `git remote add upstream 원본_저장소_URL`
5. `git pull upstream main`
6. `git switch -c feature/add-my-name`

### 협업 흐름(Collaborator)
1. Repository collaborator 등록
2. Branch protection rules 추가(예: Require a pull request before merging)
3. `git clone 원본_저장소_URL`
4. `git switch -c feature/mybranch` 후 `git commit -m "message"`
5. `git push origin feature/mybranch`
6. GitHub에서 feature/mybranch → main으로 Pull Request 생성

## 자주 사용하는 명령어

### git show
특정 커밋 하나를 집중해서 살펴볼 때 사용. 변경 내용(diff), 커밋 메시지, 작성자, 날짜 출력. 코드 리뷰나 이력 확인 시 사용.

- `git show`: HEAD와 동일
- `git show HEAD`: 현재 브랜치의 최신 커밋 확인
- `git show 커밋해시`: 특정 커밋 지정 확인

### git diff
두 상태 간의 차이점만 비교해서 보여주는 명령어. 커밋 전 변경 사항 점검, 병합·충돌 원인 분석에 사용.

- `git diff`: Working Directory ↔ Staging Area
- `git diff --staged`: Staging Area ↔ HEAD
- `git diff HEAD~1 HEAD`: 커밋 ↔ 커밋

### git blame
파일의 각 줄이 누가, 언제, 어떤 커밋에서 수정했는지 추적. 버그 원인 추적 시 사용.

`git blame main.py`

### git stash
현재 작업 중인 변경 사항을 임시로 치워두는 명령어. 커밋하지 않고 작업을 잠시 중단할 때, 브랜치 이동이나 긴급 수정 시 유용.

- `git stash`: 변경 사항 임시 저장
- `git stash list`: 저장된 stash 목록 확인
- `git stash pop`: 가장 최근 stash를 다시 적용하고 목록에서 제거
- `git stash apply`: 제거하지 않고 적용만

### git reset
브랜치의 기준을 과거 커밋으로 이동시키는 명령어. 히스토리를 바꾸므로 협업 브랜치에서 사용 시 주의.

- `--soft`: 커밋만 취소, 변경 내용 유지
- `--mixed`(기본): 커밋 + 스테이징 취소
- `--hard`: 전부 삭제

`git reset --soft HEAD~1`: HEAD만 한 커밋 이전으로 이동, 변경 내용 유지
`git reset --hard HEAD~1`: HEAD 이동 + 스테이징 + 파일까지 모두 되돌림

### git revert
특정 커밋을 되돌리는 새 커밋을 생성. 기존 기록은 그대로 유지되고 "이 커밋을 취소했다"는 기록이 남음. 협업 중 안전하게 롤백할 때 사용.

`git revert 커밋해시`

### git commit --amend
마지막 커밋을 고치는 옵션. 가장 최근 커밋을 새 커밋으로 교체하며 커밋 메시지 수정, 변경 파일 추가/제거 가능.

- `git commit --amend`: 마지막 커밋 수정
- `git commit --amend --no-edit`: 기존 커밋 메시지 유지
