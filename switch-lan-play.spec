%global commit0 c0c663e3fdc95d6d6e8ab401caa2bfb5b5872e00
%global commit1 274f2bd3b70847cadd9a3965577a87e666ab9ac3
%global commit2 183ebc03331c7c92f8eaded42f3d262fbecce37a

Name: switch-lan-play
Version: v0.2.3
Release:        1%{?dist}
Summary: Make you and your friends play games like in a LAN.

License: GNU v3
URL: http://www.lan-play.com/
Source0:  https://github.com/spacemeowx2/switch-lan-play/archive/%{commit0}.tar.gz
Source1: https://github.com/libuv/libuv/archive/%{commit1}.tar.gz
Source2: https://github.com/skypjack/uvw/archive/%{commit2}.tar.gz

BuildRequires: libpcap-devel gcc g++ cmake libatomic libatomic-static
Requires: libpcap

%description
Make you and your friends play games like in a LAN.

%prep
%setup -n %{name}-%{commit0} -a1 -a2
rm -rf external/{libuv,uvw}
mv libuv-%{commit1} external/libuv
mv uvw-%{commit2} external/uvw

%build
mkdir -p build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 build/src/lan-play %{buildroot}/%{_bindir}/%{name}


%files
%license
%{_bindir}/%{name}

%changelog
* Mon Dec 21 2020 Anthony Rabbito <hello@anthonyrabbito.com> - 0.2.3
