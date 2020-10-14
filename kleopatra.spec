#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kleopatra
Version  : 20.08.2
Release  : 26
URL      : https://download.kde.org/stable/release-service/20.08.2/src/kleopatra-20.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.08.2/src/kleopatra-20.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.08.2/src/kleopatra-20.08.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kleopatra-bin = %{version}-%{release}
Requires: kleopatra-data = %{version}-%{release}
Requires: kleopatra-lib = %{version}-%{release}
Requires: kleopatra-license = %{version}-%{release}
Requires: kleopatra-locales = %{version}-%{release}
Requires: gnupg
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : gpgme-dev
BuildRequires : gpgme-dev gpgme-extras
BuildRequires : kcmutils-dev
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
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kleopatra-20.08.2
cd %{_builddir}/kleopatra-20.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602710654
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
export SOURCE_DATE_EPOCH=1602710654
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kleopatra
cp %{_builddir}/kleopatra-20.08.2/COPYING %{buildroot}/usr/share/package-licenses/kleopatra/1495fc4592f8e9b7641127ee24cfe6b6930645c8
cp %{_builddir}/kleopatra-20.08.2/COPYING.DOC %{buildroot}/usr/share/package-licenses/kleopatra/5897e7b5abe2c1a662e8a3bea20d40fbcdf92d09
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
/usr/share/kleopatra/pics/kleopatra_splashscreen.png
/usr/share/kleopatra/pics/kleopatra_splashscreen.svgz
/usr/share/kleopatra/pics/kleopatra_wizard.png
/usr/share/kleopatra/pics/kleopatra_wizard.svgz
/usr/share/kservices5/kleopatra_config_appear.desktop
/usr/share/kservices5/kleopatra_config_cryptooperations.desktop
/usr/share/kservices5/kleopatra_config_dirserv.desktop
/usr/share/kservices5/kleopatra_config_gnupgsystem.desktop
/usr/share/kservices5/kleopatra_config_smimevalidation.desktop
/usr/share/kservices5/kleopatra_decryptverifyfiles.desktop
/usr/share/kservices5/kleopatra_decryptverifyfolders.desktop
/usr/share/kservices5/kleopatra_signencryptfiles.desktop
/usr/share/kservices5/kleopatra_signencryptfolders.desktop
/usr/share/kwatchgnupg/pics/kwatchgnupg.png
/usr/share/kwatchgnupg/pics/kwatchgnupg2.png
/usr/share/metainfo/org.kde.kleopatra.appdata.xml
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
/usr/lib64/qt5/plugins/kcm_kleopatra.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kleopatra/1495fc4592f8e9b7641127ee24cfe6b6930645c8
/usr/share/package-licenses/kleopatra/5897e7b5abe2c1a662e8a3bea20d40fbcdf92d09

%files locales -f kleopatra.lang -f kwatchgnupg.lang
%defattr(-,root,root,-)

