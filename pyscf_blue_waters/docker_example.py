#!/usr/bin/env python3
# Docker can be used without compiling, but only when submitting.
import sys
nm=sys.argv[1]

print("""#!/bin/bash
#PBS -l nodes=1:ppn=16:xe
#PBS -l walltime=12:30:00
#PBS -A bahu
#PBS -N %s
#PBS -e \$PBS_JOBID.err
#PBS -o \$PBS_JOBID.out
#PBS -m bea
#PBS -M lkwagner@illinois.edu
#PBS -l gres=shifter
#PBS -q normal
#PBS -v UDI=lkwagner/pyscf:latest

# To add certain modules that you do not have added via ~/.modules
. /opt/modules/default/init/bash

cd $PBS_O_WORKDIR
export CRAY_ROOTFS=UDI
export PYTHONPATH=/pyscf
export OMP_NUM_THREADS=16
aprun -N 1 -n 1 -d 16 -b -- /usr/local/bin/python  %s > %s.out
"""%(nm,nm,nm))
