echo "ls > sample.txt result:"
echo "sample text from stdin" > sample.txt

echo "ls | ./test_stdio.py result:"
ls | ./test_stdio.py argument#1 argument#2

echo "cat sample.txt | ./test_stdio.py result:"
cat sample.txt | ./test_stdio.py argument#1 argument#2

echo "./test_stdio.py <<< Test stdio result:"
./test_stdio.py argument#1 argument#2 <<< "Test stdio"

echo "./test_stdio.py < sample.txt result:"
./test_stdio.py argument#1 argument#2 < sample.txt

echo "./test_stdio.py < /dev/null  (NULL test) result"
./test_stdio.py argument#1 argument#2 < /dev/null

