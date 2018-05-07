rm cmake_fei-1.0* -rf
cp cmake_fei cmake_fei-1.0 -r
tar zcvf cmake_fei-1.0.tar.gz cmake_fei-1.0
cp cmake_fei-1.0.tar.gz ~/rpmbuild/SOURCES/
rpmbuild -ba cmake_fei/packaging/cmake_fei.spec
rm cmake_fei-1.0* -rf

sudo rpm -Uvh ~/rpmbuild/RPMS/i386/cmake_fei-1.0-1.i386.rpm --force --nodeps
/usr/apps/com.mc.cmake_fei/bin/hello