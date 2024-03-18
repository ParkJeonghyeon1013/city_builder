## **Project name**

: 음.. 일단 USD IO이긴 한데 변경해보자.. 

Weather village? 
Village Builder? City builder.. ?

## **Goal**

- **넣고 싶은 수업 내용들:**
thread / DB or pandas / bitmask / logging / 이빠진 프레임 혹은 0byte 이미지 거르기 / web API
- **보여주고자 하는 것:** 
maya / houdini asset 사용해서 씬 구성 variation
- **배우고자 하는 것:**
houdini / USD 익히기
수업에서 배운 내용 응용
stand alone tool 개발 (= 자동화 툴)
- **사용툴:** 
houdini / shotgrid / slack / pyhcarm + [maya]

---

## **Process**

- 프로세스를 세분화 하여 일단 한번 전반을 구현한 후 디테일 잡아가는 걸로!
    
    1. [maya] : 마야 건물 asset
    2. [houdini] : 구름 asset or 날씨?(눈 비 구름)
    3. [houdini] : 도시 씬 자동화 랜덤 구성 or 구름 및 건물 선택 가능 
    4. [houdini] :→ 사용자가 프레임 별 이미지 확인→ 이빠진 프레임 혹은 0btye 이미지 거르기→ 맘에 안들면 해당 프레임 혹은 전체 프레임 다시 랜더
    5. [?] : mov 형태로 뽑기→ 사용자가 해당 mov 확인
    6. [Shotgrid] : 해당 mov shotgrid에 등록7. [Slack] : 알람 보내기

**1차 목표 >> 도시 자동 생성 Builder Viewer Alarm** 

1. [Houdini] 자동화 도시 builder 만들기
2. [Qt] 랜더 돌려 이미지 뽑아 보여주기
3. [Houdini]

---

1. **UI design