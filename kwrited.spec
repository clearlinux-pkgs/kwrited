#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : kwrited
Version  : 5.16.5
Release  : 23
URL      : https://download.kde.org/stable/plasma/5.16.5/kwrited-5.16.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.16.5/kwrited-5.16.5.tar.xz
Source1 : https://download.kde.org/stable/plasma/5.16.5/kwrited-5.16.5.tar.xz.sig
Summary  : KDE daemon listening for wall and write messages
Group    : Development/Tools
License  : GPL-2.0
Requires: kwrited-bin = %{version}-%{release}
Requires: kwrited-data = %{version}-%{release}
Requires: kwrited-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde

%description
No detailed description available

%package bin
Summary: bin components for the kwrited package.
Group: Binaries
Requires: kwrited-data = %{version}-%{release}
Requires: kwrited-license = %{version}-%{release}

%description bin
bin components for the kwrited package.


%package data
Summary: data components for the kwrited package.
Group: Data

%description data
data components for the kwrited package.


%package license
Summary: license components for the kwrited package.
Group: Default

%description license
license components for the kwrited package.


%prep
%setup -q -n kwrited-5.16.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567646609
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1567646609
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kwrited
cp COPYING %{buildroot}/usr/share/package-licenses/kwrited/COPYING
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kwrited

%files data
%defattr(-,root,root,-)
/usr/share/knotifications5/kwrited.notifyrc
/usr/share/xdg/autostart/kwrited-autostart.desktop

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kwrited/COPYING
