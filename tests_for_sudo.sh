

for testfile in `ls *.csv`; 
do
	result=`python main.py $testfile |grep -i 'now numbers is 81'|wc -l`
	if [ $result -ge 1 ]; then 
		echo "pass $testfile"
	else
		echo "not pass $testfile"
	fi
done