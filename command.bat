python3 -c "d=open('input.txt','rb').read(); open('input.txt','wb').write(d.lstrip(b'\xef\xbb\xbf'))"
python3 answer.py < input.txt