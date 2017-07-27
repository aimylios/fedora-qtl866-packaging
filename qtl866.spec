%global commit 544d42c6f4f56e641f179ba24b638d017e5ab217
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           qtl866
Version:        0
Release:        0.20161031git%{shortcommit}%{?dist}
Summary:        GUI driver for the TL866 (MiniPRO) chip programmer

Group:          Applications/Engineering
License:        GPLv3+
URL:            https://github.com/wd5gnr/qtl866
Source0:        https://github.com/wd5gnr/qtl866/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

# https://github.com/wd5gnr/qtl866/pull/9
Patch0:         https://github.com/lkundrak/qtl866/commit/6eb0fd70.patch#/0001-Fix-build.patch
Patch1:         https://github.com/lkundrak/qtl866/commit/cdcdc2c9.patch#/0002-Fix-a-typo.patch
Patch2:         https://github.com/lkundrak/qtl866/commit/42d15fb1.patch#/0003-Load-qtparts-on-build.patch

# https://github.com/wd5gnr/qtl866/pull/8
Patch3:         https://github.com/lkundrak/qtl866/commit/9f7553d4.patch#/0004-Add-a-desktop-file-and-an-icon.patch
Patch4:         https://github.com/lkundrak/qtl866/commit/7b3f233b.patch#/0005-Add-AppStream-metadata.patch

# Not upstreamable
Patch5:         https://github.com/lkundrak/qtl866/commit/6a4fe197.patch#/0006-Use-my-clone-in-AppData-for-now.patch
Patch6:         https://github.com/lkundrak/qtl866/commit/006d5dfa.patch#/0007-Make-it-somehow-work-with-Wayland.patch

BuildRequires:  qt5-qtbase-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  git
Requires:       minipro
Requires:       bless

%description
GUI for a programming utility compatible with Minipro TL866CS and Minipro
TL866A chip programmers. Supports more than 13000 target devices
(including AVRs, PICs, various BIOSes and EEPROMs).


%prep
%setup -q -n %{name}-%{commit}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
# The binary patch needs to be applied with git
git --git-dir=. apply --unsafe-paths --directory=. --apply %{PATCH4}
%patch5 -p1
%patch6 -p1


%build
%{_qt5_qmake}
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_bindir}
install binhexedit %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -pm644 qtl866.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications qtl866.desktop
mkdir -p %{buildroot}%{_datadir}/appdata
install -pm644 qtl866.appdata.xml %{buildroot}%{_datadir}/appdata/
make install INSTALL_ROOT=%{buildroot}


%check
appstream-util --nonet validate-relax %{buildroot}%{_datadir}/appdata/qtl866.appdata.xml


%files
%{_bindir}/qtl866
%{_bindir}/binhexedit
%{_datadir}/applications/qtl866.desktop
%{_datadir}/icons/hicolor
%{_datadir}/appdata/qtl866.appdata.xml
%doc README.md
%license COPYING


%changelog
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161031git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161030git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 29 2016 Lubomir Rintel <lkundrak@v3.sk> - 0-0.20161029git7bb1d95
- Initial packaging
