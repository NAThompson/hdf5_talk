FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y libhdf5-dev
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-pip
RUN apt-get install -y hexedit
RUN pip3 install Cython
RUN pip3 install numpy
RUN pip3 install six
RUN pip3 install h5py
RUN apt-get install -y hdf5-tools
RUN apt-get install -y hdfview
RUN apt-get install -y emacs
