# 목차

[**1. 오류**](https://github.com/oypark/TIL/blob/master/git_user_tip.md#1-%EC%98%A4%EB%A5%98)

   [(1) LF 오류해결](https://github.com/oypark/TIL/blob/master/git_user_tip.md#1-lf-%EC%98%A4%EB%A5%98%ED%95%B4%EA%B2%B0)


[**2. Git User Tip**](https://github.com/oypark/TIL/blob/master/git_user_tip.md#2-git-user-tip)

   [(1) .gitignore](https://github.com/oypark/TIL/blob/master/git_user_tip.md#1-gitignore)



---



# 1. 오류

## (1) LF 오류해결

([참고 사이트](https://dabo-dev.tistory.com/13))

* 작업을 진행하고 `git add .` 실행

* 하지만 명령어가 실행되지 않고, 워킹 디렉토리의 모든 파일에 대해 다음과 같은 **에러메세지**가 뜸

  ```bash
  warning: LF will be replaced by CRLF in 파일명.ipynb.
  The file will have its original line endings in your working directory
  ```

  >  여기서 `LF`, `CRLF`란?
  >
  > * `LF` (Line-Feed) : Mac, Linux (Unix 계열) 줄바꿈 문자열 = \n 
  > * `CR` (Carriage-Return) : Mac 초기 모델 줄바꿈 문자열 = \r
  > * `CRLF` (Carriage-Return + Line-Feed) : Windows, DOS 줄바꿈 문자열 = \r\n (CR(\r) 와 LR(\n) 두 동작을 합쳐서 (\r\n))

* 즉, OS 계열 마다 줄바꿈을 바라보는 문자열이 다르기 때문에 형상관리를 해주는 Git이 바라볼 때 둘 중 어느 쪽을 선택할지 몰라 경고 메세지를 띄운 것!

* 다음 코드로 오류 해결!

  ```bash
  # Windows, DOS 명령어
  $ git config --global core.autocrlf true
  
  # Linux, MAC 명령어
  $ git config --global core.autocrlf input
  ```

  * `core.autocrlf true` : CRLF 를 `LF 로 변경`
  * `core.autocrlf false` : 플랫폼(OS) 상관없이 줄바꿈에 대한 `문자열 그대로 인식`해 저장 (문제발생 가능성 존재)
  * `core.autocrlf input` : `LF`를 line ending으로 사용



## (2) 용량이 큰 파일 commit 후 push가 안될 때

([참고 사이트](https://gmlwjd9405.github.io/2018/05/25/git-add-cancle.html))

*  용량이 큰 csv 파일을 작업 디렉토리에 저장하고 `git add, commit ` 커멘드를 실행.

* `git push origin master`를 진행하자 다음과 같은 오류 발생 (다음과 같은 오류들이 나왔다.. 해결해보려고 여러가지 시도해보다가 나옴)

  ```bash
  remote: error: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
  remote: error: Trace: 어쩌고 저쩌고 몇줄 더 있고
  ! [remote rejected] master    -> origin 
  error: failed to push some refs to 'https://github.com/디렉토리'
  ```

  ```bash
  error: the following untracked working tree files would be overwritten by merge:
  ```

  ```bash
  error: RPC failed; curl 92 HTTP/2 stream 0 was not closed cleanly: CANCEL (err 8)
  fatal: the remote end hung up unexpectedly
  ```

* 보이는 것 처럼 각각 error들이 모두 다른 말을 하고 있어서 도대체 뭐가 문제인가 싶어서 `git log`를 확인해봤다.

  ![image-20220228220146811](git_user_tip.assets/image-20220228220146811.png)

* origin은 `89e98b7` 까지 업데이트가 되었고, 그 이후 `a1232e5`부터 7개 changes가 push가 되지 않는 상태였다.

  * 사실 해당 changes들은 `.gitignore`를 수정하기 위함이었고, 100MB가 넘는 파일 업로드 하려면 추가 커멘드가 필요하지만 (굳이 안올려도 됐기에) <u>csv 파일은 다른 곳으로 옮겨놓고 커밋 내역을 삭제하기로 결정!</u>

* 문제가 되는 csv 파일을 이동시키고, 아래 코드로 7개의 `commit을 취소`한 후 남아있는 변경 내역만 다시 commit 해줬다.

  ```bash
  $ git reset --mixed HEAD~7
  Unstaged changes after reset:
  M       .gitignore
  
  It took 2.48 seconds to enumerate unstaged changes after reset.  You can
  use '--quiet' to avoid this.  Set the config setting reset.quiet to true
  to make this the default.
  ```

  * 커밋 내역 삭제 후 `git log`

  ![image-20220228221042155](git_user_tip.assets/image-20220228221042155.png)

  * `git add, commit, push` 다시 해준 후 `git log` - 해결완료!

  ![image-20220228221234917](git_user_tip.assets/image-20220228221234917.png)

* (<u>추가정보</u>) `commit 취소` 에 여러가지 옵션이 있어 가져와보았다.

  * `--mixed` 옵션(기본 옵션) : commit 취소, 해당 파일들 unstaged 상태로 working directory에 보존

    ```bash
    $ git reset --mixed HEAD^
    $ git reset HEAD^     #--mixed 생략가능
    $ git reset HEAD~2    #마지막 2개 commit 취소
    ```

  * `--soft` 옵션 : commit 취소, 해당 파일들 staged 상태로 working directory에 보존

    ```bash
    $ git reset --soft HEAD^
    ```

  * `--hard` 옵션 : commit 취소, 해당 파일들 unstaged 상태로 working directory에서 삭제

    ```bash
    $ git reset --hard HEAD^
    ```

    




---


# 2. Git User Tip

## (1) .gitignore

([참고사이트](https://stackoverflow.com/questions/19663093/apply-gitignore-on-an-existing-repository-already-tracking-large-number-of-file))

* 작업 중인 디렉토리를 git이 이미 팔로우 하고 있는 상황에서는 아래와 같이 .gitignore 파일을 생성하고 push를 해도 .gitignore에 저장한 파일 형식이 사라지지 않음

  ```bash
  # .gitignore 파일 생성
  $ touch .gitignore
  
  # 제외하고 싶은 파일 혹은 폴더 지정 후 git add, commit, push 진행
  $ git add .
  
  $ git commit -m "add .gitignore"
  
  $ git push origin master
  ```

* 다음 코드로 해결! (<u>주의사항 확인</u>)

  ```bash
  ## removes all cached instances of the unwanted files
  $ git rm -r --cached .
  
  # git add, commit, push
  $ git add .
  
  $ git commit -m ".gitignore is now working!"
  
  $ git push origin master
  ```

* 모든 파일의 cached instances를 삭제하는 대신, 원하는 `directory를 지정`할 수도 있음!

  * tracking 하고싶지 않은 파일이 `directory` 폴더 아래에 있을 경우, 아래와 같은 코드를 대신 실행!

    ```bash
    $ git rm -r --cached directory/
    ```

* 해당 repository를 push 하고 여전히 tracking 되고 있는 다른 곳을 pull 해올 경우, 이후 작업파일이 모두 삭제될 수 있음 <u>주의</u>!
