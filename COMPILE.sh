set -e
make -s -j8 clean

# one of the following
# ./configure -q --with-pydebug
# ./configure -q --with-ensurepip=install

# make -s -j8 regen-token
# make -s -j8 regen-pegen
# make -s -j8 regen-all
make -s -j8 all
# make -s -j8 regen-global-objects

./python -m ensurepip --default-pip
./python TESTING.py

# make -s -j8 regen-pegen regen-frozen
