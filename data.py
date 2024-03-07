import pandas as pd
from pandas.core.construction import array

df = pd.read_csv('data/20211123_ssbn13hs01.csv') # csv 파일 열기
df = df.drop(index=[0, 1], axis=0) # 파일 정보부분 제거

df.set_index('row_num', inplace = True) # row_num 인덱스 설정

df.to_csv("data.csv", mode='w') # csv 파일로 저장

df = pd.read_csv('data.csv')
df = df.astype({'row_num':'int'}) # row_num을 정수형 설정
df = df.astype({'signal':'string'}) # 배열 타입형을 문자열로 지정

df.set_index('row_num', inplace = True) # row_num을 인덱스로 설정

df['signal'] = df['signal'].str.slice(start=1, stop=-1) # 배열을 문자열 슬라이싱으로 전처리

df = df.sort_index(ascending=True) # 인덱스 정렬
df.to_csv("data.csv", mode='w') # csv 파일로 저장
