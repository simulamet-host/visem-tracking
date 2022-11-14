for i in 11 12 13 14 15 19 21 22 23 24 29 30 35 36 38 47 52 54 60 82
do
    mv /home/vajira/data/VISEM_original/visem-extracted-30s-excluding-selected-20/${i}_*.mp4 /home/vajira/data/VISEM_original/visem-extracted-30s-selected-20-videos
done

# Remove fist 30s videos

for i in 11 12 13 14 15 19 21 22 23 24 29 30 35 36 38 47 52 54 60 82
do
    rm -rf /home/vajira/data/VISEM_original/visem-extracted-30s-selected-20-videos/${i}_0_30.mp4
done
