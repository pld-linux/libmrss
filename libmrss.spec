Summary:	C library for parsing, writing and creating RSS files or streams
Summary(pl.UTF-8):	Biblioteka obsługująca parsowanie, tworzenie i zapisywanie kanałów RSS
Name:		libmrss
Version:	0.19.2
Release:	2
License:	LGPL v2
Group:		Development/Libraries
Source0:	http://www.autistici.org/bakunin/libmrss/%{name}-%{version}.tar.gz
# Source0-md5:	a6f66b72898d27270e3a68007f90d62b
URL:		http://www.autistici.org/bakunin/libmrss/
BuildRequires:	curl-devel
BuildRequires:	libnxml-devel
Requires:	libnxml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mRSS is a C library for parsing, writing and creating RSS (0.91, 0.92,
1.0, 2.0) files or streams

%description -l pl.UTF-8
Biblioteka obsługująca parsowanie, tworzenie i zapisywanie kanałów RSS

%package devel
Summary:	Header files for mRss library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki mRss
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel
Requires:	libnxml-devel

%description devel
Header files for mRss library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki mRss.

%package static
Summary:	Static mRss library
Summary(pl.UTF-8):	Statyczna biblioteka mRss
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static mRss library.

%description static -l pl.UTF-8
Statyczna biblioteka mRss.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libmrss.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmrss.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmrss.so
%{_includedir}/mrss.h
%{_pkgconfigdir}/mrss.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/libmrss.a
