#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kleopatra
Version  : 24.08.2
Release  : 79
URL      : https://download.kde.org/stable/release-service/24.08.2/src/kleopatra-24.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.2/src/kleopatra-24.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.2/src/kleopatra-24.08.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kleopatra-bin = %{version}-%{release}
Requires: kleopatra-data = %{version}-%{release}
Requires: kleopatra-lib = %{version}-%{release}
Requires: kleopatra-license = %{version}-%{release}
Requires: kleopatra-locales = %{version}-%{release}
Requires: gnupg
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : extra-cmake-modules-data
BuildRequires : git
BuildRequires : gnupg
BuildRequires : gpgme-dev
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : ki18n-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kio-dev
BuildRequires : kmailtransport-dev
BuildRequires : kmbox-dev
BuildRequires : kmime-dev
BuildRequires : kstatusnotifieritem-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : libgpg-error-extras
BuildRequires : libkleo-dev
BuildRequires : mimetreeparser-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(gpg-error)
BuildRequires : pkgconfig(libassuan)
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Analyzing Build Performance
For debug build time:
We need ClangBuildAnalyzer
git clone https://github.com/aras-p/ClangBuildAnalyzer
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=<path> ../
make install

%package bin
Summary: bin components for the kleopatra package.
Group: Binaries
Requires: kleopatra-data = %{version}-%{release}
Requires: kleopatra-license = %{version}-%{release}

%description bin
bin components for the kleopatra package.


%package data
Summary: data components for the kleopatra package.
Group: Data

%description data
data components for the kleopatra package.


%package doc
Summary: doc components for the kleopatra package.
Group: Documentation

%description doc
doc components for the kleopatra package.


%package lib
Summary: lib components for the kleopatra package.
Group: Libraries
Requires: kleopatra-data = %{version}-%{release}
Requires: kleopatra-license = %{version}-%{release}

%description lib
lib components for the kleopatra package.


%package license
Summary: license components for the kleopatra package.
Group: Default

%description license
license components for the kleopatra package.


%package locales
Summary: locales components for the kleopatra package.
Group: Default

%description locales
locales components for the kleopatra package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kleopatra-24.08.2
cd %{_builddir}/kleopatra-24.08.2
pushd ..
cp -a kleopatra-24.08.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728928581
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
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
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1728928581
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kleopatra
cp %{_builddir}/kleopatra-%{version}/.krazy.license %{buildroot}/usr/share/package-licenses/kleopatra/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/kleopatra-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kleopatra/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kleopatra-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kleopatra/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kleopatra-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kleopatra/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kleopatra-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kleopatra/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kleopatra-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kleopatra/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/kleopatra-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kleopatra/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kleopatra-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kleopatra/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kleopatra-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kleopatra/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kleopatra-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kleopatra/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kleopatra-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kleopatra/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kleopatra-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kleopatra/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
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
%find_lang kleopatra
%find_lang kwatchgnupg
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kleopatra
/V3/usr/bin/kwatchgnupg
/usr/bin/kleopatra
/usr/bin/kwatchgnupg

%files data
%defattr(-,root,root,-)
/usr/share/applications/kleopatra_import.desktop
/usr/share/applications/org.kde.kleopatra.desktop
/usr/share/applications/org.kde.kwatchgnupg.desktop
/usr/share/icons/hicolor/128x128/apps/kleopatra.png
/usr/share/icons/hicolor/16x16/apps/kleopatra.png
/usr/share/icons/hicolor/22x22/apps/kleopatra.png
/usr/share/icons/hicolor/22x22/apps/kwatchgnupg.png
/usr/share/icons/hicolor/256x256/apps/kleopatra.png
/usr/share/icons/hicolor/32x32/apps/kleopatra.png
/usr/share/icons/hicolor/48x48/apps/kleopatra.png
/usr/share/icons/hicolor/64x64/apps/kleopatra.png
/usr/share/kio/servicemenus/kleopatra_decryptverifyfiles.desktop
/usr/share/kio/servicemenus/kleopatra_decryptverifyfolders.desktop
/usr/share/kio/servicemenus/kleopatra_signencryptfiles.desktop
/usr/share/kio/servicemenus/kleopatra_signencryptfolders.desktop
/usr/share/kleopatra/pics/kleopatra_splashscreen.png
/usr/share/kleopatra/pics/kleopatra_splashscreen.svgz
/usr/share/kleopatra/pics/kleopatra_wizard.png
/usr/share/kleopatra/pics/kleopatra_wizard.svgz
/usr/share/kwatchgnupg/pics/kwatchgnupg.png
/usr/share/kwatchgnupg/pics/kwatchgnupg2.png
/usr/share/metainfo/org.kde.kleopatra.appdata.xml
/usr/share/mime-packages/application-vnd-kde-kleopatra.xml
/usr/share/mime-packages/kleopatra-mime.xml
/usr/share/qlogging-categories6/kleopatra.categories
/usr/share/qlogging-categories6/kleopatra.renamecategories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kleopatra/index.cache.bz2
/usr/share/doc/HTML/ca/kleopatra/index.docbook
/usr/share/doc/HTML/ca/kwatchgnupg/index.cache.bz2
/usr/share/doc/HTML/ca/kwatchgnupg/index.docbook
/usr/share/doc/HTML/de/kleopatra/index.cache.bz2
/usr/share/doc/HTML/de/kleopatra/index.docbook
/usr/share/doc/HTML/de/kwatchgnupg/index.cache.bz2
/usr/share/doc/HTML/de/kwatchgnupg/index.docbook
/usr/share/doc/HTML/en/kleopatra/index.cache.bz2
/usr/share/doc/HTML/en/kleopatra/index.docbook
/usr/share/doc/HTML/en/kwatchgnupg/index.cache.bz2
/usr/share/doc/HTML/en/kwatchgnupg/index.docbook
/usr/share/doc/HTML/es/kleopatra/index.cache.bz2
/usr/share/doc/HTML/es/kleopatra/index.docbook
/usr/share/doc/HTML/es/kwatchgnupg/index.cache.bz2
/usr/share/doc/HTML/es/kwatchgnupg/index.docbook
/usr/share/doc/HTML/et/kleopatra/index.cache.bz2
/usr/share/doc/HTML/et/kleopatra/index.docbook
/usr/share/doc/HTML/et/kwatchgnupg/index.cache.bz2
/usr/share/doc/HTML/et/kwatchgnupg/index.docbook
/usr/share/doc/HTML/fr/kleopatra/index.cache.bz2
/usr/share/doc/HTML/fr/kleopatra/index.docbook
/usr/share/doc/HTML/fr/kwatchgnupg/index.cache.bz2
/usr/share/doc/HTML/fr/kwatchgnupg/index.docbook
/usr/share/doc/HTML/it/kleopatra/index.cache.bz2
/usr/share/doc/HTML/it/kleopatra/index.docbook
/usr/share/doc/HTML/it/kwatchgnupg/index.cache.bz2
/usr/share/doc/HTML/it/kwatchgnupg/index.docbook
/usr/share/doc/HTML/nl/kleopatra/index.cache.bz2
/usr/share/doc/HTML/nl/kleopatra/index.docbook
/usr/share/doc/HTML/nl/kwatchgnupg/index.cache.bz2
/usr/share/doc/HTML/nl/kwatchgnupg/index.docbook
/usr/share/doc/HTML/pt/kleopatra/index.cache.bz2
/usr/share/doc/HTML/pt/kleopatra/index.docbook
/usr/share/doc/HTML/pt/kwatchgnupg/index.cache.bz2
/usr/share/doc/HTML/pt/kwatchgnupg/index.docbook
/usr/share/doc/HTML/pt_BR/kleopatra/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kleopatra/index.docbook
/usr/share/doc/HTML/pt_BR/kwatchgnupg/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kwatchgnupg/index.docbook
/usr/share/doc/HTML/ru/kleopatra/index.cache.bz2
/usr/share/doc/HTML/ru/kleopatra/index.docbook
/usr/share/doc/HTML/ru/kwatchgnupg/index.cache.bz2
/usr/share/doc/HTML/ru/kwatchgnupg/index.docbook
/usr/share/doc/HTML/sl/kleopatra/index.cache.bz2
/usr/share/doc/HTML/sl/kleopatra/index.docbook
/usr/share/doc/HTML/sl/kwatchgnupg/index.cache.bz2
/usr/share/doc/HTML/sl/kwatchgnupg/index.docbook
/usr/share/doc/HTML/sv/kleopatra/index.cache.bz2
/usr/share/doc/HTML/sv/kleopatra/index.docbook
/usr/share/doc/HTML/sv/kwatchgnupg/index.cache.bz2
/usr/share/doc/HTML/sv/kwatchgnupg/index.docbook
/usr/share/doc/HTML/uk/kleopatra/index.cache.bz2
/usr/share/doc/HTML/uk/kleopatra/index.docbook
/usr/share/doc/HTML/uk/kwatchgnupg/index.cache.bz2
/usr/share/doc/HTML/uk/kwatchgnupg/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libkleopatraclientcore.so.1.3.0
/V3/usr/lib64/libkleopatraclientgui.so.1.3.0
/V3/usr/lib64/qt6/plugins/pim6/kcms/kleopatra/kleopatra_config_gnupgsystem.so
/usr/lib64/libkleopatraclientcore.so.1
/usr/lib64/libkleopatraclientcore.so.1.3.0
/usr/lib64/libkleopatraclientgui.so.1
/usr/lib64/libkleopatraclientgui.so.1.3.0
/usr/lib64/qt6/plugins/pim6/kcms/kleopatra/kleopatra_config_gnupgsystem.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kleopatra/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kleopatra/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kleopatra/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kleopatra/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kleopatra/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kleopatra/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kleopatra/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kleopatra/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kleopatra/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kleopatra/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kleopatra/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kleopatra.lang -f kwatchgnupg.lang
%defattr(-,root,root,-)

