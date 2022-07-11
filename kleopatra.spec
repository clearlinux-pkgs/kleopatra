#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kleopatra
Version  : 22.04.3
Release  : 45
URL      : https://download.kde.org/stable/release-service/22.04.3/src/kleopatra-22.04.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.04.3/src/kleopatra-22.04.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.04.3/src/kleopatra-22.04.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kleopatra-bin = %{version}-%{release}
Requires: kleopatra-data = %{version}-%{release}
Requires: kleopatra-lib = %{version}-%{release}
Requires: kleopatra-license = %{version}-%{release}
Requires: kleopatra-locales = %{version}-%{release}
Requires: gnupg
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : extra-cmake-modules-data
BuildRequires : git
BuildRequires : gpgme-dev
BuildRequires : gpgme-dev gpgme-extras
BuildRequires : kcodecs-dev
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kdoctools-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : kitemmodels-dev
BuildRequires : kmime-dev
BuildRequires : knotifications-dev
BuildRequires : ktextwidgets-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kwindowsystem-dev
BuildRequires : kxmlgui-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : libgpg-error-extras
BuildRequires : libkleo-dev

%description
Kleopatra packaging notes
=========================
The build dependencies should be fairly straightforward (see CMakeLists.txt)

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


%package dev
Summary: dev components for the kleopatra package.
Group: Development
Requires: kleopatra-lib = %{version}-%{release}
Requires: kleopatra-bin = %{version}-%{release}
Requires: kleopatra-data = %{version}-%{release}
Provides: kleopatra-devel = %{version}-%{release}
Requires: kleopatra = %{version}-%{release}

%description dev
dev components for the kleopatra package.


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
%setup -q -n kleopatra-22.04.3
cd %{_builddir}/kleopatra-22.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657581588
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1657581588
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kleopatra
cp %{_builddir}/kleopatra-22.04.3/.krazy.license %{buildroot}/usr/share/package-licenses/kleopatra/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
cp %{_builddir}/kleopatra-22.04.3/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kleopatra/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/kleopatra-22.04.3/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kleopatra/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/kleopatra-22.04.3/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kleopatra/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/kleopatra-22.04.3/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kleopatra/7697008f58568e61e7598e796eafc2a997503fde
cp %{_builddir}/kleopatra-22.04.3/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kleopatra/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/kleopatra-22.04.3/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kleopatra/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/kleopatra-22.04.3/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kleopatra/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kleopatra-22.04.3/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kleopatra/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kleopatra-22.04.3/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kleopatra/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/kleopatra-22.04.3/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kleopatra/6f1f675aa5f6a2bbaa573b8343044b166be28399
cp %{_builddir}/kleopatra-22.04.3/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kleopatra/757b86330df80f81143d5916b3e92b4bcb1b1890
pushd clr-build
%make_install
popd
%find_lang kleopatra
%find_lang kwatchgnupg

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kleopatra
/usr/bin/kwatchgnupg

%files data
%defattr(-,root,root,-)
/usr/share/applications/kleopatra_import.desktop
/usr/share/applications/org.kde.kleopatra.desktop
/usr/share/icons/hicolor/128x128/apps/kleopatra.png
/usr/share/icons/hicolor/16x16/apps/kleopatra.png
/usr/share/icons/hicolor/22x22/apps/kleopatra.png
/usr/share/icons/hicolor/256x256/apps/kleopatra.png
/usr/share/icons/hicolor/32x32/apps/kleopatra.png
/usr/share/icons/hicolor/48x48/apps/kleopatra.png
/usr/share/icons/hicolor/64x64/apps/kleopatra.png
/usr/share/kconf_update/kleopatra-15.08-kickoff.sh
/usr/share/kconf_update/kleopatra.upd
/usr/share/kio/servicemenus/kleopatra_decryptverifyfiles.desktop
/usr/share/kio/servicemenus/kleopatra_decryptverifyfolders.desktop
/usr/share/kio/servicemenus/kleopatra_signencryptfiles.desktop
/usr/share/kio/servicemenus/kleopatra_signencryptfolders.desktop
/usr/share/kleopatra/pics/kleopatra_splashscreen.png
/usr/share/kleopatra/pics/kleopatra_splashscreen.svgz
/usr/share/kleopatra/pics/kleopatra_wizard.png
/usr/share/kleopatra/pics/kleopatra_wizard.svgz
/usr/share/kservices5/kleopatra_config_gnupgsystem.desktop
/usr/share/kwatchgnupg/pics/kwatchgnupg.png
/usr/share/kwatchgnupg/pics/kwatchgnupg2.png
/usr/share/metainfo/org.kde.kleopatra.appdata.xml
/usr/share/mime-packages/application-vnd-kde-kleopatra.xml
/usr/share/qlogging-categories5/kleopatra.categories
/usr/share/qlogging-categories5/kleopatra.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/lib64/libkleopatraclientcore.so
/usr/lib64/libkleopatraclientgui.so

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
/usr/lib64/libkleopatraclientcore.so.1
/usr/lib64/libkleopatraclientcore.so.1.3.0
/usr/lib64/libkleopatraclientgui.so.1
/usr/lib64/libkleopatraclientgui.so.1.3.0
/usr/lib64/qt5/plugins/pim/kcms/kleopatra/kleopatra_config_gnupgsystem.so

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

