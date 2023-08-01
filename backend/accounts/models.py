from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager  # AbstractUser 호출
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_field):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        if not password:
            raise ValueError('User must have a password.')

        user = self.model(
            email=self.normalize_email(email), **extra_field)
        user.set_password(password)
        user.save(using=self.db)
        return user


'''
구글 회원가입 시 요구하는 값 참고
1. 성(선택사항)/이름 -> validation 없음
2. 생일 (연도/월/일) -> 연도/일 validation 존재 + 월은 선택 + 해당 연도 + 월에 존재하는 일만 입력가능 + KST 07월 27일 16시 기준 26일 까지 등록 불가
3. 성별 (여성/남성/공개안함/사용자 지정) -> 사용자 지정 선택 시 성별이 무엇인지 입력 필드 + 나를 지칭할 떄 사용할 대명사 (여성/남성/기타) <- 사용자 지정 제외
4. 이메일(추천 가능) <- 이 부분은 실제 구글이 아니기 떄문에 제외 하고 입력 값을 입력 예정
5. 비밀번호 
6. 복구 이메일 추가 (건너뛰기 가능) <- 배제
7. 전화번호 (원칙상 국가 번호 + 핸드폰 번호) <- 한국 한정으로 변경하여 010-xxxx-xxxx 로 기준 변경
'''
# AbstractUser를 상속받아 구현. 기본 제공 값 중 일부 수정 필요 값 및 추가 필요 값 추가
class User(AbstractUser):
    GENDER_CHOICES = (
        ('FE', '여성'),
        ('MA', '남성'),
        ('NA', '공개안함'),
    )

    phoneNumberRegex = RegexValidator(regex=r"^010-?(\d{4})-?(\d{4})$")

    phone = models.CharField(validators=[phoneNumberRegex], max_length=20, unique=True, verbose_name='핸드폰 번호')
    last_name = models.CharField(max_length=30, verbose_name='이름')
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='NA', verbose_name='성별')
    birth_day = models.DateField(auto_now=False, verbose_name='생년월일')
    email = models.EmailField(unique=True, verbose_name='이메일')
    username = models.CharField(max_length=50, unique=False, null=True, verbose_name='유저 이름')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name']

    class Meta:
        db_table = 'user'

    def __str__(self):
        return "{}".format(self.email)