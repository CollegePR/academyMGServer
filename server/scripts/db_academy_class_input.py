from academyMGS.models import *

classList = ["WINDOWS", "HWP", "POWER POINT", "EXCEL", "ACCESS", "라즈베리파이", "아두이노", "스크래치", "파이썬", "비쥬얼베이직", "C언어",
             "C++", "JAVA", "C#", "자료구조론", "ITQ", "GTQ", "ATC기술자격", "3DS MAX기술자격", "워드프로세서", "컴퓨터활용능력", "정보처리기능사",
             "정보처기기운용기능사", "그래픽스운용기능사", "웹디자인기능사", "인터넷정보관리사""ILLUSTARATOR", "PHOTOSHOP", "포트폴리오", "FLASH",
             "DREAMWEAVER", "PREMIERE", "AFTER EFFECT", "AUTO CAD", "3DS MAX", "스케치업", "라이노", "어플리케이션 제작", "프로그램 제작",
             "SYSTEM 구축", "NETWORKING", "HACKING SOLUTION", "경시부문/공모부문", "전국정보경시대회", "영재교육원 선발대비", "입시지도"]


def run(*args):
    for className in classList:
        academyclass = AcademyClass(
            name=className,
        )
        academyclass.save()
