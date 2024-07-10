# rotten-korean-romanizer
Turn your pristine Korean text into a mangled mess of Roman letters! This half-baked romanization tool is perfect for those who want their Korean to be barely recognizable. 

⚠️ Warning: May cause linguistic indigestion and confused looks from actual Korean speakers. Use at your own risk! ⚠️

## Installation

```
pip install rotten-korean-romanizer
```

## Usage

Here's a simple example of how to use the rotten_korean_romanizer:

```python
from rotten_korean_romanizer import romanize_text

# Romanize a Korean word
print(romanize_text("안녕하세요"))  # Output: annyeonghaseyo

# Romanize a sentence
print(romanize_text("한글을 로마자로 변환합니다"))  # Output: hangeuleul romajaro byeonhwanhabnida

# Romanize Korean text containing Hangul, emoji, and English characters
print(romanize_text("안녕하세요, 세계!🌍, Hello, world!")) # annyeonghaseyo, segye!🌍, Hello, world!
```

