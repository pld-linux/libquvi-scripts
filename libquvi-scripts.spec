Summary:	Embedded lua scripts that libquvi uses for parsing the media details
Summary(pl.UTF-8):	Skrypty osadzonego lua wykorzystywane przez libquvi do analizy multimediów
Name:		libquvi-scripts
Version:	0.4.9
Release:	1
License:	LGPL v2.1+
Group:		Applications
Source0:	http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
# Source0-md5:	a7f3dad2e2809857e876726813bba1be
URL:		http://quvi.sourceforge.net/
BuildRequires:	autoconf >= 2.67
BuildRequires:	automake >= 1:1.11
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
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
%{_npkgconfigdir}/libquvi-scripts.pc
