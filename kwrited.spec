#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kwrited
Version  : 5.25.0
Release  : 64
URL      : https://download.kde.org/stable/plasma/5.25.0/kwrited-5.25.0.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.25.0/kwrited-5.25.0.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.25.0/kwrited-5.25.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: kwrited-bin = %{version}-%{release}
Requires: kwrited-data = %{version}-%{release}
Requires: kwrited-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdbusaddons-dev

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
%setup -q -n kwrited-5.25.0
cd %{_builddir}/kwrited-5.25.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1655409540
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1655409540
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kwrited
cp %{_builddir}/kwrited-5.25.0/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kwrited/3e8971c6c5f16674958913a94a36b1ea7a00ac46
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
/usr/share/package-licenses/kwrited/3e8971c6c5f16674958913a94a36b1ea7a00ac46
