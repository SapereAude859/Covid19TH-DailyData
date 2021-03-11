# 🦠 Covid19TH-DailyData ![Python application](https://github.com/pluz85/TH-Covid-19-Tableau-WDC/workflows/Python%20application/badge.svg) ![daily-data](https://github.com/pluz85/Covid19TH-DailyData/workflows/daily-data/badge.svg?event=schedule) 	![GitHub](https://img.shields.io/github/license/pluz85/Covid19TH-DailyData?logo=MIT)
ข้อมูล Covid-19 ประเทศไทย เป็นวัตถุดิบในการใช้งานต่างๆ จาก [Covid-Tracker](https://covidtracker.5lab.co/), [Covid19.th-Stat](https://covid19.th-stat.com/) และ [Data.go.th](https://data.go.th/dataset/covid-19-daily)


## ประเภทไฟล์ 🗃
> - [CSV](https://github.com/pluz85/Covid19TH-DailyData/tree/master/dataset/csv) หรือ Comma Separated Value เหมาะสำหรับเป็นวัตถุดิบในการวิเคราะห์ในโปรแกรมต่างๆ เช่น Tableau
>
> - [JSON](https://github.com/pluz85/Covid19TH-DailyData/tree/master/dataset/json) เหมาะสำหรับการพัฒนาเวปหรือ App ต่าง ๆ
>
> - [Excel 🔥](https://github.com/pluz85/Covid19TH-DailyData/tree/master/dataset/xlsx) ซึ่งเป็นไฟล์ประเภทที่โดนขอมากที่สุด 😫 และคนใช้เยอะที่สุด จึงเป็นจุดเริ่มต้นในการเขียน Workflow ในการเก็บไฟล์ต่างๆ

## ชื่อไฟล์ 📑

>|       ชื่อไฟล์       |                รายละเอียด                |                       ที่มา                       |                                                      Excel                                                     |                                                     CSV                                                     |                                                      JSON                                                      |
>|:-----------------:|:---------------------------------------:|:-----------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
>| `covid-tracker.*` |     ข้อมูลรายละเอียดจุดต่างๆใน 5lab tracker ✨ (Service Shutdown)|  [Covid-Tracker](https://covidtracker.5lab.co/) | [covid-tracker.xlsx](https://github.com/pluz85/Covid19TH-DailyData/raw/master/dataset/xlsx/covid-tracker.xlsx) | [covid-tracker.csv](https://github.com/pluz85/Covid19TH-DailyData/raw/master/dataset/csv/covid-tracker.csv) | [covid-tracker.json](https://github.com/pluz85/Covid19TH-DailyData/raw/master/dataset/json/covid-tracker.json) |
>|      `area.*`     |          แจ้งเตือนพื้นที่ตามคำประกาศ          | [Covid19.th-Stat](https://covid19.th-stat.com/) |          [area.xlsx](https://github.com/pluz85/Covid19TH-DailyData/raw/master/dataset/xlsx/area.xlsx)          |          [area.csv](https://github.com/pluz85/Covid19TH-DailyData/raw/master/dataset/csv/area.csv)          |          [area.json](https://github.com/pluz85/Covid19TH-DailyData/raw/master/dataset/json/area.json)          |
>|     `cases.*`     |               ข้อมูลแต่ละเคส               | [Covid19.th-Stat](https://covid19.th-stat.com/) |         [cases.xlsx](https://github.com/pluz85/Covid19TH-DailyData/raw/master/dataset/xlsx/cases.xlsx)         |         [cases.csv](https://github.com/pluz85/Covid19TH-DailyData/raw/master/dataset/csv/cases.csv)         |         [cases.json](https://github.com/pluz85/Covid19TH-DailyData/raw/master/dataset/json/cases.json)         |
>|    `timeline.*`   | ข้อมูลสรุปตามช่วงเวลา (เริ่มตั้งแต่วันที่ 01/01/20) | [Covid19.th-Stat](https://covid19.th-stat.com/) |      [timeline.xlsx](https://github.com/pluz85/Covid19TH-DailyData/raw/master/dataset/xlsx/timeline.xlsx)      |      [timeline.csv](https://github.com/pluz85/Covid19TH-DailyData/raw/master/dataset/csv/timeline.csv)      |      [timeline.json](https://github.com/pluz85/Covid19TH-DailyData/raw/master/dataset/json/timeline.json)      |
>|    `Data-Gov.*`   | ข้อมูลจาก Data.go.th  | [Data.go.th](https://data.go.th/dataset/covid-19-daily) |      [Data-Gov.xlsx](https://github.com/pluz85/Covid19TH-DailyData/raw/master/dataset/xlsx/Data-Gov.xlsx)                   |      [Data-Gov.csv](https://github.com/pluz85/Covid19TH-DailyData/raw/master/dataset/csv/Data-Gov.csv)      |      [Data-Gov.json](https://github.com/pluz85/Covid19TH-DailyData/raw/master/dataset/json/Data-Gov.json)      |


### 📦 หรือสามารถ Download รวมทุกไฟล์เพื่อความสะดวก [dataset.zip](https://github.com/pluz85/Covid19TH-DailyData/raw/master/dataset.zip)


## ตัวอย่างข้อมูล 💽

>   `covid-tracker.*`


```python

+----+-----------+------------------+-----------------+---------+---------+-------+----------+---------------+--------+-----------------+-----------------------------------------------------------------------------------------+--------------------------------------------+------+
|    | status    | date             | placename       |     lat |     lng |   age | gender   | nationality   | from   | patientstatus   | note                                                                                    | source                                     |   id |
+====+===========+==================+=================+=========+=========+=======+==========+===============+========+=================+=========================================================================================+============================================+======+
|  0 | confirmed | 2020-01-13 17:30 | สนามบินสุวรรณภูมิ   | 13.69   | 100.75  |    61 | female   | Chinese       | China  | recovered       | (เคสที่ 1) เดินทางมาจากอู่ฮั่น                                                                 | https://www.bbc.com/thai/thailand-51701394 |    0 |
+----+-----------+------------------+-----------------+---------+---------+-------+----------+---------------+--------+-----------------+-----------------------------------------------------------------------------------------+--------------------------------------------+------+
|  1 | confirmed | 2020-01-17 17:30 | สนามบินสุวรรณภูมิ   | 13.69   | 100.745 |    74 | female   | Chinese       | China  | recovered       | (เคสที่ 2) เดินทางมาจากอู่ฮั่น                                                                 | https://www.bbc.com/thai/thailand-51701394 |    1 |
+----+-----------+------------------+-----------------+---------+---------+-------+----------+---------------+--------+-----------------+-----------------------------------------------------------------------------------------+--------------------------------------------+------+
|  2 | confirmed | 2020-01-22 17:30 | โรงพยาบาลนครปฐม | 13.8216 | 100.066 |    73 | female   | Thai          | China  | recovered       | (เคสที่ 3) เดินทางกลับจากไปเที่ยวอู่ฮั่น                                                          | https://www.bbc.com/thai/thailand-51701394 |    2 |
+----+-----------+------------------+-----------------+---------+---------+-------+----------+---------------+--------+-----------------+-----------------------------------------------------------------------------------------+--------------------------------------------+------+
|  3 | confirmed | 2020-01-22 17:30 | สนามบินสุวรรณภูมิ   | 13.688  | 100.745 |    68 | male     | Chinese       | China  | recovered       | (เคสที่ 4) เดินทางมาจากอู่ฮั่น ตรวจพบจากการคัดกรองที่สนามบินสุวรรณภูมิ รักษาหายและเดินทางกลับประเทศแล้ว   | https://www.bbc.com/thai/thailand-51701394 |    3 |
+----+-----------+------------------+-----------------+---------+---------+-------+----------+---------------+--------+-----------------+-----------------------------------------------------------------------------------------+--------------------------------------------+------+
|  4 | confirmed | 2020-01-24 17:30 | โรงพยาบาลราชวิถี  | 13.7651 | 100.536 |    33 | female   | Chinese       | China  | recovered       | (เคสที่ 6) เป็นภรรยาของผู้ป่วยรายที่ 4 ซึ่งเป็นนักท่องเที่ยวชาวจีนอายุ 68 ปี รักษาหายและเดินทางกลับประเทศแล้ว | https://www.bbc.com/thai/thailand-51701394 |    4 |
+----+-----------+------------------+-----------------+---------+---------+-------+----------+---------------+--------+-----------------+-----------------------------------------------------------------------------------------+--------------------------------------------+------+
```
--------------------------------------

>   `area.*`

```python

+----+-------------------------------+---------------------+----------+-----------------------------------------------------------------------------------------------------------------------+-------------+--------------------------------------------+------------+--------------+---------------------+
|    | Date                          | Time                | Detail   | Location                                                                                                              | Recommend   | AnnounceBy                                 | Province   | ProvinceEn   | Update              |
+====+===============================+=====================+==========+=======================================================================================================================+=============+============================================+============+==============+=====================+
|  0 | 27 มีนาคม - 10 เมษายน 2563     |                     |          | ซอยบางลา ต.ป่าตอง อ.กะทู้                                                                                                |             | สำนักงานสาธารณสุขจังหวัดภูเก็ต 27 มีนาคม 2563     | ภูเก็ต       | Phuket       | 2020-04-08 11:58:58 |
+----+-------------------------------+---------------------+----------+-----------------------------------------------------------------------------------------------------------------------+-------------+--------------------------------------------+------------+--------------+---------------------+
|  1 | 29 มีนาคม 2563                 | 07.55 น.            |          | ผู้โดยสารสายการบินนกแอร์ เที่ยวบินที่ DD7103 เส้นทางหาดใหญ่ - ดอนเมือง เลขที่นั่ง 34A (ติดตามผู้สัมผัสใกล้ชิด 2 แถวหน้า-หลังครบแล้ว เว้นที่นั่ง 34A) |             | สำนักงานสาธารณสุขจังหวัดสงขลา  4 เมษายน 2563   | สงขลา      | Songkhla     | 2020-04-08 06:37:16 |
+----+-------------------------------+---------------------+----------+-----------------------------------------------------------------------------------------------------------------------+-------------+--------------------------------------------+------------+--------------+---------------------+
|  2 | 29 มีนาคม 2563 , 30 มีนาคม 2563 | 12.34 น. , 06.00 น. |          | ผู้โดยสารสายการบินไทย เที่ยวบิน TG911 เส้นทาง ประเทศอังกฤษ - สุวรรณภูมิ เลขที่นั่ง 45K 44H 44K 45H                                   |             | สำนักงานสาธารณสุขจังหวัดปราจีนนบุรี 4 เมษายน 2563 | ปราจีนบุรี    | Prachinburi  | 2020-04-08 06:11:43 |
+----+-------------------------------+---------------------+----------+-----------------------------------------------------------------------------------------------------------------------+-------------+--------------------------------------------+------------+--------------+---------------------+
|  3 | 28-29 มีนาคม 2563              | 09.25 น. , 15.51 น. |          | ผู้โดยสารสายการบินไทย เที่ยวบิน TG917 เส้นทาง สหราชอาณาจักร (ลอนดอนฮีทโธรว์) - สุวรรณภูมิ ระบุที่นั่งไม่ได้ 2 ที่นั่ง                         |             | สำนักงานสาธารณสุขจังหวัดนนทบุรี 2 เมษายน 2563    | นนทบุรี      | Nonthaburi   | 2020-04-03 13:50:21 |
+----+-------------------------------+---------------------+----------+-----------------------------------------------------------------------------------------------------------------------+-------------+--------------------------------------------+------------+--------------+---------------------+
|  4 | 27-28 มีนาคม 2563              | 09.25 น. , 15.52 น. |          | ผู้โดยสารสายการบินไทย เที่ยวบิน TG917 เส้นทาง สหราชอาณาจักร (ลอนดอนฮีทโธรว์) - สุวรรณภูมิ ที่นั่ง 4D                                   |             | สำนักงานสาธารณสุขจังหวัดนนทบุรี 2 เมษายน 2563    | นนทบุรี      | Nonthaburi   | 2020-04-03 13:47:54 |
+----+-------------------------------+---------------------+----------+-----------------------------------------------------------------------------------------------------------------------+-------------+--------------------------------------------+------------+--------------+---------------------+

```
--------------------------------------

>   `cases.*`

```python

+----+---------------------+------+-------+----------+------------+----------+------------+------------+--------------+------------+--------------+----------+
|    | ConfirmDate         |   No |   Age | Gender   | GenderEn   | Nation   | NationEn   | Province   |   ProvinceId | District   | ProvinceEn   | Detail   |
+====+=====================+======+=======+==========+============+==========+============+============+==============+============+==============+==========+
|  0 | 2020-04-10 00:00:00 | 2473 |     0 | หญิง      | Female     | จีน       | Chinese    | ภูเก็ต       |           42 |            | Phuket       |          |
+----+---------------------+------+-------+----------+------------+----------+------------+------------+--------------+------------+--------------+----------+
|  1 | 2020-04-10 00:00:00 | 2472 |     0 | หญิง      | Female     | จีน       | Chinese    | ภูเก็ต       |           42 |            | Phuket       |          |
+----+---------------------+------+-------+----------+------------+----------+------------+------------+--------------+------------+--------------+----------+
|  2 | 2020-04-10 00:00:00 | 2471 |     0 | หญิง      | Female     | จีน       | Chinese    | ภูเก็ต       |           42 |            | Phuket       |          |
+----+---------------------+------+-------+----------+------------+----------+------------+------------+--------------+------------+--------------+----------+
|  3 | 2020-04-10 00:00:00 | 2470 |     0 | หญิง      | Female     | จีน       | Chinese    | ภูเก็ต       |           42 |            | Phuket       |          |
+----+---------------------+------+-------+----------+------------+----------+------------+------------+--------------+------------+--------------+----------+
|  4 | 2020-04-10 00:00:00 | 2469 |    47 | ชาย      | Male       | ไทย      | Thai       | นนทบุรี      |           24 |            | Nonthaburi   |          |
+----+---------------------+------+-------+----------+------------+----------+------------+------------+--------------+------------+--------------+----------+
```
--------------------------------------

>   `timeline.*`

```python

+----+------------+----------------+----------------+-------------------+-------------+-------------+-------------+----------------+----------+
|    | Date       |   NewConfirmed |   NewRecovered |   NewHospitalized |   NewDeaths |   Confirmed |   Recovered |   Hospitalized |   Deaths |
+====+============+================+================+===================+=============+=============+=============+================+==========+
|  0 | 01/01/2020 |              0 |              0 |                 0 |           0 |           0 |           0 |              0 |        0 |
+----+------------+----------------+----------------+-------------------+-------------+-------------+-------------+----------------+----------+
|  1 | 01/02/2020 |              0 |              0 |                 0 |           0 |           0 |           0 |              0 |        0 |
+----+------------+----------------+----------------+-------------------+-------------+-------------+-------------+----------------+----------+
|  2 | 01/03/2020 |              0 |              0 |                 0 |           0 |           0 |           0 |              0 |        0 |
+----+------------+----------------+----------------+-------------------+-------------+-------------+-------------+----------------+----------+
|  3 | 01/04/2020 |              0 |              0 |                 0 |           0 |           0 |           0 |              0 |        0 |
+----+------------+----------------+----------------+-------------------+-------------+-------------+-------------+----------------+----------+
|  4 | 01/05/2020 |              0 |              0 |                 0 |           0 |           0 |           0 |              0 |        0 |
+----+------------+----------------+----------------+-------------------+-------------+-------------+-------------+----------------+----------+
```

>   `Data-Gov.*`

```python

+------+-------+-------+---------------+-------------------------+---------------------+---------------------+---------------------+---------------------+----------------------------------------------+
|   no |   age | sex   | nationality   | province_of_isolation   | notification_date   | announce_date       | province_of_onset   | district_of_onset   | quarantine                                   |
+======+=======+=======+===============+=========================+=====================+=====================+=====================+=====================+==============================================+
| 4441 |    54 | หญิง  | Thailand      | กทม                     | 2020-12-22 00:00:00 | 2020-12-21 00:00:00 | กทม                 | บางกะปิ             | สัมผัสใกล้ชิดกับผู้ป่วยยืนยันรายก่อนหน้านี้  |
+------+-------+-------+---------------+-------------------------+---------------------+---------------------+---------------------+---------------------+----------------------------------------------+
| 4442 |    66 | หญิง  | Thailand      | กทม                     | 2020-12-22 00:00:00 | 2020-12-21 00:00:00 | กทม                 | ดอนเมือง            | สัมผัสใกล้ชิดกับผู้ป่วยยืนยันรายก่อนหน้านี้  |
+------+-------+-------+---------------+-------------------------+---------------------+---------------------+---------------------+---------------------+----------------------------------------------+
| 4443 |    41 | หญิง  | Russia        | กทม                     | 2020-12-22 00:00:00 | 2020-12-21 00:00:00 | กทม                 | บางรัก              | ผู้ที่เดินทางมาจากต่างประเทศ และเข้า ASQ/ALQ |
+------+-------+-------+---------------+-------------------------+---------------------+---------------------+---------------------+---------------------+----------------------------------------------+
| 4444 |    52 | หญิง  | Thailand      | กทม                     | 2020-12-22 00:00:00 | 2020-12-21 00:00:00 | สมุทรสาคร           | เมือง               | Cluster ตลาดกลางกุ้ง สมุทรสาคร               |
+------+-------+-------+---------------+-------------------------+---------------------+---------------------+---------------------+---------------------+----------------------------------------------+
| 4445 |    28 | ชาย   | China         | กทม                     | 2020-12-22 00:00:00 | 2020-12-21 00:00:00 | กทม                 | คลองเตย             | อื่นๆ                                        |
+------+-------+-------+---------------+-------------------------+---------------------+---------------------+---------------------+---------------------+----------------------------------------------+


```

## Installation

>   - Clone the repository `git clone https://github.com/pluz85/Covid19TH-DailyData.git`

>   - Run `pip install -r requirements.txt`

## Usage

```python
python Covid19_TH_dailyData.py
```
