import re

# 초성, 중성, 종성 리스트
CHOSEONG = ['g', 'gg', 'n', 'd', 'dd', 'r', 'm', 'b', 'bb', 's', 'ss', '', 'j', 'jj', 'ch', 'k', 't', 'p', 'h']
JUNGSEONG = ['a', 'ae', 'ya', 'yae', 'eo', 'e', 'yeo', 'ye', 'o', 'wa', 'wae', 'oe', 'yo', 'u', 'wo', 'we', 'wi', 'yu', 'eu', 'ui', 'i']
JONGSEONG = ['', 'g', 'gg', 'gs', 'n', 'nj', 'nh', 'd', 'l', 'lg', 'lm', 'lb', 'ls', 'lt', 'lp', 'lh', 'm', 'b', 'bs', 's', 'ss', 'ng', 'j', 'ch', 'k', 't', 'p', 'h']

# 복합 자음 변환 규칙
COMPLEX_CONSONANTS = {
    'ㄳ': 'gs', 'ㄵ': 'nj', 'ㄶ': 'nh', 'ㄺ': 'lg', 'ㄻ': 'lm', 'ㄼ': 'lb',
    'ㄽ': 'ls', 'ㄾ': 'lt', 'ㄿ': 'lp', 'ㅀ': 'lh', 'ㅄ': 'bs'
}

# 받침 발음 규칙
CONSONANT_FINAL = {
    'ㄱ': 'k', 'ㄲ': 'k', 'ㄳ': 'k', 'ㄴ': 'n', 'ㄵ': 'n', 'ㄶ': 'n', 'ㄷ': 't',
    'ㄹ': 'l', 'ㄺ': 'k', 'ㄻ': 'm', 'ㄼ': 'l', 'ㄽ': 'l', 'ㄾ': 'l', 'ㄿ': 'p',
    'ㅀ': 'l', 'ㅁ': 'm', 'ㅂ': 'p', 'ㅄ': 'p', 'ㅅ': 't', 'ㅆ': 't', 'ㅇ': 'ng',
    'ㅈ': 't', 'ㅊ': 't', 'ㅋ': 'k', 'ㅌ': 't', 'ㅍ': 'p', 'ㅎ': 't'
}

# 단일 자음/모음 변환 규칙
SINGLE_JAMO = {
    'ㄱ': 'g', 'ㄲ': 'gg', 'ㄴ': 'n', 'ㄷ': 'd', 'ㄸ': 'dd', 'ㄹ': 'r', 'ㅁ': 'm', 'ㅂ': 'b', 
    'ㅃ': 'bb', 'ㅅ': 's', 'ㅆ': 'ss', 'ㅇ': '', 'ㅈ': 'j', 'ㅉ': 'jj', 'ㅊ': 'ch', 'ㅋ': 'k', 
    'ㅌ': 't', 'ㅍ': 'p', 'ㅎ': 'h', 'ㅏ': 'a', 'ㅐ': 'ae', 'ㅑ': 'ya', 'ㅒ': 'yae', 'ㅓ': 'eo', 
    'ㅔ': 'e', 'ㅕ': 'yeo', 'ㅖ': 'ye', 'ㅗ': 'o', 'ㅘ': 'wa', 'ㅙ': 'wae', 'ㅚ': 'oe', 
    'ㅛ': 'yo', 'ㅜ': 'u', 'ㅝ': 'wo', 'ㅞ': 'we', 'ㅟ': 'wi', 'ㅠ': 'yu', 'ㅡ': 'eu', 'ㅢ': 'ui', 'ㅣ': 'i'
}

def decompose(char):
    if '가' <= char <= '힣':
        char_code = ord(char) - ord('가')
        jong = char_code % 28
        jung = ((char_code - jong) // 28) % 21
        cho = (char_code - jong) // 28 // 21
        return (CHOSEONG[cho], JUNGSEONG[jung], JONGSEONG[jong])
    else:
        return (char, '', '')

def romanize_syllable(char, next_char=None):
    cho, jung, jong = decompose(char)
    
    result = cho + jung
    
    if jong:
        if next_char and '가' <= next_char <= '힣':
            next_cho, _, _ = decompose(next_char)
            if next_cho == '':
                result += CONSONANT_FINAL.get(jong, jong)
            else:
                result += jong
        else:
            result += CONSONANT_FINAL.get(jong, jong)
    
    # 'ㄹ' 받침 뒤 'ㄴ', 'ㄹ' 초성 규칙
    if jong == 'l' and next_char and '가' <= next_char <= '힣':
        next_cho, _, _ = decompose(next_char)
        if next_cho in ['n', 'r']:
            result = result[:-1] + 'll'
    
    return result

def romanize_text(text):
    result = []
    for i, char in enumerate(text):
        if '가' <= char <= '힣':
            next_char = text[i+1] if i+1 < len(text) else None
            result.append(romanize_syllable(char, next_char))
        elif char in SINGLE_JAMO:
            result.append(SINGLE_JAMO[char])
        else:
            result.append(char)
    return ''.join(result)