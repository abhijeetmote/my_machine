tm=`date +"%H%M"`
echo $tm
if [ $(($tm%100)) -eq 0 ];then
export DISPLAY=:0; /usr/bin/zenity --error --text="Please Drink Water\!" --title="Health Alert\!";
fi

if [ $tm -eq 1330 ];then
export DISPLAY=:0; /usr/bin/zenity --error --text="Its Lunch Time\!" --title="Health Alert\!";
fi

if [ $tm -eq 1445 ];then
export DISPLAY=:0; /usr/bin/zenity --error --text="Learn Something new\!" --title="Learn Alert\!";
fi

if [ $tm -eq 1600 ];then
export DISPLAY=:0; /usr/bin/zenity --error --text="Its Tea Time\!" --title="Health Alert\!";
fi


if [ $tm -eq 1800 ];then
export DISPLAY=:0; /usr/bin/zenity --error --text="Please log time and Update the tickets\!" --title="Work Alert\!";
fi

if [ $tm -eq 1830 ];then
export DISPLAY=:0; /usr/bin/zenity --error --text="Complete All tasks...\!" --title="Time to leave \!";
fi
