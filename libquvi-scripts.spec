Summary:	Embedded lua scripts that libquvi uses for parsing the media details
Summary(pl.UTF-8):	Skrypty osadzonego lua wykorzystywane przez libquvi do analizy multimediów
Name:		libquvi-scripts
Version:	0.9.20131130
Release:	2
License:	AGPL v3+
Group:		Applications
Source0:	http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
# Source0-md5:	46ddfd887260a515199c2e1ba8c46d8a
URL:		http://quvi.sourceforge.net/
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	lua-socket
# build process and tests aren't noarch, but built package is
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains embedded lua scripts that libquvi uses for
parsing the media details.

%description -l pl.UTF-8
Ten pakiet zawiera skrypty osadzonego lua, wykorzystywane przez
libquvi przy analizie szczegółów danych multimedialnych.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
%if "%{_gnu}" != "-gnux32"
	--build=%{_host} \
	--host=%{_host} \
%endif
	--disable-silent-rules \
	--with-nsfw \
	--with-nlfy
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_npkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/%{name}
%{_mandir}/man7/libquvi-scripts.7*
%{_mandir}/man7/quvi-modules.7*
%{_mandir}/man7/quvi-modules-3rdparty.7*
%{_npkgconfigdir}/libquvi-scripts-0.9.pc
