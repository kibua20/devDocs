#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

# Regular expression sample code for https://kibua20.tistory.com/199
string = 'The Regular Expresion !!! 123 @#! 한글'

# 소문자만, +는 1번 이상 반복
pattern = re.compile('[a-z]+')
print(pattern.findall(string))
# 결과: ['he', 'egular', 'xpresion']


# 소문자만, ?는 0번 또는 1번 이상 표시
pattern = re.compile('[a-z]?')
print(pattern.findall(string))
# 결과: ['', 'h', 'e', '', '', 'e', 'g', 'u', 'l', 'a', 'r', '', '', 'x', 'p', 'r', 'e', 's', 'i', 'o', 'n', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']


# 소문자만, *는 0번 또는 그 이상 표시
pattern = re.compile('[a-z]*')
print(pattern.findall(string))
# 결과: ['', 'he', '', '', 'egular', '', '', 'xpresion', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']


# 소문자, 대문자, 숫자, +는 1번 이상 반복
pattern = re.compile('[a-zA-Z0-1]+')
print(pattern.findall(string))
# 결과: ['The', 'Regular', 'Expresion', '1']


# 소문자, 대문자, 숫자, ?는 0번 또는 1번 이상 표시
pattern = re.compile('[a-zA-Z0-1]?')
print(pattern.findall(string))
# 결과: ['T', 'h', 'e', '', 'R', 'e', 'g', 'u', 'l', 'a', 'r', '', 'E', 'x', 'p', 'r', 'e', 's', 'i', 'o', 'n', '', '', '', '', '', '1', '', '', '', '', '', '', '', '', '', '']


# 소문자, 대문자, 숫자, *는 0번 또는 그 이상 표시
pattern = re.compile('[a-zA-Z0-1]*')
print(pattern.findall(string))
# 결과: ['The', '', 'Regular', '', 'Expresion', '', '', '', '', '', '1', '', '', '', '', '', '', '', '', '', '']


# 주민번호 뒷 번호를 *******로 치환
string = '090320-3212345'
# 기호 '-'와 0~9까지의 숫자 7개 반복의 패턴 정의
pattern = '-[0-9]{7}'
#  sub(정규표현식, 바꿀문자열, 입력문자열)
print ( re.sub(pattern, '-*******', string) )
# 결과: 090320-*******


#split 예제
pattern = re.compile(':')
print ( pattern.split('key:value') )
# 결과: ['key', 'value'] 


string = """Ross McFluff: 834.345.1254 155 Elm Street
Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way
Heather Albrecht: 548.326.4584 919 Park Place"""


entries = re.split("\n+", string)
print (entries)
# 결과: 개행 문자를 기준으로 분리한 문자열 4개의 list 
# ['Ross McFluff: 834.345.1254 155 Elm Street', 
# 'Ronald Heathmore: 892.345.3428 436 Finley Avenue', 
# 'Frank Burger: 925.541.7625 662 South Dogwood Way', 
# 'Heather Albrecht: 548.326.4584 919 Park Place']

# :와 ' ' 공백(space)을 패턴으로 4개의 list로 분리
result = [re.split(":? ", entry, maxsplit=4) for entry in entries]
print (result)
# 결과:  성, 이름, 전화번호, 우편번호, 거리명 list 저장됨
# [
#    ['Ross', 'McFluff', '834.345.1254', '155', 'Elm Street'], 
#    ['Ronald', 'Heathmore', '892.345.3428', '436', 'Finley Avenue'], 
#    ['Frank', 'Burger', '925.541.7625', '662', 'South Dogwood Way'], 
#    ['Heather', 'Albrecht', '548.326.4584', '919', 'Park Place']
# ]