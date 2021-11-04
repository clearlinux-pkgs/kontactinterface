#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kontactinterface
Version  : 21.08.3
Release  : 35
URL      : https://download.kde.org/stable/release-service/21.08.3/src/kontactinterface-21.08.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.08.3/src/kontactinterface-21.08.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.08.3/src/kontactinterface-21.08.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kontactinterface-data = %{version}-%{release}
Requires: kontactinterface-lib = %{version}-%{release}
Requires: kontactinterface-license = %{version}-%{release}
Requires: kontactinterface-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev

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
%setup -q -n kontactinterface-21.08.3
cd %{_builddir}/kontactinterface-21.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1636056096
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
export SOURCE_DATE_EPOCH=1636056096
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kontactinterface
cp %{_builddir}/kontactinterface-21.08.3/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kontactinterface/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/kontactinterface-21.08.3/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kontactinterface/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/kontactinterface-21.08.3/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kontactinterface/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kontactinterface-21.08.3/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kontactinterface/6f1f675aa5f6a2bbaa573b8343044b166be28399
cp %{_builddir}/kontactinterface-21.08.3/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kontactinterface/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/kontactinterface-21.08.3/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kontactinterface/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kontactinterface-21.08.3/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kontactinterface/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kontactinterface-21.08.3/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kontactinterface/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
pushd clr-build
%make_install
popd
%find_lang kontactinterfaces5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservicetypes5/kontactplugin.desktop
/usr/share/qlogging-categories5/kontactinterface.categories
/usr/share/qlogging-categories5/kontactinterface.renamecategories

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
/usr/lib64/libKF5KontactInterface.so.5.18.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kontactinterface/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kontactinterface/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kontactinterface/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kontactinterface/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kontactinterface/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kontactinterface/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kontactinterface/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f kontactinterfaces5.lang
%defattr(-,root,root,-)

