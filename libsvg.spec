%define major   1
%define libname %mklibname svg %{major}

Summary:	A generic SVG library
Name:		libsvg
Version:	0.1.4
Release:	%mkrel 3
License:	LGPL
Group:		System/Libraries
URL:		http://cairographics.org/snapshots/
Source:		http://cairographics.org/snapshots/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig >= 0.8
BuildRequires:	libxml2-devel
BuildRequires:	png-devel
BuildRequires:	jpeg-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A generic SVG library.

%package -n	%{libname}
Summary:	A generic SVG library
Group:		System/Libraries

%description -n	%{libname}
A generic SVG library.

%package -n	%{libname}-devel
Summary:	Libraries and include files for developing with libsvg
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}

%description -n	%{libname}-devel
This package provides the necessary development libraries and include
files to allow you to develop with libsvg.

%prep
%setup -q

%build
%configure2_5x
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/*.so.%{major}*

%files -n %{libname}-devel
%defattr(644,root,root,755)
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.a
%{_includedir}/*
%{_libdir}/pkgconfig/libsvg.pc


