from pyproj import Transformer
import pyproj
import numpy as np
import pandas as pd
from shapely.geometry import Point as point
import geopandas as gpd
import folium
import random

import glob

target = 'path/to/*.shp'  # *.shp 상위 경로 디렉토리
# target 양식을 지키는 모든 파일 리스트형태로 저장
f_list = glob.glob(target)

def getMap(m,file_Path):
    # 구역별 색상선택을 위한 랜덤 변수
    color_random = "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
    # cp949로 안하면 인코딩이 안됨
    df = gpd.read_file(file_Path, encoding='cp949')
    # 중심좌표 구하고 4326 EPSG 좌표게 변환
    df['center_point'] = df['geometry'].centroid
    df['center_point'] = df['center_point'].to_crs(epsg=4326)
    # 경도
    df['lng'] = df['center_point'].map(lambda x:x.xy[0][0])
    # 위도
    df['lat'] = df['center_point'].map(lambda x:x.xy[1][0])
    # geometry의 중간 좌표 구하기
    df['center_point'] = df['geometry'].centroid
    # 경도 위도의 위치
    df_x = df['lng']
    df_y = df['lat']
    # 좌표들을 저장할 리스트
    coords = []
    # 좌표 추가
    for i in range(len(df)-1):
        x = df_x[i]
        y = df_y[i]
        coords.append([y, x])
    # 그리드 별 원 그리기
    for i in range(len(coords)):
        folium.Circle(
            location = coords[i],
            radius = 50,
            color = color_random,
            fill = 'crimson',
        ).add_to(m)
    # 다음 구역을 위한 좌표 초기화
    coords=[]
    # 지도 html에 저장하기
    m.save('C:\\Users\\Playdata\\Desktop\\study/map.html')
  
  # m = 지도 초기 좌표 지정
m = folium.Map([37.576454, 126.920860], zoom_start = 9)
for file in f_list:
    getMap(m,file)

m