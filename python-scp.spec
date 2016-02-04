%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global srcname scp

Name:           python-%{srcname}
Version:        0.7.1
Release:        6%{?dist}
Summary:        Scp module for paramiko

License:        LGPLv2+
URL:            https://github.com/jbardin/scp.py
Source0:        https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
# For tests
BuildRequires:  python-paramiko
Requires:       python-paramiko

%description
The scp.py module uses a paramiko transport to send and receive files via the
scp1 protocol. This is the protocol as referenced from the openssh scp program,
and has only been tested with this implementation.


%prep
%setup -q -n %{srcname}-%{version}
rm -r %{srcname}.egg-info


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%check
%{__python2} setup.py test

 
%files
%doc LICENSE.txt PKG-INFO README.md
%{python2_sitelib}/*


%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 Orion Poplawski <orion@cora.nwra.com> - 0.7.1-3
- Add missing BR python-paramiko for tests

* Wed Feb 19 2014 Orion Poplawski <orion@cora.nwra.com> - 0.7.1-2
- Add missing BR python-setuptools
- Other minor cleanup
- Add %%check

* Fri Feb 14 2014 Orion Poplawski <orion@cora.nwra.com> - 0.7.1-1
- Initial package
