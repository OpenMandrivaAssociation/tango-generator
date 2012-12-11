%define name tango-generator
%define version 3.2.1
%define unmangled_version 3.2.1
%define release 3
%define _unpackaged_files_terminate_build 0

Summary: Tango Generator
Name: %{name}
Version: %{version}
Release: %mkrel %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: GPLv2
Group: Graphical desktop/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Requires: python >= 2.4
Requires: librsvg2
Requires: imagemagick
Requires: pygtk2.0 >= 2.6.3-2
BuildRequires:	python-devel
Url: http://mejogid.ohallwebservices.com/

%description
An icon theme creation application

%prep
%setup -q -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database
%update_desktop_database

%postun
%update_mime_database
%update_desktop_database

%files
%defattr(-,root,root)
%doc COPYING AUTHORS README
%_bindir/tango-generator
%_datadir/applications/tango-generator.desktop
%_iconsdir/*/*/*/*
%_datadir/mime/packages/*.xml
%_datadir/tango-generator
%py_puresitedir/*


%changelog
* Mon Nov 08 2010 Funda Wang <fwang@mandriva.org> 3.2.1-3mdv2011.0
+ Revision: 595052
- update file list
- update file list

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 3.2.1-3mdv2010.0
+ Revision: 445348
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 3.2.1-2mdv2009.1
+ Revision: 326008
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sat Jan 05 2008 Jérôme Soyer <saispo@mandriva.org> 3.2.1-1mdv2008.1
+ Revision: 145835
- import tango-generator


