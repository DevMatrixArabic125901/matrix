from sqlalchemy import Boolean, Column, String

from . import BASE, SESSION


class Locks(BASE):
    __tablename__ = "locks"
    chat_id = Column(String(14), primary_key=True)
    # Booleans are for "is this locked", _NOT_ "is this allowed"
    bots = Column(Boolean, default=False)
    commands = Column(Boolean, default=False)
    email = Column(Boolean, default=False)
    forward = Column(Boolean, default=False)
    url = Column(Boolean, default=False)

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)  # ensure string
        self.bots = False
        self.commands = False
        self.email = False
        self.forward = False
        self.url = False


Locks.__table__.create(checkfirst=True)


def init_locks(chat_id, reset=False):
    curr_restr = SESSION.query(Locks).get(str(chat_id))
    if reset:
        SESSION.delete(curr_restr)
        SESSION.flush()
    restr = Locks(str(chat_id))
    SESSION.add(restr)
    SESSION.commit()
    return restr









def update_lock(chat_id, lock_type, locked):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    if not curr_perm:
        curr_perm = init_locks(chat_id)
    if lock_type == "bots":
        curr_perm.bots = locked
    elif lock_type == "commands":
        curr_perm.commands = locked
    elif lock_type == "email":
        curr_perm.email = locked
    elif lock_type == "forward":
        curr_perm.forward = locked
    elif lock_type == "url":
        curr_perm.url = locked
    SESSION.add(curr_perm)
    SESSION.commit()


def is_locked(chat_id, lock_type):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    SESSION.close()
    if not curr_perm:
        return False
    if lock_type == "bots":
        return curr_perm.bots
    if lock_type == "commands":
        return curr_perm.commands
    if lock_type == "email":
        return curr_perm.email
    if lock_type == "forward":
        return curr_perm.forward
    if lock_type == "url":
        return curr_perm.url

matrixvois1 = "matrix/helpers/styles/Voic/ابو عباس لو تاكل خره.ogg"
matrixvois2 = "matrix/helpers/styles/Voic/استمر نحن معك.ogg"
matrixvois3 = "matrix/helpers/styles/Voic/افحط بوجه.ogg"
matrixvois4 = "matrix/helpers/styles/Voic/اكعد لا اسطرك سطره العباس.ogg"
matrixvois5 = "matrix/helpers/styles/Voic/اللهم لا شماته.ogg"
matrixvois6 = "matrix/helpers/styles/Voic/امرع دينه.ogg"
matrixvois7 = "matrix/helpers/styles/Voic/امشي بربوك.ogg"
matrixvois8 = "matrix/helpers/styles/Voic/انت اسكت انت اسكت.ogg"
matrixvois9 = "matrix/helpers/styles/Voic/انت سايق زربه.ogg"
matrixvois10 = "matrix/helpers/styles/Voic/اوني تشان.ogg"
matrixvois11 = "matrix/helpers/styles/Voic/برافو عليك استادي.ogg"
matrixvois12 = "matrix/helpers/styles/Voic/بلوك محترم.ogg"
matrixvois13 = "matrix/helpers/styles/Voic/بووم في منتصف الجبهة.ogg"
matrixvois14 = "matrix/helpers/styles/Voic/بيتش.ogg"
matrixvois15 = "matrix/helpers/styles/Voic/تخوني ؟.ogg"
matrixvois15 = "matrix/helpers/styles/Voic/تره متكدرلي.ogg"
matrixvois17 = "matrix/helpers/styles/Voic/تعبان اوي.ogg"
matrixvois18 = "matrix/helpers/styles/Voic/تكذب.ogg"
matrixvois19 = "matrix/helpers/styles/Voic/حسبي الله.ogg"
matrixvois20 = "matrix/helpers/styles/Voic/حشاش.ogg"
matrixvois21 = "matrix/helpers/styles/Voic/حقير.ogg"
matrixvois22 = "matrix/helpers/styles/Voic/خاص.ogg"
matrixvois23 = "matrix/helpers/styles/Voic/خاله ما تنامون.ogg"
matrixvois24 = "matrix/helpers/styles/Voic/خرب شرفي اذا ابقى بالعراق.ogg"
matrixvois25 = "matrix/helpers/styles/Voic/دكات الوكت الاغبر.ogg"
matrixvois26 = "matrix/helpers/styles/Voic/ررردح.ogg"
matrixvois27 = "matrix/helpers/styles/Voic/سلامن عليكم.ogg"
matrixvois28 = "matrix/helpers/styles/Voic/شعليك.ogg"
matrixvois29 = "matrix/helpers/styles/Voic/شكد شفت ناس مدودة.ogg"
matrixvois30 = "matrix/helpers/styles/Voic/شلون ،.ogg"
matrixvois31 = "matrix/helpers/styles/Voic/صح لنوم.ogg"
matrixvois32 = "matrix/helpers/styles/Voic/صمت.ogg"
matrixvois33 = "matrix/helpers/styles/Voic/ضحكة مصطفى الحجي.ogg"
matrixvois34 = "matrix/helpers/styles/Voic/طماطه.ogg"
matrixvois35 = "matrix/helpers/styles/Voic/طيح الله حضك.ogg"
matrixvois36 = "matrix/helpers/styles/Voic/فاك يوو.ogg"
matrixvois37 = "matrix/helpers/styles/Voic/فرحان.ogg"
matrixvois38 = "matrix/helpers/styles/Voic/لا تضل تضرط.ogg"
matrixvois39 = "matrix/helpers/styles/Voic/لا تقتل المتعه يا مسلم.ogg"
matrixvois40 = "matrix/helpers/styles/Voic/لا مستحيل.ogg"
matrixvois41 = "matrix/helpers/styles/Voic/لا والله شو عصبي.ogg"
matrixvois42 = "matrix/helpers/styles/Voic/لش.ogg"
matrixvois43 = "matrix/helpers/styles/Voic/لك اني شعليه.ogg"
matrixvois44 = "matrix/helpers/styles/Voic/ما اشرب.ogg"
matrixvois45 = "matrix/helpers/styles/Voic/مع الاسف.ogg"
matrixvois46 = "matrix/helpers/styles/Voic/مقتدى.ogg"
matrixvois47 = "matrix/helpers/styles/Voic/من رخصتكم.ogg"
matrixvois48 = "matrix/helpers/styles/Voic/منو انت.ogg"
matrixvois49 = "matrix/helpers/styles/Voic/منورني.ogg"
matrixvois50 = "matrix/helpers/styles/Voic/نتلاكه بالدور الثاني.ogg"
matrixvois51 = "matrix/helpers/styles/Voic/نستودعكم الله.ogg"
matrixvois52 = "matrix/helpers/styles/Voic/ها شنهي.ogg"
matrixvois53 = "matrix/helpers/styles/Voic/ههاي الافكار حطها.ogg"
matrixvois54 = "matrix/helpers/styles/Voic/وينهم.ogg"
matrixvois55 = "matrix/helpers/styles/Voic/يموتون جهالي.ogg"
matrixvois56 = "matrix/helpers/styles/Voic/اريد انام.ogg"
matrixvois57 = "matrix/helpers/styles/Voic/افتحك فتح.ogg"
matrixvois58 = "matrix/helpers/styles/Voic/اكل خره لدوخني.ogg"
matrixvois59 = "matrix/helpers/styles/Voic/السيد شنهو السيد.ogg"
matrixvois60 = "matrix/helpers/styles/Voic/زيج2.ogg"
matrixvois61 = "matrix/helpers/styles/Voic/زيج لهارون.ogg"
matrixvois62 = "matrix/helpers/styles/Voic/زيج الناصرية.ogg"
matrixvois63 = "matrix/helpers/styles/Voic/راقبو اطفالكم.ogg"
matrixvois64 = "matrix/helpers/styles/Voic/راح اموتن.ogg"
matrixvois65 = "matrix/helpers/styles/Voic/ذس اس مضرطة.ogg"
matrixvois66 = "matrix/helpers/styles/Voic/دروح سرسح منا.ogg"
matrixvois67 = "matrix/helpers/styles/Voic/خويه ما دكوم بيه.ogg"
matrixvois68 = "matrix/helpers/styles/Voic/خلصت تمسلت ديلة كافي انجب.ogg"
matrixvois69 = "matrix/helpers/styles/Voic/بعدك تخاف.ogg"
matrixvois70 = "matrix/helpers/styles/Voic/بسبوس.ogg"
matrixvois71 = "matrix/helpers/styles/Voic/اني بتيتة كحبة.ogg"
matrixvois72 = "matrix/helpers/styles/Voic/انعل ابوكم لابو اليلعب وياكم طوبة.ogg"
matrixvois73 = "matrix/helpers/styles/Voic/انت شدخلك.ogg"
matrixvois74 = "matrix/helpers/styles/Voic/انا ماشي بطلع.ogg"
matrixvois75 = "matrix/helpers/styles/Voic/امداك وامده الخلفتك.ogg"
matrixvois76 = "matrix/helpers/styles/Voic/امبيههههه.ogg"
matrixvois77 = "matrix/helpers/styles/Voic/هدي بيبي.ogg"
matrixvois78 = "matrix/helpers/styles/Voic/هاه صدك تحجي.ogg"
matrixvois79 = "matrix/helpers/styles/Voic/مو كتلك رجعني.ogg"
matrixvois80 = "matrix/helpers/styles/Voic/مامرجية منك هاية.ogg"
matrixvois81 = "matrix/helpers/styles/Voic/ليش هيجي.ogg"
matrixvois82 = "matrix/helpers/styles/Voic/كـــافـي.ogg"
matrixvois83 = "matrix/helpers/styles/Voic/كس اخت السيد.ogg"
matrixvois84 = "matrix/helpers/styles/Voic/شنو كواد ولك اني هنا.ogg"
matrixvois85 = "matrix/helpers/styles/Voic/شجلبت.ogg"
matrixvois86 = "matrix/helpers/styles/Voic/شبيك وجه الدبس.ogg"
matrixvois87 = "matrix/helpers/styles/Voic/سييييي.ogg"
matrixvois88 = "matrix/helpers/styles/Voic/زيجج1.ogg"
matrixvois89 = "matrix/helpers/styles/Voic/يموتون جهالي.ogg"
matrixvois90 = "matrix/helpers/styles/Voic/ياخي اسكت اسكت.ogg"
matrixvois91 = "matrix/helpers/styles/Voic/وينهم.ogg"
matrixvois92 = "matrix/helpers/styles/Voic/هيلو سامر وحود.ogg"
matrixvois93 = "matrix/helpers/styles/Voic/هو.ogg"
matrixvois94 = "matrix/helpers/styles/Voic/ههاي الافكار حطها.ogg"

def get_locks(chat_id):
    try:
        return SESSION.query(Locks).get(str(chat_id))
    finally:
        SESSION.close()