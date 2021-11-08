# README.md

## first, 환경설정에 대해

anaconda로 env 만들은 환경에서 진행

python version = 3.6

## second, 각 파일 설명

### 1. 

```
crawling.py => 선행연구 코드 보고 자막 및 타임 코드 자동 추출(selenium 사용)
```

### 2. 

```
crawling_clova => naver clova에 접속하여 타임 코드 및 자막을 자동으로
추출하려 하였으나 실패(네이버는 selenium을 싫어한다는 소리를 들음)
```

### 3.

```
gcloudsttTest => thapgil
```

### 4.

```
google_api_test => 구글 stt api를 이용하여 timecode와 자막생성, 이 결과를 test.json파일에 저장, test.json이 없을 경우 새로 생성
```

<img src="https://user-images.githubusercontent.com/68285994/137739196-842f7690-1525-4b66-b472-13c2b8dcb444.png" width="300" height="400"/>

### 5.

```
classify_Text ==> text분류하기 (in korean)
데이터는 Naver sentiment movie corpus v1.0을 사용
네이버 영화 리뷰 감정 분석 
==> 영화 리뷰 데이터를 통해 학습한 뒤 해당 리뷰가 긍정적인 리뷰인지 아닌지를 예측
```

### 6.

```
pbl
data는 깃허브의 사이즈 제한으로 올리지 못함
여러 모델 실험 중(CNN, Logistic Regression 등)

```

