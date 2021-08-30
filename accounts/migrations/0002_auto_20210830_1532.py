# Generated by Django 3.2.4 on 2021-08-30 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL([
            '''
            INSERT INTO accounts_nickname
            (part, content) VALUES 
                ('a', '행복한'),
                ('a', '홀가분한'),
                ('a', '사랑스러운'),
                ('a', '즐거운'),
                ('a', '자랑스러운'),
                ('a', '설레는'),
                ('a', '활기찬'),
                ('a', '뿌듯한'),
                ('a', '통쾌한'),
                ('a', '게으른'),
                ('a', '소심한'),
                ('a', '엉뚱한'),
                ('a', '심각한'),
                ('a', '솔직한'),
                ('a', '솔직한'),
                ('a', '느긋한'),
                ('a', '분노한'),
                ('a', '아찔한'),
                ('a', '정신없는'),
                ('a', '혼란스러운');
            ''',
            '''
            INSERT INTO accounts_nickname
            (part, content, emoji) VALUES
                ('n', '딸기', '🍓'),
                ('n', '키위', '🥝'),
                ('n', '포도', '🍇'),
                ('n', '복숭아', '🍑'),
                ('n', '레몬', '🍋'),
                ('n', '아보카도', '🥑'),
                ('n', '사과', '🍏'),
                ('n', '수박', '🍉'),
                ('n', '쿠키', '🍪');
            ''',
            '''
            INSERT INTO accounts_tag
                (tag_code, tag_text) VALUES
                (1, '분류 없음'),
                (2, '공부'),
                (3, '게임'),
                (4, '코딩'),
                (5, '문서 작업'),
                (6, '영상 제작'),
                (7, '디자인'),
                (8, '학생'),
                (9, '직장인'),
                (10, '프리랜서'),
                (11, '영상 시청'),
                (12, '웹 서핑')
            ''',
            '''
            INSERT INTO accounts_tag
            (tag_code, tag_text) VALUES
                (13, '멤브레인'),
                (14, '펜타그래프'),
                (15, '기계식 적축'),
                (16, '기계식 청축'),
                (17, '기계식 갈축'),
                (18, '기계식 흑축'),
                (19, '기계식 광출'),
                (20, '무접점 정전'),

                (21, '텐키'),
                (22, '텐키리스'),
                (23, '방수'),
                (24, '키스킨 제공'),
                (25, '키압 낮음'),
                (26, '키압 중간'),
                (27, '키압 높음'),
                (28, '무한동시입력'),
                (29, '폴링레이트 1000Hz'),
                (30, '비키스타일'),
                (31, '백라이트'),
                (32, '응답속도 1ms 이하'),
                (33, '아이솔레이션'),

                (34, '광마우스'),
                (35, '3버튼'),
                (36, '5버튼'),
                (37, '6버튼'),
                (38, '7버튼'),
                (39, 'DPI버튼'),
                (40, '일반 감도'),
                (41, '게이밍 감도'),
                (42, '고급 게이밍 감도'),
                (43, '무게추'),
                (44, 'DPI낮음'),
                (45, 'DPI일반'),
                (46, 'DPI높음'),

                (47, 'HERO 센서'),
                (48, 'PMW-3320 센서'),
                (49, 'ADSN-3050 센서'),
                (50, '델타제로센서'),
                (51, 'PAW-3519 센서'),
                (52, '옵티컬 센서'),

                (53, '인체공학적디자인'),
                (54, '유선'),
                (55, '블루투스'),
                (56, '무선 USB'),
                (57, '배터리'),
                (58, 'USB충전'),
                (59, '무선충전'),
                (60, '무소음/저소음'),

                (61, '멀티페어링'),
                (62, '안드로이드 호환'),
                (63, 'windows 호환'),
                (64, 'MacOSX 호환'),
                (65, '무게 무거움'),
                (66, '무게 적당함'),
                (67, '무게 가벼움');
            '''
        ])
    ]
