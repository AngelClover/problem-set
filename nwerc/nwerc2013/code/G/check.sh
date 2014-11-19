PROC=$0
TEST_PATH=../../problemset/problems/Grachten/testcases/
for i in `ls $TEST_PATH*.in ` 
do
    j=${i%.*}
    l=${j##*/}
    echo $i,$j,$l
    ./G.py <$i >$l.tmp
    diff $l.tmp $j.out
    if test $? -eq 1
    then
        echo -e "$j. \e[0;31;1merror\e[0m"
    else
        echo -e "$j. \e[0;32;1mPASSED\e[0m"
    fi
done
