for folder in $(du -sh good_data_* | sort -nr | head -n 5)
if [ -d $folder ]
then
    mv $folder best_data
fi