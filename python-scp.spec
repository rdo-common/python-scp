%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global srcname scp
%global pypi_name scp

Name:           python-%{srcname}
Version:        0.10.2
Release:        5%{?dist}
Summary:        Scp module for paramiko

License:        LGPLv2+
URL:            https://github.com/jbardin/scp.py
Source0:        https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-setuptools
BuildRequires:  python2-devel

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

# For tests
BuildRequires: python-paramiko, python3-paramiko

%description
The scp.py module uses a paramiko transport to send and receive files via the
scp1 protocol. This is the protocol as referenced from the openssh scp program,
and has only been tested with this implementation.

%package -n     python2-%{pypi_name}
Summary:        scp module for paramiko
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python-paramiko
%description -n python2-%{pypi_name}
The scp.py module uses a paramiko transport to send and receive files via the
scp1 protocol. This is the protocol as referenced from the openssh scp program,
and has only been tested with this implementation.

%package -n     python3-%{pypi_name}
Summary:        scp module for paramiko
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-paramiko
%description -n python3-%{pypi_name}
The scp.py module uses a paramiko transport to send and receive files via the
scp1 protocol. This is the protocol as referenced from the openssh scp program,
and has only been tested with this implementation.

%prep
%setup -q -n %{srcname}-%{version}
rm -r %{srcname}.egg-info

%build
%py2_build
%py3_build

%install
%py3_install
%py2_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{pypi_name}
%doc README.rst PKG-INFO
%license LICENSE.txt
%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.rst PKG-INFO
%license LICENSE.txt
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-4
- Rebuild for Python 3.6

* Wed Nov 16 2016 Ben Rosser <rosser.bjr@gmail.com> - 0.10.2-3
- Remove ownership of python3_sitelib/__pycache__ from the python3 subpackage.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 03 2016 Ben Rosser <rosser.bjr@gmail.com> - 0.10.2-1
- Updated package to latest upstream version.
- Modernized spec file.
- Added support for Python 3.

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
