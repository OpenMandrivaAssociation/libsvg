%define major   1
%define libname %mklibname svg %{major}

Summary:	A generic SVG library
Name:		libsvg
Version:	0.1.4
Release:	13
License:	LGPL
Group:		System/Libraries
URL:		http://cairographics.org/snapshots/
Source:		http://cairographics.org/snapshots/%{name}-%{version}.tar.bz2
Patch:		libsvg-0.1.4-libpng-1.5.patch
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	jpeg-devel

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
%patch -p1 -b .libpng15~

%build
export LIBS="`pkg-config --libs libxml-2.0` `pkg-config --libs libpng` -ljpeg -lz -lm"

%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/*.so.%{major}*

%files -n %{libname}-devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/libsvg.pc

%changelog
* Tue Jan 31 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.1.4-12
+ Revision: 769964
- Fix build with libpng 1.5
- Drop libpng 1.2 dependency
- Clean up spec file

  + Oden Eriksson <oeriksson@mandriva.com>
    - attempt to relink against libpng15.so.15

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-10
+ Revision: 661529
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-9mdv2011.0
+ Revision: 602607
- rebuild

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-8mdv2010.1
+ Revision: 488782
- rebuilt against libjpeg v8

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-7mdv2010.0
+ Revision: 416625
- rebuilt against libjpeg v7

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-6mdv2009.0
+ Revision: 229787
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-4mdv2008.1
+ Revision: 178948
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Thu Feb 15 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.4-2mdv2007.0
+ Revision: 121269
- rebuild
- spec file clean
- Import libsvg

* Mon Mar 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.1.4-1mdk
- New release 0.1.4
- use mkrel
- use mkrel

* Wed Mar 09 2005 Götz Waschk <waschk@linux-mandrake.com> 0.1.3-1mdk
- spec fixes
- New release 0.1.3

* Sat Jun 05 2004 Marcel Pol <mpol@mandrake.org> 0.1.2-2mdk
- buildrequires (slbd)

* Fri Jun 04 2004 Marcel Pol <mpol@mandrake.org> 0.1.2-1mdk
- initial mandrake package

