# Using Lucas's binary.

Get Lucas's binary from `/projects/sciteam/batr/crystal_lucas/bin/Linux-ifort14_XE_emt64/v1.0.2/Pcrystal`.

# Compiling from scratch.

Last verified on crystal17-1.0.2 on 07-02-2017.

Get the objects from Box/Weekly meetings with `lucas/Useful files/crystal[version]/*`

Unzip the version:

    tar xzf crystal17_v1_0_2_Linux-ifort14_emt64_Pdistrib.tar.gz

Open the makefile variables file:

    vi build/Xmakes/Linux-ifort14_XE_emt64.inc

Edit the file to look like this:

    # For Linux on clutwin intel64, using Intel Fortran Compiler

    MPIBIN  =   
    F90     = ftn                                # changes
    LD      = $(F90)
    PLD     = ftn                                # changes

    F90FLAGS = -O3 -align -i -cxxlib             # changes
    F90FIXED = -FI
    F90FREE  = -FR
    SAVEMOD = -module $(MODDIR)
    INCMOD  = -I$(MODDIR)
    LDFLAGS = #$(F90FLAGS)                       # changes
    LDLIBS  = -Lxcfun xcfun/libxcfun.a  #-lm     # changes
    #LDLIBS  =

    MXMB    = $(OBJDIR)/libmxm.o

    MACHINE_C=mach_linux

    CC = cc                                      #changes
    CFLAGS = -O2 -vec-report0 -Wall -diag-disable 177,279,383,869,981,1418,1419,1572 -DNDEBUG
    CXX = CC                                     #changes
    CXXFLAGS = $(CFLAGS) -fno-rtti -fno-exceptions

    # MPI harness
    HARNESS = $(MPI)

Move to the build and build. 

    cd build
    make          # For serial.
    make parallel # For parallel 

Executables are now in `../bin/Linux-ifort14_XE_emt64/v1.0.2/`
