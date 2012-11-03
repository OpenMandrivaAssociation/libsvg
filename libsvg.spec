%define major 1
%define libname %mklibname svg %{major}
%define develname %mklibname svg -d

Summary:	A generic SVG library
Name:		libsvg
Version:	0.1.4
Release:	13
License:	LGPL
Group:		System/Libraries
URL:		http://cairographics.org/snapshots/
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.bz2
Patch0:		libsvg-0.1.4-libpng-1.5.patch
BuildRequires:	pkgconfig >= 0.8
BuildRequires:	libxml2-devel
BuildRequires:	png-devel
BuildRequires:	jpeg-devel

%description
A generic SVG library.

%package -n %{libname}
Summary:	A generic SVG library
Group:		System/Libraries

%description -n %{libname}
A generic SVG library.

%package -n %{develname}
Summary:	Libraries and include files for developing with libsvg
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Obsoletes:	%{mklibname svg 1}-devel < 0.1.4-13

%description -n	%{develname}
This package provides the necessary development libraries and include
files to allow you to develop with libsvg.

%prep
%setup -q
%apply_patches

%build
export LIBS="`pkg-config --libs libxml-2.0` `pkg-config --libs libpng` -ljpeg -lz -lm"

%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std
rm %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/libsvg.pc
