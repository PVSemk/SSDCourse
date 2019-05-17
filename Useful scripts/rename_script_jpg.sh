j=0;
for i in *.jpg;
do let j+=1;
if [ "$j" -lt "10" ];
then mv $i 00000$j.jpg;
elif [ "$j" -lt "100" ];
then mv $i 0000$j.jpg;
elif [ "$j" -lt "1000" ];
then mv $i 000$j.jpg;
else mv $i 00$j.jpg;
fi;
done
