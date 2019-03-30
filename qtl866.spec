%global commit 1173c3e048c9b777611b379892f397dd5c64a261
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           qtl866
Version:        0
Release:        0.20170405git%{shortcommit}%{?dist}
Summary:        GUI driver for the TL866 (MiniPRO) chip programmer

License:        GPLv3+
URL:            https://github.com/wd5gnr/qtl866
Source0:        https://github.com/wd5gnr/qtl866/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

# Not upstreamable
Patch0:         https://github.com/lkundrak/qtl866/commit/006d5dfa.patch#/0007-Make-it-somehow-work-with-Wayland.patch

BuildRequires:  qt5-qtbase-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       minipro
Requires:       bless

%description
GUI for a programming utility compatible with MiniPRO TL866CS, MiniPRO
TL866A, and XGecu TL866II Plus chip programmers. Supports more than 13000
target devices (including AVRs, PICs, various BIOSes and EEPROMs).


%prep
%setup -q -n %{name}-%{commit}
%patch0 -p1


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
* Sat Mar 30 2019 Aimylios <aimylios@xxx.xx> - 0-0.20170405git1173c3e
- Update to a newer version
- Drop upstreamed patches

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161035git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161034git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161033git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161032git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161031git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161030git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 29 2016 Lubomir Rintel <lkundrak@v3.sk> - 0-0.20161029git7bb1d95
- Initial packaging
