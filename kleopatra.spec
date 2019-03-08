#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kleopatra
Version  : 18.12.3
Release  : 4
URL      : https://download.kde.org/stable/applications/18.12.3/src/kleopatra-18.12.3.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.3/src/kleopatra-18.12.3.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.3/src/kleopatra-18.12.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kleopatra-bin = %{version}-%{release}
Requires: kleopatra-data = %{version}-%{release}
Requires: kleopatra-lib = %{version}-%{release}
Requires: kleopatra-license = %{version}-%{release}
Requires: kleopatra-locales = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : gpgme-dev
BuildRequires : kmime-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : libkleo-dev
BuildRequires : qtbase-dev mesa-dev

%description
These scripts are to be executed like this:
Windows: gpg-connect-agent -v --no-ext-connect -S path\to\S.uiserver < script
Unix:    gpg-connect-agent -v                  -S path/to/S.uiserver < script
You need a very recent gpg-connect-agent (min. GnuPG 2.0.8-svn4603) for most
scripts, at least for the gpgex cases.

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
%setup -q -n kleopatra-18.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552018662
mkdir -p clr-build
pushd clr-build
export LDFLAGS="${LDFLAGS} -fno-lto"
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1552018662
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kleopatra
cp COPYING %{buildroot}/usr/share/package-licenses/kleopatra/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/kleopatra/COPYING.DOC
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
/usr/share/xdg/kleopatra.categories
/usr/share/xdg/kleopatra.renamecategories

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
/usr/share/package-licenses/kleopatra/COPYING
/usr/share/package-licenses/kleopatra/COPYING.DOC

%files locales -f kleopatra.lang -f kwatchgnupg.lang
%defattr(-,root,root,-)

