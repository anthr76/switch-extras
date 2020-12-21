%global commit0 c0c663e3fdc95d6d6e8ab401caa2bfb5b5872e00

Name: switch-lan-play
Version: v0.2.3
Release:        1%{?dist}
Summary: Make you and your friends play games like in a LAN.

License: GNU v3
URL: http://www.lan-play.com/
Source0:  https://github.com/spacemeowx2/switch-lan-play/archive/%{version}.tar.gz

BuildRequires: libpcap-devel git gcc g++ cmake
Requires: libpcap

%description
Make you and your friends play games like in a LAN.

%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%check


%files
%license
%doc


%changelog
* - Initial build
