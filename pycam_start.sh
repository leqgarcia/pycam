
#!c:/bin/csh

####################################
#   APCT Scripting                 #
####################################


#echo "params"
#set
#echo "params"




# TO DO: Setup version support below $PYCAM_ROOT

set PYCAM_VERSION = ""


set PYCAM_ROOT=X:/genesis/sys/scripts/pycam/$PYCAM_VERSION/

cd ${PYCAM_ROOT}

python ${PYCAM_ROOT}/main.py


# PAUSE "   SCRIPT DONE     "

