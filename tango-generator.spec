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

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc COPYING AUTHORS README
