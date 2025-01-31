%define major 1
%define libname %mklibname svg %{major}
%define devname %mklibname svg -d

Summary:	A generic SVG library
Name:		libsvg
Version:	0.1.4
Release:	27
License:	LGPLv2
Group:		System/Libraries
Url:		https://cairographics.org/snapshots/
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.bz2
Patch0:		libsvg-0.1.4-libpng-1.5.patch
Patch1:		libsvg-0.1.4-libtool-2.x.patch
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libxml-2.0)

%description
A generic SVG library.

%package -n	%{libname}
Summary:	A generic SVG library
Group:		System/Libraries

%description -n	%{libname}
A generic SVG library.

%package -n	%{devname}
Summary:	Libraries and include files for developing with libsvg
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package provides the necessary development libraries and include
files to allow you to develop with libsvg.

%prep
%autosetup -p1
mv configure.in configure.ac

%build
export LIBS="$(pkg-config --libs libxml-2.0` `pkg-config --libs libpng) -ljpeg -lz -lm"

%configure --disable-static
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libsvg.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/libsvg.pc
