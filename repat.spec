Summary:	The RDF Parser Toolkit
Summary(pl):	Narzêdzia do analizy RDF
Name:		repat
Version:	20001224
Release:	1
License:	LGPL or MPL
Group:		Libraries
# Source0-md5:	58a36eeb50adbdefa41639745dc1e8b3
Source0:	http://injektilo.org/rdf/%{name}.2000-12-24.zip
Patch0:		%{name}-redland.patch
URL:		http://injektilo.org/rdf/repat.html
BuildRequires:	expat-devel >= 1.95.0
BuildRequires:	libtool
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
repat is a callback-based RDF parser built on James Clark's expat.
It's implemented in Standard C and should be usable in most
environments.

%description -l pl
repat to oparty na callbackach analizator RDF zbudowany w oparciu o
expat Jamesa Clarka. Jest zaimplementowany w standardowym C i powinien
nadawaæ siê do u¿ytku w wiêkszo¶ci ¶rodowisk.

%package devel
Summary:	Header file for repat library
Summary(pl):	Plik nag³ówkowy biblioteki repat
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	expat-devel >= 1.95.0

%description devel
Header file for repat library.

%description devel -l pl
Plik nag³ówkowy biblioteki repat.

%package static
Summary:	repat static library
Summary(pl):	Statyczna biblioteka repat
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
repat static library.

%description static -l pl
Statyczna biblioteka repat.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
libtool --mode=compile %{__cc} %{rpmcflags} -o rdfparse.lo -c rdfparse.c
libtool --mode=link %{__cc} %{rpmldflags} -o librepat.la rdfparse.lo -rpath %{_libdir} -lexpat
%{__cc} %{rpmcflags} -o rdfdump.o -c rdfdump.c
libtool --mode=link %{__cc} %{rpmldflags} -o rdfdump rdfdump.o librepat.la

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/repat,%{_bindir}}

libtool --mode=install install librepat.la $RPM_BUILD_ROOT%{_libdir}
libtool --mode=install install rdfdump $RPM_BUILD_ROOT%{_bindir}
install rdfparse.h $RPM_BUILD_ROOT%{_includedir}/repat

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES.txt
# COPYING not included - it refers to included expat only
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/repat

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
