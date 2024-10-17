%define _name OpenOffice.org-cs-templates

Summary: Czech templates for the OpenOffice.org suite
Name:    %{_name} 
Version: 012004
Release: %mkrel 5
License: LGPL
Group:   Office
Source0: OpenOffice.org-cs-templates.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: OpenOffice.org-l10n-cs
URL: https://oo-cs.sourceforge.net/templates/index.php

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



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 012004-5mdv2011.0
+ Revision: 616418
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 012004-4mdv2010.0
+ Revision: 430214
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 012004-3mdv2009.0
+ Revision: 266090
- rebuild early 2009.0 package (before pixel changes)

* Sun May 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 012004-2mdv2009.0
+ Revision: 205687
- Should not be noarch ed

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 012004-1mdv2008.1
+ Revision: 141036
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import OpenOffice.org-cs-templates


* Mon Sep 27 2004 Robert Vojta <robert.vojta@mandrake.org> 012004-1mdk
- initial package

