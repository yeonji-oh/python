# python

pip install -e .					# install_requires만 설치
pip install -e .[interactive]		# extras_require도 같이 설치!
pip install -e yeonji_[interactive] # extras_require도 같이 설치!

# requirements.txt 생성
pip freeze > requirements.txt

# 필요한 모든 패키지 설치
pip install -r requirements.txt

----
주의 사항
pip freeze가 현재 환경에 설치된 모든 패키지를 포함하므로,
이 명령을 실행 하기 전에 새 가상 환경을 생성하고 필요한 패키지만 설치하는 것이 좋다.
이렇게 하면 requirements.txt 파일이 프로젝트에 필요한 패키지만 포함하게 된다.
가상 환경은 venv 나 conda 같은 도구를 이용하여 생성할 수 있다.
----

# 실행 파일 만들기
pip install pyinstaller
pyinstaller --onefile scripts/main_2.py
dist 하위 참고
mac, window 환경별로 명령어 다름, pyinstaller는 빌드하는 환경에 따라 만들어줌

# 패키지 설치 파일 만들기
pip install setuptools wheel
python setup.py sdist bdist_wheel
dist 하위 참고

---
주의사항
import 한 패키지 폴더들의 경로를 잘 생각 하자..
---
