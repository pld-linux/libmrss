Summary:	C library for parsing, writing and creating RSS files or streams
Summary(pl.UTF-8):	Biblioteka obsługująca parsowanie, tworzenie i zapisywanie kanałów RSS
Name:		libmrss
Version:	0.19.0
Release:	1
License:	LGPL v2
Group:		Development/Libraries
Source0:	http://www.autistici.org/bakunin/libmrss/%{name}-%{version}.tar.gz
# Source0-md5:	d2a4968001b7af86111f2281810f049f
URL:		http://www.autistici.org/bakunin/libmrss/
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
