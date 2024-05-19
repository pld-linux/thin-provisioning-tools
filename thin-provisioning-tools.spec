Summary:	Tools for manipulating dm-thin device-mapper target metadata
Summary(pl.UTF-8):	Narzędzia do modyfikowania metadanych celów dm-thin device-mappera
Name:		thin-provisioning-tools
Version:	1.0.12
Release:	1
License:	GPL v3+
Group:		Applications/System
#Source0Download: https://github.com/jthornber/thin-provisioning-tools/releases
Source0:	https://github.com/jthornber/thin-provisioning-tools/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	05d99251481dbd135c3c39a02fafd3cb
# cargo vendor && cd .. && tar cJf thin-provisioning-tools-1.0.12-vendor.tar.xz thin-provisioning-tools-1.0.12/vendor thin-provisioning-tools-1.0.12/Cargo.lock
Source1:	%{name}-%{version}-vendor.tar.xz
# Source1-md5:	91dc98d98d0036d87bf6123e2781fe6b
URL:		https://github.com/jthornber/thin-provisioning-tools
BuildRequires:	cargo
BuildRequires:	expat-devel >= 1.95
BuildRequires:	libstdc++-devel >= 6:4.0
BuildRequires:	rpmbuild(macros) >= 2.004
BuildRequires:	rust
Obsoletes:	device-mapper-persistent-data
ExclusiveArch:	%{rust_arches}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A suite of tools for manipulating the metadata of the dm-thin
device-mapper target.

%description -l pl.UTF-8
Zestaw narzędzi do modyfikowania metadanych celów dm-thin
device-mappera.

%prep
%setup -q -b1

export CARGO_HOME="$(pwd)/.cargo"

mkdir -p "$CARGO_HOME"
cat >.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/jthornber/rio?branch=master"]
git = "https://github.com/jthornber/rio"
branch = "master"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export CARGO_HOME="$(pwd)/.cargo"

%cargo_build --frozen

%install
rm -rf $RPM_BUILD_ROOT
export CARGO_HOME="$(pwd)/.cargo"

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PDATA_TOOLS=%{cargo_targetdir}/%{rust_target}/release/pdata_tools \
	STRIP=:

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README.md doc/TODO.md
%attr(755,root,root) %{_sbindir}/cache_check
%attr(755,root,root) %{_sbindir}/cache_dump
%attr(755,root,root) %{_sbindir}/cache_metadata_size
%attr(755,root,root) %{_sbindir}/cache_repair
%attr(755,root,root) %{_sbindir}/cache_restore
%attr(755,root,root) %{_sbindir}/cache_writeback
%attr(755,root,root) %{_sbindir}/era_check
%attr(755,root,root) %{_sbindir}/era_dump
%attr(755,root,root) %{_sbindir}/era_invalidate
%attr(755,root,root) %{_sbindir}/era_restore
%attr(755,root,root) %{_sbindir}/pdata_tools
%attr(755,root,root) %{_sbindir}/thin_check
%attr(755,root,root) %{_sbindir}/thin_delta
%attr(755,root,root) %{_sbindir}/thin_dump
%attr(755,root,root) %{_sbindir}/thin_ls
%attr(755,root,root) %{_sbindir}/thin_metadata_pack
%attr(755,root,root) %{_sbindir}/thin_metadata_size
%attr(755,root,root) %{_sbindir}/thin_metadata_unpack
%attr(755,root,root) %{_sbindir}/thin_repair
%attr(755,root,root) %{_sbindir}/thin_restore
%attr(755,root,root) %{_sbindir}/thin_rmap
%attr(755,root,root) %{_sbindir}/thin_trim
%{_mandir}/man8/cache_check.8*
%{_mandir}/man8/cache_dump.8*
%{_mandir}/man8/cache_metadata_size.8*
%{_mandir}/man8/cache_repair.8*
%{_mandir}/man8/cache_restore.8*
%{_mandir}/man8/cache_writeback.8*
%{_mandir}/man8/era_check.8*
%{_mandir}/man8/era_dump.8*
%{_mandir}/man8/era_invalidate.8*
%{_mandir}/man8/era_restore.8*
%{_mandir}/man8/thin_check.8*
%{_mandir}/man8/thin_delta.8*
%{_mandir}/man8/thin_dump.8*
%{_mandir}/man8/thin_ls.8*
%{_mandir}/man8/thin_metadata_pack.8*
%{_mandir}/man8/thin_metadata_size.8*
%{_mandir}/man8/thin_metadata_unpack.8*
%{_mandir}/man8/thin_repair.8*
%{_mandir}/man8/thin_restore.8*
%{_mandir}/man8/thin_rmap.8*
%{_mandir}/man8/thin_trim.8*
