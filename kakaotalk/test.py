# -*- coding: utf-8 -*-
from kakaotalk import kakaotalk as kakao

kakao.duuid = ''
kakao.sKey = ''
kakao.user_id = ''

chatId = ''

s = kakao.start()
suc = kakao.write(s, chatId, "(하트)")
