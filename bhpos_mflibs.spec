%define	major 2
%define libname	%mklibname bhpos_mflibs %{major}

Summary:	BananaPOS bhpos_mflibs libraries
Name:		bhpos_mflibs
Version:	2.0.0
Release:	%mkrel 0.beta3.4
License:	GPL
Group:		System/Libraries
URL:		http://www.bananahead.com
Source0:	ftp://bananahead.com/pub/bhpos2/stable/%{name}-%{version}.tar.bz2
Patch0:         bhpos_mflibs-2.0.0-fix-build.patch 
BuildRequires:	bhpos_commonlibs-devel >= 2.0.0
BuildRequires:	bhpos_hwlib-devel >= 2.0.0
BuildRequires:	bhpos_base >= 2.0.0
BuildRequires:	bhpos_base-devel >= 2.0.0
BuildRequires:	gtkmm2.4
BuildRequires:	gtkmm2.4-devel
BuildRequires:	intltool
BuildRequires:	libtool >= 1.5
BuildRequires:	libxml2 >= 2.5.8
BuildRequires:	libusb-devel >= 0.1.8
BuildRequires:	libxml++-devel >= 2.6
BuildRequires:	pkgconfig
BuildRequires:	MySQL-devel
BuildRequires:  perl(XML::Parser)
BuildRequires:	gettext-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
BananaPOS mflibs libraries, are required by the server (mysql version).

%package -n	%{libname}
Summary:	BananaPOS bhpos_mflibs libraries
Group:          System/Libraries
Requires:	bhpos_base >= 2.0.0

%description -n	%{libname}
BananaPOS bhpos_mflibs libraries, are required by the server (mysql version).

%package -n	%{libname}-devel
Summary:	Development files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Requires:	bhpos_commonlibs-devel >= 2.0.0
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libname}-devel
Development files for the %{name} library

%prep

%setup -q -n %{name}-%{version}
%patch0 -p1

%build
sh ./autogen.sh

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname} -f %{name}.lang
%defattr(-,root,root)
%doc COPYING ChangeLog NEWS README
%{_libdir}/bhpos2.0/lib*.so.*
%dir %{_datadir}/bhpos2.0/images
%{_datadir}/bhpos2.0/images/*.png

%files -n %{libname}-devel
%defattr(-, root, root)  
%{_libdir}/bhpos2.0/*.a
%{_libdir}/bhpos2.0/*.la
%{_libdir}/bhpos2.0/*.so
%{_libdir}/pkgconfig/bhmflib-2.0.pc
%{_includedir}/bhpos2.0/widget/*.h
%{_includedir}/bhpos2.0/*.h



