Name:    kde-base-artwork 
Summary: KDE Base Artwork 
Version: 4.10.5
Release: 1%{?dist}

# http://techbase.kde.org/Policies/Licensing_Policy
License: LGPLv3+ 
URL:     http://www.kde.org/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/%{version}/src/%{name}-%{version}.tar.xz
BuildArch: noarch

BuildRequires: kdelibs4-devel >= %{version}
# for ksplash and ownership of %%{_kde4_appsdir}/ksplash
Requires: kde-workspace

Conflicts: kde-workspace-ksplash-themes < 4.8.80

%description
%{summary}.


%prep
%setup -q 


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform} 


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files 
%doc COPYING
%{_kde4_appsdir}/ksplash/Themes/Default/


%changelog
* Sun Jun 30 2013 Than Ngo <than@redhat.com> - 4.10.5-1
- 4.10.5

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- 4.10.4

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Mon Apr 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-1
- 4.10.2

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.1-1
- 4.10.1

* Fri Feb 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-1
- 4.10.0

* Tue Jan 22 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.98-1
- 4.9.98

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.97-1
- 4.9.97

* Wed Dec 19 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.95-1
- 4.9.95

* Tue Dec 04 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.90-1
- 4.9.90

* Mon Dec 03 2012 Than Ngo <than@redhat.com> - 4.9.4-1
- 4.9.4

* Sat Nov 03 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.3-1
- 4.9.3

* Fri Sep 28 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.2-1
- 4.9.2

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 4.9.1-1
- 4.9.1

* Fri Jul 27 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.0-1
- 4.9.0
- Requires: kde-workspace

* Thu Jul 12 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.97-1
- 4.8.97

* Fri Jun 29 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.95-1
- 4.8.95
- fix URL
- BR: kdelibs4-devel

* Tue Jun 12 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.90-1
- first try

