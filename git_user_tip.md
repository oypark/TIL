# 1. 오류

### (1) LF 오류해결

([참고 사이트](https://dabo-dev.tistory.com/13))

* 상황

  > 작업을 진행하고 <u>git add 명령어</u>를 다음과 같이 입력
  >
  > ```bash
  > git add .
  > ```
  >
  > 명령어가 실행되지 않고, 워킹 디렉토리의 모든 파일에 대해 다음과 같은 <u>에러메세지</u>가 뜸
  >
  > ```bash
  > warning: LF will be replaced by CRLF in 파일명.ipynb.
  > The file will have its original line endings in your working directory
  > ```

* `LF`, `CRL`F란?

  * `LF` (Line-Feed) : Mac, Linux (Unix 계열) 줄바꿈 문자열 = \n 
  * `CR` (Carriage-Return) : Mac 초기 모델 줄바꿈 문자열 = \r
  * `CRLF` (Carriage-Return + Line-Feed) : Windows, DOS 줄바꿈 문자열 = \r\n (CR(\r) 와 LR(\n) 두 동작을 합쳐서 (\r\n))

* 에러가 난 이유

  * OS 계열 마다 줄바꿈을 바라보는 문자열이 다르기 때문에 형상관리를 해주는 Git이 바라볼 때 둘 중 어느 쪽을 선택할지 몰라 경고 메세지를 띄운 것!

* <u>해결방안</u>

  ```bash
  # Windows, DOS 명령어
  git config --global core.autocrlf true
  
  # Linux, MAC 명령어
  git config --global core.autocrlf input
  ```

  * `core.autocrlf = true` : CRLF 를 `LF 로 변경`
  * ``core.autocrlf = false` : 플랫폼(OS) 상관없이 줄바꿈에 대한 `문자열 그대로 인식`해 저장 (문제발생 가능성 존재)
  * `core.autocrlf = input` : `LF`를 line ending으로 사용





# 2. Git User Tip

## (1) .gitignore

([참고사이트](https://stackoverflow.com/questions/19663093/apply-gitignore-on-an-existing-repository-already-tracking-large-number-of-file))

* 상황

  > 작업 중인 디렉토리를 git이 이미 팔로우 하고 있는 상황
  >
  > 아래와 같이 .gitignore 파일을 생성하고 push를 해도 .gitignore에 저장한 파일 형식이 사라지지 않음
  >
  > ```bash
  > ## .gitignore 파일 생성
  > touch .gitignore
  > 
  > # .gitignore 파일에 원하는 파일 형식 입력, 저장 후 add-commit-push 진행
  > git add .
  > 
  > git commit -m "make .gitignore file"
  > 
  > git push origin master
  > ```

* 해결방법

  > 작업 중인 디렉토리에 가서 다음과 같은 코드를 수행
  >
  > ```bash
  > ## removes all cached instances of the unwanted files
  > git rm -r --cached .
  > 
  > git add .
  > 
  > git commit -m ".gitignore is now working!"
  > 
  > git push origin master
  > ```
  >
  > 모든 파일의 cached instances를 삭제하는 대신, 원하는 directory를 지정할 수도 있음!
  >
  > tracking 하고싶지 않은 파일이 `directory/`에 있을 경우, 아래와 같은 코드를 대신 실행!
  >
  > ```bash
  > git rm -r --cached directory/
  > ```

* 주의사항
  * 다른 경로에서 rm 명령어 사용하지 않도록 주의!
  * 해당 repository를 push 하고, 여전히 tracking 되고 있는 다른 곳에서 pull 해올 경우 파일이 모두 삭제될 수 있음!
