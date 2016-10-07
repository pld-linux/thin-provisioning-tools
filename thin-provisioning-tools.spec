Summary:	Tools for manipulating dm-thin device-mapper target metadata
Summary(pl.UTF-8):	Narzędzia do modyfikowania metadanych celów dm-thin device-mappera
Name:		thin-provisioning-tools
Version:	0.6.3
Release:	1
License:	GPL v3+
Group:		Applications/System
#Source0Download: https://github.com/jthornber/thin-provisioning-tools/releases
Source0:	https://github.com/jthornber/thin-provisioning-tools/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	28b352363ea7eb6698ad2efcd7d8c2ae
Patch0:		%{name}-sh.patch
URL:		https://github.com/jthornber/thin-provisioning-tools
BuildRequires:	autoconf >= 2.61
BuildRequires:	boost-devel
BuildRequires:	expat-devel >= 1.95
BuildRequires:	gcc-c++ >= 6:4.0
BuildRequires:	libaio-devel
BuildRequires:	libstdc++-devel >= 6:4.0
Obsoletes:	device-mapper-persistent-data
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A suite of tools for manipulating the metadata of the dm-thin
device-mapper target.

%description -l pl.UTF-8
Zestaw narzędzi do modyfikowania metadanych celów dm-thin
device-mappera.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure \
	--with-optimisation=" "

%{__make} \
	V=

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README.md TODO.org
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
%attr(755,root,root) %{_sbindir}/thin_check
%attr(755,root,root) %{_sbindir}/thin_delta
%attr(755,root,root) %{_sbindir}/thin_dump
%attr(755,root,root) %{_sbindir}/thin_ls
%attr(755,root,root) %{_sbindir}/thin_metadata_size
%attr(755,root,root) %{_sbindir}/thin_repair
%attr(755,root,root) %{_sbindir}/thin_restore
%attr(755,root,root) %{_sbindir}/thin_rmap
%attr(755,root,root) %{_sbindir}/thin_trim
%{_mandir}/man8/cache_check.8*
%{_mandir}/man8/cache_dump.8*
%{_mandir}/man8/cache_repair.8*
%{_mandir}/man8/cache_restore.8*
%{_mandir}/man8/era_check.8*
%{_mandir}/man8/era_dump.8*
%{_mandir}/man8/era_invalidate.8*
%{_mandir}/man8/thin_check.8*
%{_mandir}/man8/thin_delta.8*
%{_mandir}/man8/thin_dump.8*
%{_mandir}/man8/thin_ls.8*
%{_mandir}/man8/thin_metadata_size.8*
%{_mandir}/man8/thin_repair.8*
%{_mandir}/man8/thin_restore.8*
%{_mandir}/man8/thin_rmap.8*
%{_mandir}/man8/thin_trim.8*
