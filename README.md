# step 1 - tagging


edit tagging.sh:

but before edit this file. for example:
opencv_annotation --annotations=/home/yakir/bottle/annotations/can.info --images=/home/yakir/bottle/images/positive/

explaintation:
-annotations=/home/yakir/bottle/annotations/can.info - where the boxes file will be saved
--images=/home/yakir/bottle/images/positive/ - the path to the positive folder of the imgs

after run ./tagging.sh

with the mouse you selcet the area of the objects, press 'c' to make it green and then press 'n' to the next img

in the end - ctrl+c

## mark negative folder

go to imgs/negative and put there all the negative imgs,
open bg.txt -> evry row is the name of img for exmple 0.png ... 1.png an so on.

## create sample

go to the annotation folder, and open creatSamples.sh for editing:

opencv_createsamples -info can.info -num 21 -w 50 -h 150 -vec can.vec

you need to write the name of the info file (the one that was created after tagging) and write the outpt name of the vec file.
you also need to set w (the widht of the object) and h (the height of the object).

then run ./createSamples.sh

## training

go to imgs/negative nd open training.sh for editing:

for example:
edit the relevant fields:
 
opencv_traincascade -data output -vec /home/yakir/bottle/annotations/can.vec -bg bg.txt -numPos 21 -numNeg 21 -mem 2048 -mode ALL -numStages 40 -w 50 -h 150 -featureType LBP 

then run ./training.sh

the output will be at output folder:

the file called cascade.xml


