Summary:	Embedded lua scripts that libquvi uses for parsing the media details
Name:		libquvi-scripts
Version:	0.4.6
Release:	1
License:	LGPL v2+
Group:		Applications
Source0:	http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
# Source0-md5:	623337087a76a537beba47d8df079b8f
URL:		http://quvi.sourceforge.net/
BuildRequires:	autoconf >= 2.67
BuildRequires:	automake
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains embedded lua scripts that libquvi uses for
parsing the media details.

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
