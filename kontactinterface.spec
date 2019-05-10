#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kontactinterface
Version  : 19.04.1
Release  : 9
URL      : https://download.kde.org/stable/applications/19.04.1/src/kontactinterface-19.04.1.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.1/src/kontactinterface-19.04.1.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.1/src/kontactinterface-19.04.1.tar.xz.sig
Summary  : Kontact Plugin Interface Library
Group    : Development/Tools
License  : LGPL-2.1
Requires: kontactinterface-data = %{version}-%{release}
Requires: kontactinterface-lib = %{version}-%{release}
Requires: kontactinterface-license = %{version}-%{release}
Requires: kontactinterface-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev

%description
No detailed description available

%package data
Summary: data components for the kontactinterface package.
Group: Data

%description data
data components for the kontactinterface package.


%package dev
Summary: dev components for the kontactinterface package.
Group: Development
Requires: kontactinterface-lib = %{version}-%{release}
Requires: kontactinterface-data = %{version}-%{release}
Provides: kontactinterface-devel = %{version}-%{release}
Requires: kontactinterface = %{version}-%{release}
Requires: kontactinterface = %{version}-%{release}

%description dev
dev components for the kontactinterface package.


%package lib
Summary: lib components for the kontactinterface package.
Group: Libraries
Requires: kontactinterface-data = %{version}-%{release}
Requires: kontactinterface-license = %{version}-%{release}

%description lib
lib components for the kontactinterface package.


%package license
Summary: license components for the kontactinterface package.
Group: Default

%description license
license components for the kontactinterface package.


%package locales
Summary: locales components for the kontactinterface package.
Group: Default

%description locales
locales components for the kontactinterface package.


%prep
%setup -q -n kontactinterface-19.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557451753
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1557451753
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kontactinterface
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kontactinterface/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang kontactinterfaces5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservicetypes5/kontactplugin.desktop
/usr/share/xdg/kontactinterface.categories
/usr/share/xdg/kontactinterface.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KontactInterface/KontactInterface/Core
/usr/include/KF5/KontactInterface/KontactInterface/PimUniqueApplication
/usr/include/KF5/KontactInterface/KontactInterface/Plugin
/usr/include/KF5/KontactInterface/KontactInterface/Processes
/usr/include/KF5/KontactInterface/KontactInterface/Summary
/usr/include/KF5/KontactInterface/KontactInterface/UniqueAppHandler
/usr/include/KF5/KontactInterface/kontactinterface/core.h
/usr/include/KF5/KontactInterface/kontactinterface/kontactinterface_export.h
/usr/include/KF5/KontactInterface/kontactinterface/pimuniqueapplication.h
/usr/include/KF5/KontactInterface/kontactinterface/plugin.h
/usr/include/KF5/KontactInterface/kontactinterface/processes.h
/usr/include/KF5/KontactInterface/kontactinterface/summary.h
/usr/include/KF5/KontactInterface/kontactinterface/uniqueapphandler.h
/usr/include/KF5/kontactinterface_version.h
/usr/lib64/cmake/KF5KontactInterface/KF5KontactInterfaceConfig.cmake
/usr/lib64/cmake/KF5KontactInterface/KF5KontactInterfaceConfigVersion.cmake
/usr/lib64/cmake/KF5KontactInterface/KF5KontactInterfaceTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5KontactInterface/KF5KontactInterfaceTargets.cmake
/usr/lib64/libKF5KontactInterface.so
/usr/lib64/qt5/mkspecs/modules/qt_KontactInterface.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5KontactInterface.so.5
/usr/lib64/libKF5KontactInterface.so.5.11.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kontactinterface/COPYING.LIB

%files locales -f kontactinterfaces5.lang
%defattr(-,root,root,-)

