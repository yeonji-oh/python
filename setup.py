# 패키지 배포를 위한 설정 파일
from setuptools import setup, find_packages

setup(
    name='yeonji', # 설치 할 때 이름 ex) pip3 install yeonji_
    version='0.1.0',
    packages=find_packages(include=['yeonji', 'yeonji.*']),
    url='https://github.com/yeonji-oh',
    license='pico',
    author='yeonji.oh',
    author_email='yeonji20@naver.com',
    description='just tests',
    keywords=['yeonji', 'test'],
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[], # dependencies
    extras_require={}, # 특정 상황 에서만 설치 할 때 dependencies
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'main = scripts.main_2:main'
        ]
    },
)
