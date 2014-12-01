Summary:	Tools for manipulating dm-thin device-mapper target medatada
Summary(pl.UTF-8):	Narzędzia do modyfikowania metadanych celów dm-thin device-mappera
Name:		thin-provisioning-tools
Version:	0.4.1
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	https://github.com/jthornber/thin-provisioning-tools/archive/v%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	00bfee4c83c732fd7f5273ec2b6754a2
URL:		https://github.com/jthornber/thin-provisioning-tools
BuildRequires:	autoconf >= 2.61
BuildRequires:	boost-devel
BuildRequires:	expat-devel >= 1.95
# exact version unknown (some C++11 features needed)
BuildRequires:	gcc-c++ >= 6:4.6
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A suite of tools for manipulating the metadata of the dm-thin
device-mapper target.

%description -l pl.UTF-8
Zestaw narzędzi do modyfikowania metadanych celów dm-thin
device-mappera.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make} \
	CFLAGS="%{rpmcflags} -Wall" \
	CXXFLAGS="%{rpmcxxflags} -fno-strict-aliasing -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md TODO.org
%attr(755,root,root) %{_sbindir}/thin_check
%attr(755,root,root) %{_sbindir}/thin_dump
%attr(755,root,root) %{_sbindir}/thin_metadata_size
%attr(755,root,root) %{_sbindir}/thin_repair
%attr(755,root,root) %{_sbindir}/thin_restore
%attr(755,root,root) %{_sbindir}/thin_rmap
%attr(755,root,root) %{_sbindir}/cache_check
%attr(755,root,root) %{_sbindir}/cache_dump
%attr(755,root,root) %{_sbindir}/cache_metadata_size
%attr(755,root,root) %{_sbindir}/cache_repair
%attr(755,root,root) %{_sbindir}/cache_restore
%attr(755,root,root) %{_sbindir}/era_check
%attr(755,root,root) %{_sbindir}/era_dump
%attr(755,root,root) %{_sbindir}/era_invalidate
%attr(755,root,root) %{_sbindir}/era_restore
%attr(755,root,root) %{_sbindir}/pdata_tools
%{_mandir}/man8/thin_check.8*
%{_mandir}/man8/thin_dump.8*
%{_mandir}/man8/thin_metadata_size.8*
%{_mandir}/man8/thin_repair.8*
%{_mandir}/man8/thin_restore.8*
%{_mandir}/man8/thin_rmap.8*
%{_mandir}/man8/cache_check.8.gz
%{_mandir}/man8/cache_dump.8.gz
%{_mandir}/man8/cache_repair.8.gz
%{_mandir}/man8/cache_restore.8.gz
%{_mandir}/man8/era_check.8.gz
%{_mandir}/man8/era_dump.8.gz
%{_mandir}/man8/era_invalidate.8.gz
