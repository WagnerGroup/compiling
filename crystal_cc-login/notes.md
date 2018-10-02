# Getting the object files.

It's on Box under `Weekly meetings with Lucas/Useful files/crystal/crystal17_1.0.2`

# Clarified compiling instructions from this folder

Specific instructions to make Pcrystal:

0.- Load the modules needed for crystal 

    module unload [any other intel libraries]
    module load openmpi/1.4-gcc+ifort
    module load intel/17.0

1.- Make the crystal root directory (let us say CRYSTAL17) and copy there the
file containing the pre-compiled objects modules 
(e.g. crystal17_v1_0_2_Linux-ifort17_emt64_Pdistrib.tar.gz). The label after 
crystal17_v1_0_2 in the file name identifies which version of the FORTRAN 
compiler have to be used and the architecture for which object files
have been generated.

CRYSTAL17 has been tested for Intel Fortran compiler (ifort XE)14

    mkdir CRYSTAL17

    cp crystal17_v1_0_2_Linux-ifort17_emt64_Pdistrib.tar.gz CRYSTAL17/.

    cd CRYSTAL17

2.- Untar and uncompress this file

    tar -zxvf crystal17_v1_0_2_Linux-ifort17_emt64_Pdistrib.tar.gz

3.- Go to the build directory

    cd build

4.- Defining the mpif90 PATH by first:

    cd Xmakes

then edit the inc file. Let us take the Linux-ifort17_XE_emt64.inc file
as an example.
This file has the following instructions

    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #
    # For Linux systems using Intel Fortran XE
    #


    MPIBIN  =
    F90     = $(MPIBIN)/mpif90
    F90FLAGS = -O2 -align -static-intel
    F90MXMFL = -O2 -align -static-intel
    F90FIXED = -FI
    F90FREE  = -FR

    LD      = $(F90)
    PLD     = $(MPIBIN)/mpif90
    LDFLAGS = $(F90FLAGS)
    LDLIBS  =

    SAVEMOD = -module $(MODDIR)
    INCMOD  = -I$(MODDIR)

    MXMB    = $(OBJDIR)/libmxm.o

    # MPI harness
    HARNESS = $(MPI)

    MPP_DEFINES=-DMPP_AVAIL
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The user should specify the variable MPIBIN which is the local directory
where MPI has been installed.
Using module on campus cluster means it will be `/usr/local/openmpi-1.4-intel/bin`

5.- Return to the build directory

    cd ..

6.- type

    # This makes the serial components.
    make
    # This makes the parallel components.
    make parallel`


7.- the executable crystal, properties, Pcrystal and Pproperties will be written in `~/CRYSTAL17/bin/Linux-ifort17_XE_emt64/v1_0_2.`

# Running Pcrystal, etc.

    module load openmpi/1.4-gcc+ifort
    cp my_crystal_input INPUT
    mpirun Pcrystal &> out

Note that Pcrystal puts all output into STDERR because fun.
