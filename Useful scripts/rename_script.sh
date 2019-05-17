j=0;
for i in *.gt_data.txt;
do let j+=1;
if [ "$j" -lt "10" ];
then mv $i 00000$j.txt;
elif [ "$j" -lt "100" ];
then mv $i 0000$j.txt;
elif [ "$j" -lt "1000" ];
then mv $i 000$j.txt;
else mv $i 00$j.txt;
fi;
done
