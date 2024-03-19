import glob
import pandas as pd
# 파일 경로 어디/서브디렉토리/파일.shp 형식을 찾아달라는 의미
target = r'C:\py_source\mini project\mini project\유동인구분석/**/*.shp'
# target 양식을 지키는 모든 파일을 리스트로 저장
f_list = glob.glob(target) # target 양식을 지키는 모든 파일을 리스트로 저장
f_list_new =[]
for i in range(len(f_list)):
    df = gpd.read_file(f_list[i],encoding='cp949')
    df['center_point'] = df['geometry'].centroid
    df['center_point'] = df['center_point'].to_crs(epsg=4326)
    # 경도
    df['lng'] = df['center_point'].map(lambda x:x.xy[0][0])
    # 위도
    df['lat'] = df['center_point'].map(lambda x:x.xy[1][0])
    df['addr'] = f_list[i].split('\\')[-1].split('_')[1].replace('.shp', '')
    f_list_new.append(df)
    
result = pd.concat(f_list_new, axis=0)

# Hive query에서 쉼표를 인식 못하는 문제 발생
# polygen 출력값에서 쉼표 제거 후 ':' 으로 대체
result = result.astype({'geometry' : 'str'})
temp = pd.DataFrame({'new_geometry' : []})
# new_geometry라는 단일열을 갖고 문자열 형식의 geometry의 값을 갖는 새로운 데이터프레임
for item in result['geometry'] :
    tempp = pd.DataFrame({'new_geometry' : [item.replace(',', ':')]})
    temp = pd.concat([temp, tempp])
c_list = temp['new_geometry'].tolist()

# 기존 result 데이터 프레임에서 'geometry'열 제거 
result.drop('geometry',axis=1,inplace=True)

# ,를 :로 대체한 polygen을 원소로 갖는 리스트 c_list를 기존의 result에 새로운 열로 추가
result['geometry'] = c_list
result.columns
new_order = ['id', 'left', 'top', 'right', 'bottom', '_14age', '20_50T21_', '65age_',
       '20_60T9_18', 'weekend','geometry', 'center_point', 'lng', 'lat', 'addr']
result = result.reindex(columns=new_order)

result.to_csv('유동인구.csv',index=False,encoding='UTF-8')