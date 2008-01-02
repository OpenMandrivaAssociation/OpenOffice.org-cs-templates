%define _name OpenOffice.org-cs-templates

Summary: Czech templates for the OpenOffice.org suite
Name:    %{_name} 
Version: 012004
Release: %mkrel 1
License: LGPL
Group:   Office
Source0: OpenOffice.org-cs-templates.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: OpenOffice.org-l10n-cs
URL: http://oo-cs.sourceforge.net/templates/index.php
BuildArch: noarch

%description
Czech templates for the OpenOffice.org suite.

%prep
%setup -q -n %{_name}

%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/openoffice/share/template/czech
cp -a writer/*.stw $RPM_BUILD_ROOT/%{_libdir}/openoffice/share/template/czech/
cp -a calc/*.stc $RPM_BUILD_ROOT/%{_libdir}/openoffice/share/template/czech/
cp -a draw/*.std $RPM_BUILD_ROOT/%{_libdir}/openoffice/share/template/czech/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS index.html
%{_libdir}/openoffice/share/template/czech/*.stw
%{_libdir}/openoffice/share/template/czech/*.stc
%{_libdir}/openoffice/share/template/czech/*.std

