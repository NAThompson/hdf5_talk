FROM ubuntu:15.04
ENV HOME /root
RUN apt-get update
RUN apt-get -yq install gcc build-essential subversion zlib1g-dev

RUN apt-get install -y python3-dev    
RUN apt-get install -y python3-pip
RUN apt-get install -y git
RUN pip3 install Cython
RUN pip3 install numpy
RUN pip3 install six

# At the time of this writing, 1.9.178 is the only version that works with h5py:
ADD hdf5-1.9.178-swmr_chksum5.tar.gz /root
RUN cd ; cd hdf5-1.9.178-swmr_chksum5; ./configure --prefix=/usr/
RUN cd ; cd hdf5-1.9.178-swmr_chksum5; make -j8 && make install


RUN git clone https://github.com/h5py/h5py.git /root/h5py
RUN cd /root/h5py; git checkout 2.5.0rc1
RUN cd /root/h5py; python3 setup.py configure --hdf5=/root/hdf5-1.9.222-swmr0
RUN cd /root/h5py; python3 setup.py build
RUN cd /root/h5py; python3 setup.py install

CMD python3 -c "import h5py"