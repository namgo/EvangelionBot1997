# requires imagemagick
# also seems to freeze
export MAGICK_THREAD_LIMIT=4
for f in */
do
    cd $f
    for i in $(find | grep bmp)
    do
	convert $i -resize 480x360 "$(echo $i | cut -d'.' -f1)".png
	echo $i
	rm $i
    done
    cd ..
done
