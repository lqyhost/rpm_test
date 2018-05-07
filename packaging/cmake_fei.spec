

#key word===========================================
Summary:This is first cmake spec package of xfei
Version:1.0
Name:cmake_fei
Release:1
Source:%{name}-%{version}.tar.gz
License:GPL
Packager:xfei
Group:Application
URL:www.baidu.com
#BuildArch: %{arm}
#spec main body======================================
%description
This is just a wonderful package

%prep

%setup -q

%build
cmake .
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
echo $RPM_BUILD_ROOT
#RPM_BUILD_ROOT is virtual build dir, %file will start based on it.
echo $RPM_BUILD_DIR
echo %{buildroot}
%make_install

%post

%postun
#/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT
make clean

#files will be started in RPM_BUILD_ROOT dir
%files
%defattr(-,root,root)
/usr/lib/libhello.so
/usr/include/hello/hello.h
/usr/apps/com.mc.cmake_fei/bin/*
/usr/apps/com.mc.cmake_fei/data/*