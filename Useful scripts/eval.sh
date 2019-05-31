
for i in *.pth;
do #touch $i.txt
python3 ~/CourseWork/SSDCourse/eval.py --trained_model="$i" > $i.txt
done
