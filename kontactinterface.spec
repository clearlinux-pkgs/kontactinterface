#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 94c6be0
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kontactinterface
Version  : 24.12.2
Release  : 80
URL      : https://download.kde.org/stable/release-service/24.12.2/src/kontactinterface-24.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.2/src/kontactinterface-24.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.2/src/kontactinterface-24.12.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
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
BuildRequires : gnupg
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : libICE-dev
BuildRequires : libSM-dev
BuildRequires : libX11-dev
BuildRequires : libXScrnSaver-dev
BuildRequires : libXau-dev
BuildRequires : libXcomposite-dev
BuildRequires : libXcursor-dev
BuildRequires : libXdamage-dev
BuildRequires : libXdmcp-dev
BuildRequires : libXext-dev
BuildRequires : libXfixes-dev
BuildRequires : libXft-dev
BuildRequires : libXi-dev
BuildRequires : libXinerama-dev
BuildRequires : libXmu-dev
BuildRequires : libXpm-dev
BuildRequires : libXrandr-dev
BuildRequires : libXrender-dev
BuildRequires : libXres-dev
BuildRequires : libXt-dev
BuildRequires : libXtst-dev
BuildRequires : libXv-dev
BuildRequires : libXxf86vm-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SPDX-License-Identifier: CC0-1.0

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kontactinterface-24.12.2
cd %{_builddir}/kontactinterface-24.12.2
pushd ..
cp -a kontactinterface-24.12.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1738961796
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1738961796
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kontactinterface
cp %{_builddir}/kontactinterface-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kontactinterface/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kontactinterface-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kontactinterface/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kontactinterface-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kontactinterface/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kontactinterface-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kontactinterface/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kontactinterface-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kontactinterface/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kontactinterface-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kontactinterface/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kontactinterface-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kontactinterface/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kontactinterface-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kontactinterface/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kontactinterface-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kontactinterface/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/kontactinterface-%{version}/readme-build-ftime.txt.license %{buildroot}/usr/share/package-licenses/kontactinterface/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kontactinterfaces6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/kontactinterface.categories
/usr/share/qlogging-categories6/kontactinterface.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/KontactInterface/KontactInterface/Core
/usr/include/KPim6/KontactInterface/KontactInterface/PimUniqueApplication
/usr/include/KPim6/KontactInterface/KontactInterface/Plugin
/usr/include/KPim6/KontactInterface/KontactInterface/Processes
/usr/include/KPim6/KontactInterface/KontactInterface/Summary
/usr/include/KPim6/KontactInterface/KontactInterface/UniqueAppHandler
/usr/include/KPim6/KontactInterface/kontactinterface/core.h
/usr/include/KPim6/KontactInterface/kontactinterface/kontactinterface_export.h
/usr/include/KPim6/KontactInterface/kontactinterface/pimuniqueapplication.h
/usr/include/KPim6/KontactInterface/kontactinterface/plugin.h
/usr/include/KPim6/KontactInterface/kontactinterface/processes.h
/usr/include/KPim6/KontactInterface/kontactinterface/summary.h
/usr/include/KPim6/KontactInterface/kontactinterface/uniqueapphandler.h
/usr/include/KPim6/KontactInterface/kontactinterface_version.h
/usr/lib64/cmake/KPim6KontactInterface/KPim6KontactInterfaceConfig.cmake
/usr/lib64/cmake/KPim6KontactInterface/KPim6KontactInterfaceConfigVersion.cmake
/usr/lib64/cmake/KPim6KontactInterface/KPim6KontactInterfaceTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6KontactInterface/KPim6KontactInterfaceTargets.cmake
/usr/lib64/libKPim6KontactInterface.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6KontactInterface.so.6.3.2
/usr/lib64/libKPim6KontactInterface.so.6
/usr/lib64/libKPim6KontactInterface.so.6.3.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kontactinterface/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kontactinterface/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kontactinterface/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kontactinterface/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kontactinterface/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kontactinterface/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kontactinterface/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f kontactinterfaces6.lang
%defattr(-,root,root,-)

