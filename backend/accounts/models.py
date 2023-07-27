from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser  # AbstractUser 호출
from django.core.validators import RegexValidator


'''
구글 회원가입 시 요구하는 값 참고
1. 성(선택사항)/이름 -> validation 없음
2. 생일 (연도/월/일) -> 연도/일 validation 존재 + 월은 선택 + 해당 연도 + 월에 존재하는 일만 입력가능 + KST 07월 27일 16시 기준 26일 까지 등록 불가
3. 성별 (여성/남성/공개안함/사용자 지정) -> 사용자 지정 선택 시 성별이 무엇인지 입력 필드 + 나를 지칭할 떄 사용할 대명사 (여성/남성/기타)
4. 이메일(추천 가능) <- 이 부분은 실제 구글이 아니기 떄문에 제외 하고 입력 값을 입력 예정
5. 비밀번호 
6. 복구 이메일 추가 (건너뛰기 가능)
7. 전화번호 (건너뛰기 가능)+(원칙상 국가 번호 + 핸드폰 번호) <- 한국 한정으로 변경하여 010-xxxx-xxxx 로 기준 변경
'''
class User(AbstractUser):
    phoneNumberRegex = RegexValidator(regex=r"^010-?(\d{4})-?(\d{4})$")
    phone = models.CharField(validators=[phoneNumberRegex], max_length=20)
